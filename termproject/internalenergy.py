#!/usr/bin/env python

import re,sys

file=open(sys.argv[1],"r")
molnum=float(sys.argv[2])

fileline=file.readlines()

z=[]
e=[]
n=[]

def grep(string,file):
    expr = re.compile(string)
    etotal=0.0
    num=0
    for text in fileline:
        match = expr.search(text)
        if match != None:
            x=match.string
            y=list(x.split())
            etotal=etotal+float(y[13])
            num=num+1
        
    etotal=etotal*4.186/num
    return(etotal)

inte=grep("ENERGY:  ", file)
inte=inte/molnum

print 'INTERNAL ENERGY: ' + str(inte) + ' kJ/mol\n'
