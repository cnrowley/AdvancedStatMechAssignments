#!/bin/bash
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --account=rrg-crowley-ac
#SBATCH --time=24:00:00
#SBATCH --job-name=folding

module purge
module load nixpkgs/16.09  gcc/7.3.0  cuda/9.2.148  openmpi/3.1.2

module load amber/18.10-18.11

${AMBERHOME}/bin/pmemd.cuda -O -p pout -i md-nvt.in -c restrt.eq -o mdout.nvt
