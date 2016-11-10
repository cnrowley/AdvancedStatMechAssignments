#!/bin/bash
#PBS -N o2-pentane_long
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=4

cd $PBS_O_WORKDIR

module load namd/2.10-smp

namd2 +p4 prod_long.conf > prod_long.out

