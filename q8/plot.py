import numpy as np
import matplotlib.pyplot as plt

deprotonated_pmf=np.genfromtxt('deprotonated/pmf_deprotonated.pmf')
protonated_pmf=np.genfromtxt('protonated/pmf_protonated.pmf')

ax=plt.axes()
fig = plt.gcf()
fig.set_size_inches(3.25, 3.25)
fig.subplots_adjust(bottom=0.15, left=0.15)

plt.plot(deprotonated_pmf[:,0], deprotonated_pmf[:,1], '-r', label='protonated')
plt.plot(protonated_pmf[:,0], protonated_pmf[:,1], '-b', label='deprotonated')
plt.legend()

ax.set(ylim=(0,15), xlabel=r'z $(\AA)$', ylabel='PMF (kcal/mol)')

plt.show()
plt.savefig('q8.pdf')
