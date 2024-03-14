import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate moving average
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

# Function to read the file and extract timestep, potential energy, and volume
def read_file(file_path):
    timesteps = []
    potential_energy = []
    volume = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('ENERGY:'):
                values = line.split()
                timesteps.append(float(values[1]) * 2e-3 / 10000)  # Convert timestep to ns (each timestep is 2 fs)
                potential_energy.append(float(values[13]))  # Energy in kcal/mol
                volume.append(float(values[18]))
    return timesteps, potential_energy, volume

# Function to plot the graphs
def plot_graphs(timesteps, data, ylabel, output_path):
    num_plots = len(data)
    fig, axs = plt.subplots(num_plots, 1, figsize=(3.25, 4*num_plots))

    for i in range(num_plots):
        axs[i].plot(timesteps, data[i], label='Original Data')
        moving_mean = moving_average(data[i], window_size=1000)  # Calculate moving mean with window size 10
        axs[i].plot(timesteps[len(timesteps)-len(moving_mean):], moving_mean, color='red', label='Moving Mean')
        axs[i].set_xlabel('Time (ns)')
        axs[i].set_ylabel(ylabel[i])
        axs[i].legend()

    fig.tight_layout()
    plt.savefig(output_path + '.png')
    plt.savefig(output_path + '.pdf')
    plt.show()

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python plot.py <namd output file name>")
        return

    file_path = sys.argv[1]
    output_path = 'equilibriation'

    timesteps, potential_energy, volume = read_file(file_path)

    plot_graphs(timesteps, [potential_energy, volume], ['Potential Energy (kcal/mol)', 'Volume (cubic angstrom)'], output_path)

if __name__ == "__main__":
    main()
