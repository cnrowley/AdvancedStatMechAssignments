import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

folding=np.genfromtxt('mdtraj.txt', delimiter=',', skip_header=1)

fig=plt.figure()

fig.set_size_inches(3.25, 9)

ax1 = fig.add_subplot(611)    # The big subplot
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

fig.subplots_adjust(bottom=0.10, top=0.95, left=0.2)
# h, s, contacts, rmsd, beta, g
t=folding[:,0]*0.1 # convert to ns
hbonds=folding[:,1]
sasa=folding[:,2]
contacts=folding[:,3]
rmsd=folding[:,4]
beta=folding[:,5]
Rgyr=folding[:,6]
                 
weights=np.repeat(1.0, 100)/100

# plot the time series of the root-mean-square-displacement
plt.subplot(611)
plt.plot(t, rmsd, '-', label=r'RMSD')

# use convolve to generate running average
plt.plot(t[50:-49], np.convolve(rmsd, weights, mode='valid'))
ax1.set(xlim=(0,500), ylabel=r'RMSD ($\AA$)')
ax1.set_xticklabels([])

# plot the time series of the radius of gyration

plt.subplot(612)
plt.plot(t, Rgyr, '-', label=r'$r_{gyr} (\AA)$')
plt.plot(t[50:-49], np.convolve(Rgyr, weights, mode='valid'))
ax2.set(xlim=(0,500), ylabel=r'$r_{gyr} (\AA)$')
ax2.set_xticklabels([])

# plot the time series of the number of intramolecular hydrogen bonds
plt.subplot(613)
plt.plot(t, hbonds, '-', label=r'$n_{hbond}$')
plt.plot(t[50:-49], np.convolve(hbonds, weights, mode='valid'))
ax3.set(xlim=(0,500), ylabel='$n_{hbond}$')
ax3.set_xticklabels([])

# plot the time series of the solvent accessible surface area
plt.subplot(614)
plt.plot(t, sasa, '-', label=r'SASA ($\AA^2$)')
plt.plot(t[50:-49], np.convolve(sasa, weights, mode='valid'))
ax4.set(xlim=(0,500), ylabel=r'SASA ($\AA^2$)')
ax4.set_xticklabels([])

# plot the time series of the percentage of residues forming a beta sheet secondary structure
plt.subplot(615)
plt.plot(t, beta, '-', label='% beta')
plt.plot(t[50:-49], np.convolve(beta, weights, mode='valid'))
ax5.set(xlim=(0,500),  ylabel='% beta')
ax5.set_xticklabels([])

# plot the time series of the percentage of native contacts formed

plt.subplot(616)
plt.plot(t, contacts, '-', label='native contacts')
plt.plot(t[50:-49], np.convolve(contacts, weights, mode='valid'))
ax6.set(xlim=(0,500), xlabel='time (ns)', ylabel='native contacts')

plt.show()
plt.savefig('q9.pdf')
plt.savefig('q9.png')

