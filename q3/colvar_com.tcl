colvar {
    name protcom
    distance {
        group1 {
           atomsFile unfold-rest.pdb
           atomsCol  O
           atomsColValue 1.0
        }

        group2 {
            dummyAtom ( 0.000, 0.000, 0.000 )
        }
    }
}

harmonic {
  name restcom
  colvars  protcom
  centers 0.0
  forceConstant 1.0
}


