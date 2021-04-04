#!/bin/bash
#SBATCH --account=rrg-crowley-ab
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=o2-water_short
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module purge
module load namd-multicore/2.13

for CYCLE in  `seq 1 5`;
do
	echo "Cycle $CYCLE"
	export CYCLE=$CYCLE
	namd2 +p8 eq.conf > eq.log
	namd2 +p8 prod.conf > prod.log
	python ../removePBC.py prod_$CYCLE.colvars.traj prod_$CYCLE.unwrap.colvars.traj 33.20715
done
