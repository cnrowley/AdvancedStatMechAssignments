#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --account=rrg-crowley-ac
#SBATCH --time=30:00
#SBATCH --job-name=folding_analysis

module purge

module load StdEnv/2023
module load scipy-stack/2023b

pip install mdtraj 
python analysis.py
