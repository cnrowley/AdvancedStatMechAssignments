colvarsTrajFrequency 100

colvar {
name phi
    dihedral {
	group1 {
	    atomnumbers 5
	}
	group2 {
	    atomnumbers 7
	}
	group3 {
	    atomnumbers 9
	}
	group4 {
	    atomnumbers 12
	}
    }
}

colvar {
name psi
    dihedral {
        group1 {
            atomnumbers 7
        }
        group2 {
            atomnumbers 9
        }
        group3 {
            atomnumbers 12
        }
        group4 {
            atomnumbers 14
        }
    }
}
