#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output=mc.out
#SBATCH --mem-per-cpu=8096MB
#SBATCH --job-name=monte_carlo
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=3:00:00

./mc.x
