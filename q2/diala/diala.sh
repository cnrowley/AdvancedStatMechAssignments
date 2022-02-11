#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=diala
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load   StdEnv/2020  intel/2020.1.217 namd-multicore/2.14

namd2 +p8 diala.namd > diala.out

