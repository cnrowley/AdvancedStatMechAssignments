colvarsTrajFrequency 100

colvar {
name phi
    dihedral {
	group1 {
	    atomnumbers 13
	}
	group2 {
	    atomnumbers 15
	}
	group3 {
	    atomnumbers 17
	}
	group4 {
	    atomnumbers 1
	}
    }
}

colvar {
name psi
    dihedral {
        group1 {
            atomnumbers 15
        }
        group2 {
            atomnumbers 17
        }
        group3 {
            atomnumbers 1
        }
        group4 {
            atomnumbers 3
        }
    }
}
