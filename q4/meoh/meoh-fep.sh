#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --job-name=fep
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=24:00:00

module purge
module load namd-multicore/2.13

namd2 +p8 fep.conf > fep.out

