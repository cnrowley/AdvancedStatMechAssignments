#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys

def parse_orca_output(filepath):
    """Parse ORCA output file to extract MO energies."""
    mo_energies = []
    with open(filepath, 'r') as file:
        in_mo_section = False
        lines=file.readlines()
        c=0
        while c<len(lines):
            if("ORBITAL ENERGIES" in lines[c]):
                break
            c+=1
        c+=4
        while c<len(lines):
            # Stop parsing when we reach the end of the MO energies section
            # Extract MO energies
            columns = lines[c].split()
            if len(columns) != 4:
                break

            occupancy=int(float(columns[1]))
            if(occupancy<2):
                break
            energy = float(columns[2])  # MO energy is typically in the 3rd column
            c=c+1
    
    return (energy)


for name in ['tico6.log', 'vco6.log', 'crco6.log', 'mnco6.log', 'feco6.log', 'ru-co6.log', 'os-co6.log']:
    homo_energy = parse_orca_output(name)
    print(name + ' ' + str(homo_energy))
