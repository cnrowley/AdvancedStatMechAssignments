import sys
import MDAnalysis as mda
import matplotlib.pyplot as plt
from MDAnalysis.analysis import rdf
plt.rcParams.update({
    "font.family": "DejaVu Sans",  # Use Helvetica or Arial
    "font.size": 10,         # Minimum 8, recommended 10 pt
    "axes.labelsize": 10,    # Axis labels size
    "axes.titlesize": 0,    # Title size
    "xtick.labelsize": 8,    # Tick labels size
    "ytick.labelsize": 8,
    "legend.fontsize": 8,    # Legend font size
    "lines.linewidth": 1,    # Line thickness
    "axes.linewidth": 1,     # Axis line thickness
    "savefig.dpi": 600,      # High-resolution output
    "xtick.major.size": 5,   # Major tick size
    "xtick.minor.size": 2.5, # Minor tick size
    "ytick.major.size": 5,
    "ytick.minor.size": 2.5,
    "xtick.major.width": 0.8, # Major tick width
    "ytick.major.width": 0.8,
    "xtick.minor.width": 0.5, # Minor tick width
    "ytick.minor.width": 0.5,
    "legend.frameon": False, # No legend box
})

# Read command-line arguments
traj_file = sys.argv[1]          # Trajectory file name
cell_length = float(sys.argv[2]) # Cell length in angstroms
skip_frames = int(sys.argv[3])   # Number of frames to skip

# Load the trajectory
u = mda.Universe(traj_file, topology_format='XYZ', format='XYZ')

# Set the unit cell dimensions
u.dimensions = [cell_length, cell_length, cell_length, 90, 90, 90]

# Skip the specified number of frames
traj = u.trajectory

# Select all atoms
atoms = u.select_atoms('all')

# Calculate the radial distribution function (RDF)
rdf_calculator = rdf.InterRDF(atoms, atoms, range=(0, 12), nbins=100)
rdf_calculator.run(start=skip_frames)
print(rdf_calculator.results.rdf)

# Plot the RDF
plt.plot(rdf_calculator.results.bins[1:], rdf_calculator.results.rdf[1:])
plt.xlabel('Distance (Å)')
plt.ylabel('g(r)')
plt.xlim(0, 10)
plt.grid()
plt.show()
plt.savefig(sys.argv[4])
