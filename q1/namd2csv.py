#!/usr/bin/env python

import sys

fhin=open(sys.argv[1], 'r')
fhout=open(sys.argv[2], 'w')

fhout.write('TS,BOND,ANGLE,DIHED,IMPRP,ELECT,VDW,BOUNDARY,MISC,KINETIC,TOTAL,TEMP,POTENTIAL,TOTAL3,TEMPAVG,PRESSURE,GPRESSURE,VOLUME,PRESSAVG,GPRESSAVG\n')

lines=fhin.readlines();

for l in lines:
    if(l[0:7]=='ENERGY:'):
        fields=l.split()
        lout=""
        for f in fields[1:-1]:
            lout=lout + f +','
        fhout.write(lout + '\n')

fhout.close()

            
