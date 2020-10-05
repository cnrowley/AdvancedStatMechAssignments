import numpy as np
import matplotlib.pyplot as plt

import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA

import MDAnalysis.analysis.rms

# load experimental reference structure from PDB
ref = mda.Universe("2rvd.pdb", multiframe=False)

# load trajectory from mdcrd
trj = mda.Universe("pout", "mdcrd", topology_format="PRMTOP", format="NC")

# align trajectory with experimental structure by minimizing RMSD

alignment = align.AlignTraj(trj, ref, filename="aligned.dcd", select="backbone", match_atoms=False)
alignment.run()
rmsd=alignment.rmsd.T

# calculate radius of gyration of each frame

Rgyr = []
protein = trj.select_atoms("protein")
for ts in trj.trajectory:
    Rgyr.append(protein.radius_of_gyration())
Rgyr = np.array(Rgyr)

# read VMD data for secondary structure and number of hydrogen bonds

folding=np.genfromtxt('folding.dat', delimiter=',', skip_header=1)

fig=plt.figure()

fig.set_size_inches(3.25, 9)

ax1 = fig.add_subplot(511)    # The big subplot
ax2 = fig.add_subplot(512)
ax3 = fig.add_subplot(513)
ax4 = fig.add_subplot(514)
ax5 = fig.add_subplot(515)

fig.subplots_adjust(bottom=0.15, left=0.15)

weights=np.repeat(1.0, 100)/100

# plot the time series of the root-mean-square-displacement
plt.subplot(511)
plt.plot(folding[:,0], rmsd, '-', label=r'RMSD')

# use convolve to generate running average
plt.plot(folding[50:-49,0], np.convolve(rmsd, weights, mode='valid'))
ax1.set(xlim=(0,500), ylabel=r'RMSD ($\AA$)')
ax1.set_xticklabels([])

# plot the time series of the radius of gyration

plt.subplot(512)
plt.plot(folding[:,0], Rgyr, '-', label=r'$r_{gyr}$')
plt.plot(folding[50:-49,0], np.convolve(Rgyr, weights, mode='valid'))
ax2.set(xlim=(0,500), ylabel=r'$r_{gyr}$')
ax2.set_xticklabels([])

# plot the time series of the number of intramolecular hydrogen bonds
plt.subplot(513)
plt.plot(folding[:,0], folding[:,2], '-', label=r'$n_{hbond}$')
plt.plot(folding[50:-49,0], np.convolve(folding[:,2], weights, mode='valid'))
ax3.set(xlim=(0,500), ylabel='$n_{hbond}$')
ax3.set_xticklabels([])

# plot the time series of the solvent accessible surface area
plt.subplot(514)
plt.plot(folding[:,0], folding[:,3], '-', label=r'SASA ($\AA^2$)')
plt.plot(folding[50:-49,0], np.convolve(folding[:,3], weights, mode='valid'))
ax4.set(xlim=(0,500), ylabel=r'SASA ($\AA^2$)')
ax4.set_xticklabels([])

# plot the time series of the percentage of residues forming a beta sheet secondary structure
plt.subplot(515)
plt.plot(folding[:,0], folding[:,4], '-', label='% beta')
plt.plot(folding[50:-49,0], np.convolve(folding[:,4], weights, mode='valid'))
ax5.set(xlim=(0,500), xlabel='time (ns)', ylabel='% beta')

plt.show()
plt.savefig('q9.pdf')
