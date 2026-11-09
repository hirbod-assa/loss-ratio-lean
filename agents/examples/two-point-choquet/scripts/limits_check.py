# Exact-arithmetic check of the minimality analysis on a rational grid.
from fractions import Fraction as Q
from itertools import product
vals = [Q(n, 2) for n in range(-6, 7)] + [Q(1,3), Q(-7,3), Q(5,3)]
V = [(a, b) for a in vals for b in vals]          # includes constants and both orderings
C_ = [Q(n, 2) for n in range(-4, 5)] + [Q(1,3)]
mx = lambda x: max(x); mn = lambda x: min(x)
def T(a): return lambda x: a*mx(x) + (1-a)*mn(x)
def comon(x, y): return (x[0]-x[1])*(y[0]-y[1]) >= 0
def ax_C(F):  return all(F((x[0]+c, x[1]+c)) == F(x) + c for x in V for c in C_)
def ax_CA(F): return all(F((x[0]+y[0], x[1]+y[1])) == F(x) + F(y) for x in V for y in V if comon(x, y))
def ax_M(F):  return all(F(x) <= F(y) for x in V for y in V if x[0] <= y[0] and x[1] <= y[1])
def ax_LI(F): return all(F((x[0], x[1])) == F((x[1], x[0])) for x in V)
def ax_I(F):  return all(mn(x) <= F(x) <= mx(x) for x in V)
def ax_N(F):  return F((Q(1), Q(1))) == 1
def inT(F):
    a = F((Q(1), Q(0)))
    return 0 <= a <= 1 and all(F(x) == T(a)(x) for x in V)
cands = {
  "T(0)=min": T(Q(0)), "T(1)=max": T(Q(1)), "T(1/2)": T(Q(1,2)), "T(1/3)": T(Q(1,3)),
  "drop C : 2*max": lambda x: 2*mx(x),
  "drop C : zero": lambda x: Q(0),
  "drop CA: min+min(max-min,1)": lambda x: mn(x) + min(mx(x)-mn(x), Q(1)),
  "drop M : 2max-min": lambda x: 2*mx(x) - mn(x),
  "drop M : 2min-max": lambda x: 2*mn(x) - mx(x),
  "drop LI: x1": lambda x: x[0],
  "drop LI: x2/3+... (a=1/4 if x1>=x2, b=3/4 else)": lambda x: (x[1] + Q(1,4)*(x[0]-x[1])) if x[0] >= x[1] else (x[0] + Q(3,4)*(x[1]-x[0])),
}
print(f"{'functional':48s} C  CA M  LI | I  N  | inT")
for k, F in cands.items():
    r = [ax_C(F), ax_CA(F), ax_M(F), ax_LI(F), ax_I(F), ax_N(F), inT(F)]
    print(f"{k:48s} " + "  ".join("1" if b else "0" for b in r[:4]) + " | " + "  ".join("1" if b else "0" for b in r[4:6]) + "  | " + ("1" if r[6] else "0"))
