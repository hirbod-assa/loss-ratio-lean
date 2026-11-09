from fractions import Fraction as Fr
import itertools
vals=sorted(set([Fr(k,4) for k in range(-12,13)]+[Fr(1,3),Fr(-7,3),Fr(5,7)]))
pts=[(a,b) for a in vals for b in vals]
mx=lambda x:max(x); mn=lambda x:min(x)
fs={
'T0':lambda x:mn(x),'T1':lambda x:mx(x),'T1/3':lambda x:Fr(1,3)*mx(x)+Fr(2,3)*mn(x),
'2max':lambda x:2*mx(x),
'dropCA':lambda x:mn(x)+min(mx(x)-mn(x),1),
'2max-min':lambda x:2*mx(x)-mn(x),'2min-max':lambda x:2*mn(x)-mx(x),
'x1':lambda x:x[0],
}
cs=[Fr(-2),Fr(-1,3),Fr(1),Fr(5,2)]
def ax(F):
  C=all(F((x[0]+c,x[1]+c))==F(x)+c for x in pts for c in cs)
  CA=all(F((x[0]+y[0],x[1]+y[1]))==F(x)+F(y) for x in pts[::7] for y in pts[::5] if (x[0]-x[1])*(y[0]-y[1])>=0)
  M=all(F(x)<=F(y) for x in pts[::3] for y in pts[::4] if x[0]<=y[0] and x[1]<=y[1])
  LI=all(F(x)==F((x[1],x[0])) for x in pts)
  Ilo=all(mn(x)<=F(x) for x in pts); Ihi=all(F(x)<=mx(x) for x in pts)
  N=F((1,1))==1
  a=F((1,0)); inT= 0<=a<=1 and all(F(x)==a*mx(x)+(1-a)*mn(x) for x in pts)
  return dict(C=C,CA=CA,M=M,LI=LI,Ilo=Ilo,Ihi=Ihi,N=N,inT=inT)
for k,F in fs.items(): print(k,ax(F))
# dropCA = min(max, min+1)
print(all(fs['dropCA'](x)==min(mx(x),mn(x)+1) for x in pts))
