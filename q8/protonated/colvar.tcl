colvarsTrajFrequency 1000

 colvar {
     name zPos
     distanceZ {
 	main {
           atomsFile selcyc.pdb
           atomsCol  O
           atomsColValue 1.0
 	}

 	ref {
           atomsFile selsta.pdb
           atomsCol  O
           atomsColValue 1.0
	}
        axis (1.0, 0.0, 0.0) 
     }
     lowerBoundary -10
     upperBoundary 10.0
     lowerwallconstant 10
     upperwallconstant 10.0
     width 0.1
}

abf {
  colvars  zPos
  fullSamples 100
  hideJacobian
}

