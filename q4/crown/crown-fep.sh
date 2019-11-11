#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --job-name=fep
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=12:00:00

module purge
module load namd-multicore/2.13

namd2 +p16 fep.conf > fep.out

