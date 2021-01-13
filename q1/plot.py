import numpy as np
import matplotlib.pyplot as plt

rdf_water=np.genfromtxt('tip4p/gofr.dat')
rdf_methane=np.genfromtxt('methane/gofr.dat')

print(rdf_water[:,0])
print(rdf_water[:,1])
ax=plt.axes()
plt.plot(rdf_water[:,0], rdf_water[:,1], '-r', label='water')
plt.plot(rdf_methane[:,0], rdf_methane[:,1], '-b', label='methane')

ax.set(xlim=(0,10), xlabel=r'r $(\AA)$', ylabel='g(r)')

plt.show()
plt.savefig('q1.pdf')
plt.savefig('q1.png')

