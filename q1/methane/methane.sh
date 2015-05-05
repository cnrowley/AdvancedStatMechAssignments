#PBS -N methane
#PBS -l h_rt=4:00:00
#PBS -l nodes=1:ppn=8
#PBS -j y
#PBS -cwd
#PBS -S /bin/bash

namd2 +p8 methane.conf > methane.out

