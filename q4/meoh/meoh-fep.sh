#PBS -l walltime=60:00:00
#PBS -l nodes=1:ppn=8
#PBS -N meoh-fep
#PBS -o std.out
#PBS -q qwork
#PBS -j oe

cd $PBS_O_WORKDIR

module load namd

namd2 +p8 fep.conf > fep.out

