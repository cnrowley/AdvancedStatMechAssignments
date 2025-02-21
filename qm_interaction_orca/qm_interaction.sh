#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output=qm_interaction.log
#SBATCH --mem-per-cpu=8096MB
#SBATCH --job-name=qm_interaction
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.1

$EBROOTORCA/orca ar.inp > ar.out
$EBROOTORCA/orca co2.inp > co2.out
$EBROOTORCA/orca co2_monomer.inp > co2_monomer.out
$EBROOTORCA/orca h2o_dimer.inp > h2o_dimer.out
$EBROOTORCA/orca h2o_monomer.inp > h2o_monomer.out
$EBROOTORCA/orca nacl.inp > nacl.out
