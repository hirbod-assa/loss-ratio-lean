from fractions import Fraction as Q
from itertools import product
vals=[Q(n,2) for n in range(-4,5)]
pts=[(a,b) for a in vals for b in vals]   # includes ties x1=x2 and both orderings
def C(F): return all(F((x[0]+c,x[1]+c))==F(x)+c for x in pts for c in vals)
def com(x,y): return (x[0]-x[1])*(y[0]-y[1])>=0
def CA(F): return all(F((x[0]+y[0],x[1]+y[1]))==F(x)+F(y) for x in pts for y in pts if com(x,y))
def M(F): return all(F(x)<=F(y) for x in pts for y in pts if x[0]<=y[0] and x[1]<=y[1])
def LI(F): return all(F((x[1],x[0]))==F(x) for x in pts)
def axioms(F): return (C(F),CA(F),M(F),LI(F))
def target(a): return lambda x: a*max(x)+(1-a)*min(x)
# necessity incl. boundary a=0,1 ; and a outside [0,1] must fail M only
for a in [Q(0),Q(1),Q(1,3),Q(1,2),Q(-1),Q(2)]:
    print("a=",a,axioms(target(a)))
# two-weight family (general solution without LI): all four hold iff a1=a2 in [0,1]
ws=[Q(-1),Q(0),Q(1,2),Q(1),Q(2)]
ok=True
for a1,a2 in product(ws,ws):
    F=lambda x,a1=a1,a2=a2: min(x)+a1*max(x[0]-x[1],0)+a2*max(x[1]-x[0],0)
    ax=axioms(F); allh=all(ax); pred=(a1==a2 and 0<=a1<=1)
    if allh!=pred: ok=False; print("MISMATCH",a1,a2,ax)
    if (ax[:3]==(True,True,True))!=(0<=a1<=1 and 0<=a2<=1): ok=False; print("noLI mismatch",a1,a2)
print("two-weight family consistent:",ok)
# independence examples
print("drop C : 2max      ",axioms(lambda x:2*max(x)))
print("drop CA: 5+min     ",axioms(lambda x:5+min(x)))
print("drop M : 2max-min  ",axioms(target(Q(2))))
print("drop LI: x1        ",axioms(lambda x:x[0]))
# reconstruction: F(x) = min + F(1,0)*(max-min) recovers target
for a in [Q(0),Q(1),Q(2,5)]:
    F=target(a); A=F((1,0))
    assert all(F(x)==min(x)+A*(max(x)-min(x)) for x in pts) and F((0,0))==0
print("reconstruction ok")
