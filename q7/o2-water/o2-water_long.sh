#!/bin/bash
#SBATCH --account=rrg-crowley-ab
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=o2-water_long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load namd-multicore/2.13

namd2 +p8 eq_long.conf > eq_long.out
namd2 +p16 prod_long.conf > prod_long.out

