import sys, os

fh=open(sys.argv[1], 'r')
fhout=open(sys.argv[2], 'w')

lines=fh.readlines()
en=None
for i in range(0, len(lines)):
    if(lines[i][0:33]==" Counterpoise corrected energy = "):
        fields=lines[i+4].split()
        en=float(fields[3])

    if(lines[i][0:15]==' ! R1    R(1,2)'):
        fields=lines[i].split()
        r=float(fields[3])

        if(en != None):
            fhout.write(str(r) + ',' + str(en) + '\n')
        
fhout.close()
