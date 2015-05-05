colvarsTrajFrequency 100000

colvar {
  name slabcom
  distanceZ {
     main {
        atomsFile slab.pdb
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
       atomsFile solv.pdb
       atomsCol  B
       atomsColValue 1.0
     }
  
     ref {
       atomsFile slab.pdb
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
  forceConstant 5.0
}

harmonic {
   name soluterest1
   colvars  solute1
   forceConstant 5.0
   centers 35.0
   targetCenters 0.0
   targetNumSteps 3500000
}

