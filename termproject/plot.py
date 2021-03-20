import sys
import numpy as np
import matplotlib

def getdata(lines):
    time=[]
    pe=[]
    volume=[]

    for l in lines:
        if(l[0:7]=='ENERGY:'):
            y=l.split()
            time.append(float(y[1])/1000)
            pe.append(float(y[13]))
            volume.append(float(y[18])/1000)
                           
    return( (time, pe, volume) )

matplotlib.use('Agg')

import matplotlib.pyplot as plt


fh=open(sys.argv[1], 'r')
lines=fh.readlines()
fh.close()

(time, energies, volumes)=getdata(lines)
maxtime=max(time)

fig=plt.figure()

fig.set_size_inches(3.25, 4)

ax1 = fig.add_subplot(211)    # The big subplot
ax2 = fig.add_subplot(212)

fig.subplots_adjust(bottom=0.1, top=0.95, left=0.3, hspace=0.001)
# h, s, contacts, rmsd, beta, g
                 
weights=np.repeat(1.0, 10000)/10000

# plot the time series of the root-mean-square-displacement
plt.subplot(211)
plt.plot(time, energies, '-', label=r'Potential Energy')

# use convolve to generate running average

plt.plot(time[5000:-4999], np.convolve(energies, weights, mode='valid'))
ax1.set(xlim=(0, maxtime), xlabel='time (ps)', ylabel=r'Potential Energy (kcal/mol)')

ax1.set_xticklabels([])

# plot the time series of the radius of gyration

plt.subplot(212)
plt.plot(time, volumes, '-', label=r'Volume (nm$^3$)')
plt.plot(time[5000:-4999], np.convolve(volumes, weights, mode='valid'))
ax2.set(xlim=(0, maxtime), xlabel='time (ps)', ylabel=r'Volume (nm$^3$)')

plt.show()
plt.savefig('equilibriation.pdf')
plt.savefig('equiilbriation.png')

