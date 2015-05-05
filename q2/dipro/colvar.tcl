colvarsTrajFrequency 100

colvar {
name phi
    dihedral {
	group1 {
	    atomnumbers 19
	}
	group2 {
	    atomnumbers 11
	}
	group3 {
	    atomnumbers 7
	}
	group4 {
	    atomnumbers 5
	}
    }
}

colvar {
name psi
    dihedral {
        group1 {
            atomnumbers 21
        }
        group2 {
            atomnumbers 19
        }
        group3 {
            atomnumbers 11
        }
        group4 {
            atomnumbers 7
        }
    }
}
