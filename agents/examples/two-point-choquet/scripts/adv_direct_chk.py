from fractions import Fraction as Fr
from itertools import product
V=[Fr(k,2) for k in range(-6,7)]+[Fr(1,3),Fr(-7,3)]
P=list(product(V,V))
def ax(F):
    C=all(F((x[0]+c,x[1]+c))==F(x)+c for x in P for c in V)
    CA=all(F((x[0]+y[0],x[1]+y[1]))==F(x)+F(y) for x in P for y in P if (x[0]-x[1])*(y[0]-y[1])>=0)
    M=all(F(x)<=F(y) for x in P for y in P if x[0]<=y[0] and x[1]<=y[1])
    LI=all(F(x)==F((x[1],x[0])) for x in P)
    return (C,CA,M,LI)
pos=lambda t: t if t>0 else 0
W=[Fr(-1),Fr(0),Fr(1,3),Fr(1,2),Fr(1),Fr(2)]
ok=True
for a1 in W:
  for a2 in W:
    F=lambda x,a1=a1,a2=a2: min(x)+a1*pos(x[0]-x[1])+a2*pos(x[1]-x[0])
    r=ax(F); inb=lambda a: 0<=a<=1
    exp=(True,True,inb(a1) and inb(a2),a1==a2)
    if r!=exp: ok=False; print("mismatch",a1,a2,r,exp)
print("family ok",ok)
for name,F in [("2max",lambda x:2*max(x)),("5+min",lambda x:5+min(x)),("2max-min",lambda x:2*max(x)-min(x)),("x1",lambda x:x[0])]:
    print(name,ax(F))
