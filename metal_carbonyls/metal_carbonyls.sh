#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output=qm_interaction.log
#SBATCH --mem-per-cpu=8096MB
#SBATCH --job-name=qm_carbonyl
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.1

$EBROOTORCA/orca co.inp > co.out
$EBROOTORCA/orca cr-co6.inp > cr-co6.out
$EBROOTORCA/orca fe-co6.inp > fe-co6.out
$EBROOTORCA/orca mn-co6.inp > mn-co6.out
$EBROOTORCA/orca os-co6.inp > os-co6.out
$EBROOTORCA/orca ru-co6.inp > ru-co6.out
$EBROOTORCA/orca ti-co6.inp > ti-co6.out
$EBROOTORCA/orca v-co6.inp > v-co6.out
