colvarsTrajFrequency 1000

colvar {
    name soluteX
    distanceZ {
        main {
            atomnumbers { 1 2 }
        }

        ref {
            dummyAtom ( 0.000, 0.000, 0.000 )
        }

        axis (1.0, 0.0, 0.0)
    }
}

colvar {
    name soluteY
    distanceZ {
        main {
            atomnumbers { 1 2 }
        }

        ref {
            dummyAtom ( 0.000, 0.000, 0.000 )
        }

        axis (0.0, 1.0, 0.0)
    }
}


colvar {
    name soluteZ
    distanceZ {
        main {
            atomnumbers { 1 2 }
        }

        ref {
            dummyAtom ( 0.000, 0.000, 0.000 )
        }

        axis (0.0, 0.0, 1.0)
    }
}



harmonic {
    name soluterestX
    colvars  soluteX
    centers 0.0
    forceConstant 10.0
}

harmonic {
    name soluterestY
    colvars  soluteY
    centers 0.0
    forceConstant 10.0
}

harmonic {
    name soluterestZ
    colvars  soluteZ
    centers 0.0
    forceConstant 10.0
}

