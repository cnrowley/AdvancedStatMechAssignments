#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=o2-water_long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load   StdEnv/2020  intel/2020.1.217 namd-multicore/2.14

namd2 +p8 eq_long.conf > eq_long.out
namd2 +p16 prod_long.conf > prod_long.out

