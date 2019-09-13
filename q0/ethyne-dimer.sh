#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=methane
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module  load gaussian

g16 < ethyne-dimer.gjf > ethyne-dimer.out
