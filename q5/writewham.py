#!/usr/bin/env python

import os

for i in range(0,35):
    fname='window_' + str(i) + '/methanol-interface-prod.colvars.traj'
    if(not os.path.exists(fname)):
        continue
    
    fh=open('window_' + str(i) + '/methanol-interface-prod.colvars.traj', 'r')
    lines=fh.readlines()
    fh.close()

    fhout=open('z/z_' + str(i), 'w')

    for l in lines[1:]:
        if(l[0]!='#'):
            f=l.split()
            if(len(f)==3):
                com=float(f[1])
                ch3oh_z=float(f[2])
                fhout.write(f[0] + ' ' + str(ch3oh_z) + '\n')
    fhout.close()
