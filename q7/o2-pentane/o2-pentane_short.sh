#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --mail-type=ALL
#SBATCH --job-name=o2-pentane_short
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=3:00:00

module load nixpkgs/16.09  intel/2016.4  cuda/8.0.44
module load namd-verbs-smp/2.12

for CYCLE in  `seq 1 5`;
do
	echo "Cycle $CYCLE"
	export CYCLE=$CYCLE
	namd2 +p8 eq.conf > eq.log
	namd2 +p8 prod.conf > prod.log
	python ../removePBC.py prod_$CYCLE.colvars.traj prod_$CYCLE.unwrap.colvars.traj 33.20715
done
