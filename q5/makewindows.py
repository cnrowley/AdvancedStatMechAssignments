import os, shutil
import sys
import subprocess

def sub(cwd, w):
    pbslines="""#!/bin/bash
#SBATCH --account=rrg-crowley-ac
#SBATCH --output std.out
#SBATCH --mem-per-cpu=1024M 
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --time=12:00:00

module purge
module load namd-multicore/2.13

"""
    p=subprocess.Popen(['sbatch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    for l in pbslines:
        p.stdin.write(l.encode())
    p.stdin.write('#SBATCH -N ' + w + '\n\n')
    p.stdin.write( ('cd ' + cwd + '/' + w + '\n').encode() )
    
    p.stdin.write('namd2 +p8 tip4p-methanol-umb-eq.conf >& tip4p-methanol-umb-eq.out\n'.encode() )
    p.stdin.write('namd2 +p8 tip4p-methanol-umb-prod.conf >& tip4p-methanol-umb-prod.out\n'.encode() )
    p.stdin.close()
    p.wait()
    jobid=p.stdout.read()[:-1]
    p.stdout.close()
    print(jobid)


tclLines="""
colvarsTrajFrequency 100

colvar {
  name slabcom
  distanceZ {
     main {
        atomsFile ../slab.pdb
        atomsCol  B
        atomsColValue 1.0
     }

     ref {
       dummyAtom ( 0.000, 0.000, 0.000 )
     }
     axis (0.0, 0.0, 1.0)
  }
}
  
colvar {
  name solute1
  distanceZ {
     main {
       atomsFile ../solv.pdb
       atomsCol  B
       atomsColValue 1.0
     }
  
     ref {
       atomsFile ../slab.pdb
       atomsCol  B
       atomsColValue 1.0
     }
  
     axis (0.0, 0.0, 1.0)
   }
}

harmonic {
  name slabrestcom
  colvars  slabcom
  centers 0.0
  forceConstant 1
}

harmonic {
  name soluterest1
  colvars  solute1
  forceConstant 5.0  
"""

cwd=os.getcwd()

for i in range(0, 35):
    print('Window ' + str(i))
    print('Making subdirectory ' + 'window_' + str(i))
    os.mkdir('window_' + str(i))
    print('Copying window_' + str(i) + '.pdb to window_' + str(i) + '/initial.pdb')
    shutil.copyfile('window_' + str(i) + '.pdb', 'window_' + str(i) + '/initial.pdb')
    print('Copying tip4p-methanol-umb-eq.conf to window_' + str(i) + '/tip4p-methanol-umb-eq.conf')
    shutil.copyfile('tip4p-methanol-umb-eq.conf', 'window_' + str(i) + '/tip4p-methanol-umb-eq.conf')
    print('Copying tip4p-methanol-umb-prod.conf to window_' + str(i) + '/tip4p-methanol-umb-prod.conf')
    shutil.copyfile('tip4p-methanol-umb-prod.conf', 'window_' + str(i) + '/tip4p-methanol-umb-prod.conf')
    
    tclOutput=open('window_' + str(i) + '/umbrella.tcl', 'w')
    
    print('Writing TCL restraint for window ' + str(i))
    for l in tclLines:
        tclOutput.write(l.encode())
    tclOutput.write( ('   centers ' + str(float(34-i)) + '\n').encode() )
    tclOutput.write('}\n'.encode())
    tclOutput.close()
    
    sub(cwd, 'window_' + str(i))
    print("")
