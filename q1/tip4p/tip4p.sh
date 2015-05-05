#$ -N tip4p
#$ -l h_rt=4:00:00
#$ -pe openmp* 4
#$ -j y
#$ -cwd
#$ -S /bin/bash

../namd-2.9-smp/charmrun ../namd-2.9-smp/namd2 +p4 tip4p.conf > tip4p.out

