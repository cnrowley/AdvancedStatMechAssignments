#!/bin/bash
#SBATCH --account=rrg-crowley-ab
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=tip4p-fb
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load namd-multicore/2.13

namd2 +p8 tip4p-fb.conf > tip4p-fb.out

