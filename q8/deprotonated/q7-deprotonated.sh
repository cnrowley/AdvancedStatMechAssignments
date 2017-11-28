#!/bin/bash
#PBS -N rotaxane_deprotonated
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=4

module load namd/2.10-smp
namd2 +p4 pmf.conf > pmf.out

