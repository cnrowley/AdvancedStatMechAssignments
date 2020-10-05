import numpy as np
import matplotlib.pyplot as plt

#glycerol.txt
#headgroup.txt
#ion.txt
#tail.txt
#water.txt

dens_glycerol=np.genfromtxt('glycerol.txt', delimiter=',')
dens_headgroup=np.genfromtxt('headgroup.txt', delimiter=',')
dens_ion=np.genfromtxt('ion.txt', delimiter=',')
dens_tail=np.genfromtxt('tail.txt', delimiter=',')
dens_water=np.genfromtxt('water.txt', delimiter=',')

fig = plt.gcf()
fig.set_size_inches(3.25, 3.25)
fig.subplots_adjust(bottom=0.15, left=0.25, top=0.8)

ax=plt.axes()

plt.plot(dens_glycerol[:,0], dens_glycerol[:,1], '-', label='glycerol')
plt.plot(dens_headgroup[:,0], dens_headgroup[:,1], '-', label='headgroup')
plt.plot(dens_tail[:,0], dens_tail[:,1], '-', label='tails')
plt.plot(dens_ion[:,0], dens_ion[:,1], '-', label='ions')
plt.plot(dens_water[:,0], dens_water[:,1], '-', label='water')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)

ax.set(xlim=(-33,33), ylim=(0, 0.01), xlabel=r'Z $(\AA)$', ylabel=r'density (mol/$\AA^3$)')

plt.show()
plt.savefig('q6.pdf')
