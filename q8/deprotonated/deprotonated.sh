#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=rotaxane_unprot
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=12:00:00

module purge
module load namd-multicore/2.13

namd2 +p8 pmf.conf > pmf.out
