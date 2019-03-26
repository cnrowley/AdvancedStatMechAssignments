#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=md
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=3:00:00

./wham 0.0 35.0 150 0.001 298.15 1.0 wham.inp wham.out
