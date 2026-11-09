# Judge's independent check, exact arithmetic (fractions.Fraction), no external libraries.
# Part A: finite-model solve. Unknowns F(x) for x in G={-N..N}^2. Axioms imposed wherever all points lie in G.
#   Solve the linear system exactly, report the dimension of the solution set, then impose (M)/(I) and
#   report the feasible parameter region.
# Part B: families and witnesses on a rational grid (generic, ties, both orderings, non-integers).
from fractions import Fraction as Fr
import itertools
N=2
G=[(i,j) for i in range(-N,N+1) for j in range(-N,N+1)]
LAST=[(1,1),(1,0),(0,1)]  # put parameters last so Gauss-Jordan leaves them free
G=[p for p in G if p not in LAST]+LAST
idx={p:k for k,p in enumerate(G)}; n=len(G)
inG=lambda p:p in idx
add=lambda x,y:(x[0]+y[0],x[1]+y[1])
como=lambda x,y:(x[0]-x[1])*(y[0]-y[1])>=0
def rows(C=True,CA=True,LI=True):
    R=[]
    if CA:
        for x in G:
            for y in G:
                s=add(x,y)
                if como(x,y) and inG(s):
                    r=[Fr(0)]*(n+1); r[idx[s]]+=1; r[idx[x]]-=1; r[idx[y]]-=1; R.append(r)
    if C:
        for x in G:
            for c in range(-2*N,2*N+1):
                s=(x[0]+c,x[1]+c)
                if c and inG(s):
                    r=[Fr(0)]*(n+1); r[idx[s]]+=1; r[idx[x]]-=1; r[n]=Fr(c); R.append(r)
    if LI:
        for x in G:
            r=[Fr(0)]*(n+1); r[idx[x]]+=1; r[idx[(x[1],x[0])]]-=1; R.append(r)
    return R
def solve(R):
    R=[r[:] for r in R]; piv=[]; row=0
    for col in range(n):
        p=next((i for i in range(row,len(R)) if R[i][col]!=0),None)
        if p is None: continue
        R[row],R[p]=R[p],R[row]; pv=R[row][col]; R[row]=[v/pv for v in R[row]]
        for i in range(len(R)):
            if i!=row and R[i][col]!=0:
                f=R[i][col]; R[i]=[a-f*b for a,b in zip(R[i],R[row])]
        piv.append(col); row+=1
    if any(all(v==0 for v in r[:n]) and r[n]!=0 for r in R[row:]): return None
    free=[c for c in range(n) if c not in piv]
    # F = part + sum_k t_k * basis_k ; express each unknown as affine function of free vars
    expr={}
    for f in free: e=[Fr(0)]*(len(free)+1); e[free.index(f)]=Fr(1); expr[f]=e
    for i,c in enumerate(piv):
        e=[Fr(0)]*(len(free)+1); e[-1]=R[i][n]
        for k,f in enumerate(free): e[k]=-R[i][f]
        expr[c]=e
    return free,expr
def describe(tag,C,CA,LI):
    free,expr=solve(rows(C,CA,LI))
    print(f"[{tag}] solution dimension = {len(free)}; free unknowns at {[G[f] for f in free]}")
    return free,expr
def ineqs(free,expr,mode):
    # returns normalized linear inequalities  sum w_k t_k + b >= 0
    out=set()
    def push(e):
        if all(v==0 for v in e[:-1]):
            assert e[-1]>=0, "infeasible constant inequality"; return
        s=max(abs(v) for v in e[:-1]); out.add(tuple(v/s for v in e))
    if mode=='M':
        for x in G:
            for y in G:
                if x!=y and x[0]<=y[0] and x[1]<=y[1]:
                    push([a-b for a,b in zip(expr[idx[y]],expr[idx[x]])])
    if mode=='I':
        for x in G:
            push([a-(min(x) if k==len(free) else 0) for k,a in enumerate(expr[idx[x]])])
            push([(max(x) if k==len(free) else 0)-a for k,a in enumerate(expr[idx[x]])])
    return out
def region(S,verts,box):
    # S: inequalities w.t+b>=0. Claim: feasible set == polytope with vertices verts, described by inequalities box.
    implied=all(sum(w*v for w,v in zip(e[:-1],V))+e[-1]>=0 for e in S for V in verts)  # every ineq holds on polytope
    present=all(any(all(x==y for x,y in zip(e,f)) for e in S) for f in box)          # every facet ineq is in S
    return implied and present, len(S)
