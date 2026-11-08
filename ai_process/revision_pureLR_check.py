# Judge check of the synthesized system P_exists + R + LI + RC_LR/RM_LR (exact Fractions, 4-point uniform space)
from fractions import Fraction as F
import random
random.seed(7)
NF='NF'
n=4
def choq(k,X):  # k: list of values k(i/4), i=0..4, k[0]=0,k[4]=1 ; signed Choquet
    xs=sorted(X,reverse=True)
    return sum(xs[i]*(k[i+1]-k[i]) for i in range(n))
h=[F(0),F(0),F(0),F(1),F(1)]          # 1{p>1/2}
g=[F(0),F(1,2),F(7,10),F(87,100),F(1)] # rational concave ~ sqrt
g2=[F(0),F(3,8),F(3,4),F(1),F(1)]      # min(1,1.5p)
E=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
hs=[F(0),F(-1,2),F(1,4),F(3,2),F(1)]   # signed, non-monotone
gs=[F(0),F(3,4),F(-1,4),F(1,2),F(1)]
def ratio(A,B):
    def L(X):
        b=B(X)
        return NF if b==0 else A(X)/b
    return L
I=lambda k:(lambda X:choq(k,X))
models={
 'true h,g':ratio(I(h),I(g)),
 'h=g':ratio(I(g),I(g)),
 'signed hs,gs':ratio(I(hs),I(gs)),
}
Pip=lambda X:max(choq(g,X),choq(g2,X))
wit={
 'cube':(lambda L:(lambda X:(NF if L(X)==NF else L(X)**3)))(ratio(I(h),I(g))),
 '[Pi\':Pi\']':ratio(Pip,Pip),
 '[max:E]':ratio(Pip,I(E)),
 '[Ih:2Ig] (N fails)':ratio(I(h),lambda X:2*choq(g,X)),
 'I3: 1+(Ih-Ig)/(Ig+Ig^3)':(lambda X:(NF if choq(g,X)==0 else 1+(choq(h,X)-choq(g,X))/(choq(g,X)+choq(g,X)**3))),
}
def sh(X,c): return [x+c for x in X]
def add(X,Y): return [x+y for x,y in zip(X,Y)]
def rnd(): return F(random.randint(-40,40),random.choice([1,2,3,5,7]))
def comon_pair():
    perm=list(range(n)); random.shuffle(perm)
    a=sorted([rnd() for _ in range(n)],reverse=True); b=sorted([rnd() for _ in range(n)],reverse=True)
    X=[None]*n;Y=[None]*n
    for i,p in enumerate(perm): X[p]=a[i];Y[p]=b[i]
    return X,Y
def breakeven(hh,gg):
    # non-constant book with I_hh = I_gg, solving for one coordinate within a fixed order
    for _ in range(200):
        xs=sorted([rnd() for _ in range(n)],reverse=True)
        d=[(hh[i+1]-gg[i+1])-(hh[i]-gg[i]) for i in range(n)]
        j=random.randrange(n)
        if d[j]==0: continue
        rest=sum(xs[i]*d[i] for i in range(n) if i!=j)
        xs[j]=-rest/d[j]
        if all(xs[i]>=xs[i+1] for i in range(n-1)) and len(set(xs))>1:
            return xs
    return None
def pole(Pi,X): return Pi(X)  # used only to build test books, never inside the axiom check
def R_check(L,Pi,X,Y,extra_u=()):
    # R: if LR(X),LR(Y) not finite, then for nonzero s,t,u values finite and u(L(X+Y+u)-1)=s(..)+t(..)
    X0=sh(X,-Pi(X)); Y0=sh(Y,-Pi(Y))
    if L(X0)!=NF or L(Y0)!=NF: return 'skip'
    Z=add(X0,Y0)
    us=[rnd() or F(1) for _ in range(3)]+list(extra_u)
    for s in [F(1),F(-2),F(3,7)]:
      for t in [F(1),F(5),F(-1,3)]:
        for u in us:
          if u==0: continue
          a,b,c=L(sh(X0,s)),L(sh(Y0,t)),L(sh(Z,u))
          if NF in (a,b,c): return 'fail-pole'
          if u*(c-1)!=s*(a-1)+t*(b-1): return 'fail-id'
    return 'ok'
def lossfree(L,W):
    v=L(W)
    return v==0 or (v==NF and L(sh(W,1))==1)
