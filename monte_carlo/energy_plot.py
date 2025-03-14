import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "font.family": "DejaVu Sans",  # Use Helvetica or Arial
    "font.size": 10,         # Minimum 8, recommended 10 pt
    "axes.labelsize": 10,    # Axis labels size
    "axes.titlesize": 0,    # Title size
    "xtick.labelsize": 8,    # Tick labels size
    "ytick.labelsize": 8,
    "legend.fontsize": 8,    # Legend font size
    "lines.linewidth": 1,    # Line thickness
    "grid.linewidth": 0.5,   # Grid lines
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

# Read the data
filename = 'energy.dat'
data = np.loadtxt(filename)

# Extract columns
x = data[:, 0]
y = data[:, 1]

# Create the plot
plt.step(x, y)
plt.xlabel('Step')
plt.ylabel(r'$\mathcal{V}$ (kJ/mol)')
plt.show()
# Save the plot to disk
plt.savefig('energy_plot.png')