F_=Fr
# A1: C,CA,LI -> expect 1-dim, param a=F(1,0), F = min + a(max-min); M (and I) give a in [0,1]
free,expr=describe("C+CA+LI",True,True,True)
print("  F = min + a(max-min), a=F(0,1)=F(1,0), on G:",free==[idx[(0,1)]] and all(expr[idx[x]]==[F_(max(x)-min(x)),F_(min(x))] for x in G))
print("  (M) feasible set == [0,1] (exact, #ineq):",region(ineqs(free,expr,'M'),[(0,),(1,)],[(F_(1),F_(0)),(F_(-1),F_(1))]))
print("  (I) feasible set == [0,1] (exact, #ineq):",region(ineqs(free,expr,'I'),[(0,),(1,)],[(F_(1),F_(0)),(F_(-1),F_(1))]))
# A2: C,CA (no LI) -> expect 2-dim, params a1=F(1,0), a2=F(0,1)
free,expr=describe("C+CA",True,True,False)
ok=[G[f] for f in free]==[(1,0),(0,1)] and all(expr[idx[x]]==[F_(max(x[0]-x[1],0)),F_(max(x[1]-x[0],0)),F_(min(x))] for x in G)
print("  F = min + a1(x1-x2)^+ + a2(x2-x1)^+ on G:",ok)
box=[(F_(1),F_(0),F_(0)),(F_(-1),F_(0),F_(1)),(F_(0),F_(1),F_(0)),(F_(0),F_(-1),F_(1))]
print("  (M) feasible set == [0,1]^2 (exact, #ineq):",region(ineqs(free,expr,'M'),[(0,0),(1,0),(0,1),(1,1)],box))
# A3: CA,LI (no C) -> expect 2-dim, params k=F(1,1), a=F(1,0): F = k min + a(max-min); M gives 0<=a<=k
free,expr=describe("CA+LI",False,True,True)
ok=[G[f] for f in free]==[(1,1),(0,1)] and all(expr[idx[x]]==[F_(min(x)),F_(max(x)-min(x)),F_(0)] for x in G)
print("  F = F(1,1) min + F(0,1)(max-min) on G:",ok)
# cone {0<=a<=k}: generators (k,a)=(1,0),(1,1); test inequalities on generators (homogeneous) and facets a>=0, k-a>=0
S=ineqs(free,expr,'M')
print("  (M) feasible set == {0<=F(1,0)<=F(1,1)} (exact, #ineq):",
      all(e[-1]==0 for e in S) and region(S,[(1,0),(1,1)],[(F_(0),F_(1),F_(0)),(F_(1),F_(-1),F_(0))]))
print("  (I) feasible set == {F(1,1)=1, 0<=F(1,0)<=1} (exact, #ineq):",
      region(ineqs(free,expr,'I'),[(1,0),(1,1)],[(F_(0),F_(1),F_(0)),(F_(0),F_(-1),F_(1))]),
      "and pins k:", any(e[:2]==(F_(1),F_(0)) and e[2]==-1 for e in ineqs(free,expr,'I')) and any(e[:2]==(F_(-1),F_(0)) and e[2]==1 for e in ineqs(free,expr,'I')))

# Part B: witnesses and families on a rational grid
vals=sorted(set([Fr(k,2) for k in range(-6,7)]+[Fr(1,3),Fr(-7,3),Fr(5,7)]))
P=[(a,b) for a in vals for b in vals]
cs=[Fr(k,2) for k in range(-4,5)]+[Fr(1,3)]
mx,mn=max,min
cnt={'C':0,'CA':0,'M':0,'LI':0}
def ax(F):
    C=CA=M=LI=True
    for x in P:
        for c in cs:
            cnt['C']+=1; C&= F((x[0]+c,x[1]+c))==F(x)+c
        cnt['LI']+=1; LI&= F(x)==F((x[1],x[0]))
        for y in P:
            if como(x,y): cnt['CA']+=1; CA&= F(add(x,y))==F(x)+F(y)
            if x[0]<=y[0] and x[1]<=y[1]: cnt['M']+=1; M&= F(x)<=F(y)
    I=all(mn(x)<=F(x)<=mx(x) for x in P)
    a=F((1,0)); inT= 0<=a<=1 and all(F(x)==a*mx(x)+(1-a)*mn(x) for x in P)
    return ''.join('T' if v else 'F' for v in (C,CA,M,LI)),I,inT
T=lambda a:(lambda x:a*mx(x)+(1-a)*mn(x))
W={'T(0)=min':T(Fr(0)),'T(1)=max':T(Fr(1)),'T(1/2)':T(Fr(1,2)),'T(2/7)':T(Fr(2,7)),
   'T(-1)':T(Fr(-1)),'T(2)=2max-min':T(Fr(2)),
   '2max':lambda x:2*mx(x),'zero':lambda x:Fr(0),'5+min':lambda x:5+mn(x),
   'min(max,min+1)':lambda x:min(mx(x),mn(x)+1),'2min-max':lambda x:2*mn(x)-mx(x),'x1':lambda x:x[0],
   'min+1/4(x1-x2)^+ +3/4(x2-x1)^+':lambda x:mn(x)+Fr(1,4)*max(x[0]-x[1],0)+Fr(3,4)*max(x[1]-x[0],0),
   '3max+min (no C)':lambda x:3*mx(x)+mn(x)}
print("\nPart B  (C CA M LI) | I | inClass")
for k,F in W.items(): print(f"  {k:34s} {ax(F)}")
print("  identity min+min(max-min,1)==min(max,min+1):",all(mn(x)+min(mx(x)-mn(x),1)==min(mx(x),mn(x)+1) for x in P))
fam_ok=True
for a1,a2 in itertools.product([Fr(-1),Fr(0),Fr(1,3),Fr(1),Fr(3,2)],repeat=2):
    s,_,_=ax(lambda x:mn(x)+a1*max(x[0]-x[1],0)+a2*max(x[1]-x[0],0))
    fam_ok&= s==('TT'+('T' if 0<=a1<=1 and 0<=a2<=1 else 'F')+('T' if a1==a2 else 'F'))
print("  two-weight family: C,CA always; M iff a1,a2 in [0,1]; LI iff a1=a2:",fam_ok)
print("  points:",len(P),"axiom instances evaluated:",cnt)
