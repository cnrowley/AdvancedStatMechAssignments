#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=rotaxane_unprot
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module load nixpkgs/16.09  intel/2016.4  cuda/8.0.44
module load namd-verbs-smp/2.12

namd2 +p8 pmf.conf > pmf.out

