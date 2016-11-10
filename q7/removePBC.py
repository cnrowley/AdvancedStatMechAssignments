import sys

fh=open(sys.argv[1], 'r')
fhout=open(sys.argv[2], 'w')
lines=fh.readlines()
dim=float(sys.argv[3])
offset=[0,0,0,0]
data_prev=list(map(float,lines[1].split()))

print sys.argv[1]
print sys.argv[2]

for l in lines:
    if(l[0]=='#'):
        continue

    data=list(map(float,l.split()))
    for  i in range(1,4):
        if(  (data[i]-data_prev[i])>dim/2):
            offset[i]=offset[i]-dim
        if(  (data[i]-data_prev[i])<-dim/2):
            offset[i]=offset[i]+dim
    fhout.write(str(data[0]) + ' ' + str(data[1]+offset[1]) + ' ' +str(data[2]+offset[2]) + ' ' + str(data[3]+offset[3]) + '\n')
    data_prev=data

fhout.close()
