#!/bin/bash
#SBATCH --account=def-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M
#SBATCH --job-name=co2-dimer
#SBATCH --ntasks-per-node=8
#SBATCH --nodes=1
#SBATCH --time=24:00:00

module load gaussian
g16 < co2-dimer.gjf > co2-dimer.out

