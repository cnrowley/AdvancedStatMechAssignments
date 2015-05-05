#PBS -l walltime=60:00:00
#PBS -l nodes=1:ppn=8
#PBS -N fold
#PBS -o std.out
#PBS -q qwork
#PBS -j oe

cd $PBS_O_WORKDIR

module purge
module load gcc/4.8.3

./namd2pace +p8 fold.conf > fold.out

