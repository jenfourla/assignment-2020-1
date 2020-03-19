import sys
import pprint
import argparse
g={}
neighbours=[]
nodes=[]
h=[]


n=sys.argv[0]
metrhths_gr=0
k=1 
u=n-1
for i in range(-n+2,n):
    if(i<0):
        for j in range(1,k+1):
            
            h=[i,j]
            nodes.append(h)
            
        k=k+1
    elif(i==0):
        for j in range(0,n):
            h=[i,j]
            nodes.append(h)
    else:
        j=0
        while j<u:
           
           h=[i,j]
           nodes.append(h)
           j=j+1
        u=u-1
for l in nodes:
    
    if ((-n+2<=l[0]+1<=n-1)and(nodes.__contains__([l[0]+1,l[1]]))):
        
        y=[l[0]+1,l[1]]
        neighbours.append(y)
        
    if ((0<=l[1]+1<=n-1)and(nodes.__contains__([l[0],l[1]+1]))):
        y=[l[0],l[1]+1]
        neighbours.append(y)
    if ((-n+2<=l[0]-1<=n-1)and(nodes.__contains__([l[0]-1,l[1]]))):
        y=[l[0]-1,l[1]]
        neighbours.append(y)
    if ((0<=l[1]-1<=n-1)and(nodes.__contains__([l[0],l[1]-1]))):
        y=[l[0],l[1]-1]
        neighbours.append(y)
    for y in neighbours:
        print(l[0])
        if (metrhths_gr==0):
            d2 = {(l[0],l[1]):[y]}
            g.update(d2)
            
            metrhths_gr=metrhths_gr+1
        else:
            print((l[0],l[1]))
            d1= {(l[0],l[1]):[g[(l[0],l[1])],y]}
            g.update(d1)
    neighbours.clear()     
    metrhths_gr=0
 
 

        


