import sys
import pprint
import argparse
sys.setrecursionlimit(10**6)

g={}
neighbours=[]
nodes=[]
h=[]
if (sys.argv[1]=="-p"):
    b=sys.argv[2]
    n=int(b)
    u=n-1
else:
    b=sys.argv[1]
    n=int(b)
    u=n-1
metrhths_gr=0
k=1 

def CountFixedPolyominoes(G,untried,n,p,c):
    
    while(not(len(untried)==0)):
        found = True
        print("the value of untried is: ", untried)
        u = untried.pop()
        print("the NEW VALUE of untried is: ", untried)
        
        
        untried1=tuple(untried)
        u1 = tuple(u)
        p.append(u)
        p1 = tuple(p)
        if (len(p)==n):
             c=c+1
        else:
            
            new_neighbors = []
            
            for v in G[u1]:
                
                if  (((p1.count(v)==0))and(not(untried1.__contains__(v)))and(found)):
                    for t in p:
                        
                        if (t!=u):
                            
                            for j in G[t]:
                                if (v==j):
                                    found=False
                                else:
                                    new_neighbors.append(v)
                        else:
                            
                            new_neighbors.append(v)
                        
            new_untried = untried + new_neighbors
            
            CountFixedPolyominoes(G,new_untried,n,p,c)
        p.remove(u)
    return c
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
        
        if (metrhths_gr==0):
            d2 = {(l[0],l[1]):[y]}
            g.update(d2)
            
            metrhths_gr=metrhths_gr+1
        else:
            
            d1= {(l[0],l[1]):[g[(l[0],l[1])],y]}
            g.update(d1)
    neighbours.clear()     
    metrhths_gr=0

if (sys.argv[1]=="-p"):
    print(g)
    print(CountFixedPolyominoes(g,[(0,0)], n,[],0))
else:
    print(CountFixedPolyominoes(g,[(0,0)], n,[],0))    
 


   

 

        


