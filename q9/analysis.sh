#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --account=rrg-crowley-ab
#SBATCH --time=30:00
#SBATCH --job-name=folding_analysis

module purge

module load nixpkgs/16.09
module load python/3.7.0
module load scipy-stack/2019b

pip install mdtraj --no-index --user

python analysis.py 
