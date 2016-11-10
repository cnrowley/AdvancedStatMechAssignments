#!/bin/bash
#PBS -N o2-water_short
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=4

cd $PBS_O_WORKDIR
module load namd/2.10-smp

for CYCLE in  `seq 1 5`;
do
	echo "Cycle $CYCLE"
	export CYCLE=$CYCLE
	namd2 +p4 eq.conf > eq.log
	namd2 +p4 prod.conf > prod.log
	python ../removePBC.py prod_$CYCLE.colvars.traj prod_$CYCLE.unwrap.colvars.traj 33.20715
done
