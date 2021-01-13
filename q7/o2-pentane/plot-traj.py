import numpy as np
import matplotlib.pyplot as plt

def readtraj(fname, dim):
    fh=open(fname, 'r')

    lines=fh.readlines()

    offset=[0, 0, 0, 0]
    data_prev=list(map(float,lines[1].split()))
    traj=[]
    
    for l in lines:
        if(l[0]=='#'):
            continue

        data=list(map(float,l.split()))
        
        for  i in range(1, 4):
            if(  (data[i]-data_prev[i])>dim/2):
                offset[i]=offset[i]-dim
            if(  (data[i]-data_prev[i])<-dim/2):
                offset[i]=offset[i]+dim
        traj.append([data[0], data[1] + offset[1], data[2] + offset[2], data[3]+offset[3]])

        data_prev=data

    return(np.array(traj))


fh=open('eq.xsc', 'r')
lines=fh.readlines()
fh.close()

box_length=float( lines[2].split()[1] )
print(box_length)

ax=plt.axes()
ax.set(xlim=(-25,25), ylim=(-25,25), xlabel=r'X $(\AA)$', ylabel=r'Y $(\AA)$')

for i in range(1, 6):
    trj=readtraj('prod_' + str(i) + '.colvars.traj', box_length)
    plt.plot(trj[:,1], trj[:,2], '-', label=str(i))

plt.legend()
plt.show()
plt.savefig('o2-pentane_traj.pdf')
plt.savefig('o2-pentane_traj.png')