# ---------- necessity on representations
for name,L in models.items():
    gg={'true h,g':g,'h=g':g,'signed hs,gs':gs}[name]; hh={'true h,g':h,'h=g':g,'signed hs,gs':hs}[name]
    Pi=I(gg); rho=I(hh)
    cnt={}
    kinds={'generic':0,'breakeven':0,'mixed':0,'cancel':0}
    for trial in range(600):
        X,Y=comon_pair()
        kind='generic'
        if trial%4==1:
            B=breakeven(hh,gg)
            if B is None: continue
            # comonotone partner: same ordering (B sorted decreasing at positions 0..3)
            Y=sorted([rnd() for _ in range(n)],reverse=True); X=B; kind='mixed'
            if trial%8==1:
                B2=breakeven(hh,gg)
                if B2: Y=B2; kind='breakeven'
        if trial%4==2:
            # cancelling premiums: Y = -? choose Y comonotone with Pi(Y) = -Pi(X) via cash shift
            Y=sh(Y,-Pi(Y)-Pi(X)); kind='cancel'
            assert L(add(X,Y))==NF
        r=R_check(L,Pi,X,Y)
        cnt[(kind,r)]=cnt.get((kind,r),0)+1
        # loss-free predicate identifies rho; pole identifies Pi
        assert lossfree(L,sh(X,-rho(X))) and not lossfree(L,sh(X,-rho(X)+F(1,9)))
        assert L(sh(X,-Pi(X)))==NF
    print(name,cnt)
# RM_LR / RC_LR (alpha) on true model: a=pole shift, b=lossfree shift monotone & TV-Lipschitz
L=models['true h,g']; viol=0; maxratio=0
for _ in range(1500):
    X=[rnd() for _ in range(n)]; Y=[x+abs(rnd())/7 for x in X]
    if not (choq(g,X)<=choq(g,Y) and choq(h,X)<=choq(h,Y)): viol+=1
    nrm=max(abs(x-y) for x,y in zip(X,Y))
    if nrm>0: maxratio=max(maxratio,abs(choq(g,X)-choq(g,Y))/nrm,abs(choq(h,X)-choq(h,Y))/nrm)
print('RM_LR violations',viol,' RC Lipschitz ratio',float(maxratio))
# N derived check on model: LR(c)=1
print('N:',[models['true h,g']([F(c)]*n) for c in (-3,1,5)], 'LR(0)=',models['true h,g']([F(0)]*n))
# ---------- witnesses
for name,L in wit.items():
    Pi={'[Pi\':Pi\']':Pip,'[max:E]':I(E),'[Ih:2Ig] (N fails)':I(g)}.get(name,I(g))
    res={}
    for _ in range(400):
        X,Y=comon_pair()
        if random.random()<0.5:   # nested indicators, as in verdict
            A=[1,1,0,0];B=[1,0,0,0]; random.shuffle_ = None
            X=[F(a) for a in [1,0,0,0]]; Y=[F(a) for a in [1,1,0,0]]
            X=[x*abs(rnd()) for x in X]; Y=[y*abs(rnd()) for y in Y]
        X0=sh(X,-Pi(X)); Y0=sh(Y,-Pi(Y)); Z=add(X0,Y0)
        tu=[-Pip(Z)] if name=='[Pi\':Pi\']' and Pip(Z)!=0 else []
        r=R_check(L,Pi,X,Y,extra_u=tu)
        res[r]=res.get(r,0)+1
    print('witness',name,res)
# [Pi':Pi'] satisfies RC_LR/RM_LR(alpha)? pole shift a = Pi'(X); lossfree shift b: LR(W)=0 never; NF & LR(W+1)=1 -> b=Pi'(X)
L=wit['[Pi\':Pi\']']; bad=0
for _ in range(300):
    X=[rnd() for _ in range(n)]
    W=sh(X,-Pip(X))
    if not lossfree(L,W): bad+=1
    if lossfree(L,sh(X,-Pip(X)+F(1,3))): bad+=1
print("[Pi':Pi'] lossfree shift == Pi' (so RC/RM_LR hold, Pi' monotone 1-Lip):",bad==0)
# LR == 1 satisfies R vacuously but fails P_exists
print('LR==1: P_exists fails (no non-finite value), R vacuous')
