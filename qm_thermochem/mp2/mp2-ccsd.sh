#!/bin/bash
#SBATCH --account=def-crowley-ab
#SBATCH --output=mp2_ccsd.log
#SBATCH --mem-per-cpu=8096MB
#SBATCH --job-name=mp2_ccsd
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=24:00:00

module purge

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.1

$EBROOTORCA/orca co2.inp > co2.out
$EBROOTORCA/orca ch4.inp > ch4.out
$EBROOTORCA/orca nh3.inp > nh3.out
$EBROOTORCA/orca h2o.inp > h2o.out
$EBROOTORCA/orca h2.inp > h2.out
$EBROOTORCA/orca o2.inp > o2.out
$EBROOTORCA/orca n2.inp > n2.out

$EBROOTORCA/orca co2-ccsdt.inp > co2-ccsdt.out
$EBROOTORCA/orca ch4-ccsdt.inp > ch4-ccsdt.out
$EBROOTORCA/orca nh3-ccsdt.inp > nh3-ccsdt.out
$EBROOTORCA/orca h2o-ccsdt.inp > h2o-ccsdt.out
$EBROOTORCA/orca h2-ccsdt.inp > h2-ccsdt.out
$EBROOTORCA/orca o2-ccsdt.inp > o2-ccsdt.out
$EBROOTORCA/orca n2-ccsdt.inp > n2-ccsdt.out
