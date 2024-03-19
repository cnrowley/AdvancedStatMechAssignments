#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M
#SBATCH --mail-type=ALL
#SBATCH --job-name=mp_lr
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load   StdEnv/2023
module load   scipy-stack/2023b
module load python/3.11
module load gcc/12.3
module load rdkit/2023.09.3

python melting_point_lr.py > lr.out
