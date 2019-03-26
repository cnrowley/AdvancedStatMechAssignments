#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=fold
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=24:00:00

./namd2pace +p8 fold.conf > fold.out

