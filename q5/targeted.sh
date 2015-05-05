#$ -N targeted
#$ -l h_rt=24:00:00
#$ -pe openmp* 4
#$ -j y
#$ -cwd
#$ -S /bin/bash

module load namd/2.9-smp

namd2 +p4 tip4p-methanol-targeted.conf > tip4p-methanol-targeted.out
