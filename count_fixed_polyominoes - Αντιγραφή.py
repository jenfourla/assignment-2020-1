import sys
import pprint
import argparse
g={}
neighbours=[]
nodes=[]
h=[]
if (sys.argv[1]="-p"):
    n=argv[2]
else:
    n=argv[1]
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

if (sys.argv[1]="-p"):
    print(g)
    print(CountFixedPolyominoes(g,(0,0), n,[],0))

else:
    print(CountFixedPolyominoes(g,(0,0), n,[],0))
    
def CountFixedPolyominoes(G,untried, n,p,c):
     
     found = true
     while (!(untried.__sizeof__()==0)):
         u=untried.pop()
         p.append(u)
         if (len(p)==n):
             c=c+1
         else:
             new_neighbors={}
             for v in G[u]:
                 if (!(untried.__contains__(v)and(!(p.__contains__(v)))):
                    for t in p:
                        if t!=u:
                            for j in G[t]:
                                if (v==j):
                                    found=false
                        else:
                            new_neighbors=new_neighbors+v
             new_untried = untried + new_neighbors
             CountFixedPolyominoes(G,new_untried,n,p,c)
        p.remove(u)
     return c

 

        


