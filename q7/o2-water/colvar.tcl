colvarsTrajFrequency 50

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
