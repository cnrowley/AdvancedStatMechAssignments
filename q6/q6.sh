#$ -N q6
#$ -l h_rt=24:00:00
#$ -pe openmp* 4
#$ -j y
#$ -cwd
#$ -S /bin/bash

module load namd/2.10-smp
namd2 +p4 md.conf > md.out

