#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output=hf.log
#SBATCH --mem-per-cpu=8096MB
#SBATCH --job-name=products
#SBATCH --ntasks=4
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.1

$EBROOTORCA/orca products.inp > producys.out
