fhout=open('wham.inp', 'w')
for i in range(0, 35):
    fh=open('window_' + str(i) + '/umbrella.tcl', 'r')
    lines=fh.readlines()
    f=lines[-3].split()
    forceConstant=float(f[1])
    f=lines[-2].split()
    z_0=float(f[1])
    fhout.write('z/z_' + str(i) + ' ' + str(z_0) + ' ' + str(forceConstant) + '\n')

fhout.close()
