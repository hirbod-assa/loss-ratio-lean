# Judge report: two-point Choquet characterization (toy panel)

**Recommendation.** Adopt the *direct* proposal's theorem and proof. Use the *limits* proposal's (CA)-witness $\min\{\max(x),\min(x)+1\}$ in place of $5+\min(x)$, and turn its weakenings into one short remark. Both proposals are correct. No counterexample to either stated theorem exists, and my independent exact check confirms every finite claim.

## 1. Points of disagreement, checked

The two verdicts and the proposals do not disagree on any mathematical point. I checked the points the verdicts raised myself.

- **Limits, drop-(M) bullet.** The first pair offered is $(0,0)\le(0,1)$ with $F(0,1)=2\ge 0=F(0,0)$. This is *not* a violation of (M). The correct witness is $(-1,0)\le(0,0)$, where $F(-1,0)=1>0$. The verdict is right.
- **Limits, (iii) bullet.** The labels are swapped. $2\max-\min$ drops the half $F\le\max$, and $2\min-\max$ drops the half $F\ge\min$. My check confirms this: $2\max-\min$ satisfies $F\ge\min$ and fails $F\le\max$, and $2\min-\max$ does the reverse.
- **Limits, drop-(CA) monotonicity.** The identity $\min(x)+\min\{\max(x)-\min(x),1\}=\min\{\max(x),\min(x)+1\}$ holds because $\min(x)+\min\{d,1\}=\min\{\min(x)+d,\min(x)+1\}$. A minimum of two monotone functions is monotone, so the "crossing" gap the proposer admitted closes.
- **Direct, "(M) used here and only here".** The claim is true, because both uses of (M) (monotonicity of $g$ and $0\le a\le1$) sit in Step 2. It should still name both uses.
- **Direct, Hamel remark.** If $x,y$ are comonotone, then $\max(x+y)-\min(x+y)=(\max x-\min x)+(\max y-\min y)$ and $\min(x+y)=\min x+\min y$. So $\min+g(\max-\min)$ with $g$ additive satisfies (C), (CA) and (LI). The claim is correct.

## 2. Ranking

| Criterion | direct | limits |
|---|---|---|
| Correctness of stated claim | correct, complete | correct; two garbled witness bullets; one step sketched (now closed) |
| Author's constraints (axioms on $F$; short) | respected; short | respected; long (three equivalent conditions, a weakening, six witnesses) |
| Degenerate cases (ties, orderings, Cauchy, $a\in\{0,1\}$) | all four, explicitly | all four, explicitly |
| Scope | iff + uniqueness + independence + no-(LI) remark | iff + uniqueness + independence + internality + $F(1,1)=1$ weakening |
| Elegance | ray-by-ray, uses (C) for the decomposition | uses (CA) for the decomposition; internality gives monotonicity of $g$ for free |
| Adversarial verdict | survives | survives with repairs |
| **Rank** | **1** | **2** |

*direct* wins on correctness of presentation and on the brevity the author asked for. *limits* adds two ideas worth keeping, and they go into a remark: the stronger (CA)-witness, and the observation that (C)+(M) can be traded for internality or for $F(1,1)=1$.

## 3. Synthesized result

**Theorem.** Let $F:\mathbb{R}^2\to\mathbb{R}$. Then $F$ satisfies (C), (CA), (M) and (LI) if and only if there is $a\in[0,1]$ such that
$$F(x)=a\max(x)+(1-a)\min(x)\qquad\text{for all }x\in\mathbb{R}^2 .$$
In that case $a=F(1,0)$, so $a$ is unique. None of the four axioms can be dropped. Each of the following satisfies the other three axioms but fails the one named:
- $2\max(x)$ fails (C);
- $\min\{\max(x),\min(x)+1\}$ fails (CA);
- $2\max(x)-\min(x)$ fails (M);
- $x_1$ fails (LI).

**Remark.** The proof below also shows the following.
- (a) Without (LI): (C), (CA) and (M) hold iff $F(x)=\min(x)+a_1(x_1-x_2)^+ +a_2(x_2-x_1)^+$ with $a_1=F(1,0)$, $a_2=F(0,1)$ and $a_1,a_2\in[0,1]$.
- (b) Without (C): (CA), (M) and (LI) hold iff $F=a\max+b\min$ with $a,b\ge 0$. Hence (C) may be replaced by $F(1,1)=1$.
- (c) In the presence of (CA) and (LI), the pair (C)+(M) may be replaced by $\min(x)\le F(x)\le\max(x)$.

*(Items (b) and (c) are optional. Drop them if the author wants the shortest version.)*

**Necessity.** Let $x,y$ be comonotone. Then either $x_1\ge x_2$ and $y_1\ge y_2$, or $x_1\le x_2$ and $y_1\le y_2$; a tie fits both cases. In either case $\max(x+y)=\max x+\max y$ and $\min(x+y)=\min x+\min y$. So $F$, being linear in $(\max,\min)$, satisfies (CA). For (C), $\max$ and $\min$ both commute with adding $c$. For (M), $\max$ and $\min$ are monotone and the weights $a,1-a$ are nonnegative; this is the only use of $a\in[0,1]$. For (LI), $\max$ and $\min$ are symmetric.

**Sufficiency.**
1. Let $x=y=0$, which are comonotone. Then (CA) gives $F(0)=0$, and (C) gives $F(c,c)=c$ (trap 1).
2. Let $g(t)=F(t,0)$ for $t\ge0$. The vectors $(s,0)$ and $(t,0)$ are comonotone, so $g$ is additive. By (M), $g$ is nondecreasing. Additivity gives $g(q)=q\,g(1)$ for rational $q\ge0$. For rationals $p\le t\le q$, monotonicity gives $p\,g(1)\le g(t)\le q\,g(1)$, hence $g(t)=at$ with $a=F(1,0)$. This is trap 3, and both uses of (M) are here. From $(0,0)\le(1,0)\le(1,1)$ and (M), $0\le a\le1$. This is trap 4: the endpoints $a=0$ and $a=1$ are admitted, and they give $\min$ and $\max$.
3. By (LI), $F(0,t)=g(t)$ (trap 2). Without (LI), the same argument gives a second weight $a_2=F(0,1)\in[0,1]$, which yields Remark (a).
4. Write $m=\min(x)$ and $d=\max(x)-\min(x)$. Then $x=(m,m)+(d,0)$ or $x=(m,m)+(0,d)$ (established fact 1). By (C), $F(x)=m+ad=a\max(x)+(1-a)\min(x)$. When $d=0$ this reduces to step 1.

*Remark (b).* $c\mapsto F(c,c)$ is additive on $\mathbb{R}$ (constants are comonotone) and monotone, so it equals $kc$ with $k=F(1,1)\ge0$. Then, using (CA) and fact 2, $F(x)=km+ad$ with $0\le a\le k$; this is $a\max+(k-a)\min$. *Remark (c).* Internality gives $0\le g(t)\le t$. Hence $g$ is nondecreasing, $a\in[0,1]$, and $F(c,c)=c$.

There are no unproved steps in the theorem or in the remarks. The only `GAP` is the *existence* of a non-linear additive $g$ in §4. It is not used by the theorem.

## 4. Impossibility results

1. **No three of the four axioms suffice.** The witnesses are listed in the Theorem. The (CA)-witness $\min\{\max,\min+1\}$ has $F(0)=0$, so (CA) does work beyond normalizing $F(0)$. The direct proposal's witness $5+\min$ fails (CA) only through $F(0)\neq0$.
2. **Without (LI)** the solution set is the 2-parameter family of Remark (a). An example is $\min+\tfrac14(x_1-x_2)^+ +\tfrac34(x_2-x_1)^+$, which is not law invariant. The two orderings carry independent weights.
3. **Without (C)** the solution set is the cone $\{a\max+b\min:\ a,b\ge0\}$, for example $3\max+\min$ or $0$. (C) only normalizes $a+b=1$.
4. **Without (M)**, (C)+(CA)+(LI) give exactly $F=\min+g(\max-\min)$ with $g$ additive on $[0,\infty)$. This includes linear slopes outside $[0,1]$, such as $2\max-\min$ and $2\min-\max$. `GAP` (cited, not proved): it also includes non-linear $g$ built from a Hamel basis, which requires the axiom of choice. Monotonicity of $F$ along the ray $(t,0)$ alone is enough to exclude these solutions.
5. **Internality cannot be halved.** With (CA)+(LI), the half $F\ge\min$ alone admits $2\max-\min$, and the half $F\le\max$ alone admits $2\min-\max$.

## 5. Independent check

Script: `<scratch>/judge/judge_check.py`
Output: `<scratch>/judge/judge_check.out`

The script uses exact `Fraction` arithmetic and no libraries. It has two parts.

**Part A (finite-model solve; this is the part that differs from the panel's checks).** The unknowns are the values $F(x)$ for $x\in\{-2,\dots,2\}^2$, which gives 25 unknowns. Every instance of the axioms whose points lie in the grid is imposed as an exact linear equation, and the system is solved by Gauss–Jordan elimination. (M) and (I) are then imposed as inequalities on the free parameters, and the feasible set is compared exactly with the claimed polytope: every inequality holds at the polytope's vertices, and every facet inequality occurs.

| Axioms imposed | Solution dimension | General solution on grid | After inequalities |
|---|---|---|---|
| (C)+(CA)+(LI) | 1 | $\min+a(\max-\min)$, $a=F(1,0)$ | (M): $a\in[0,1]$ exactly (12 distinct ineqs); (I): same |
| (C)+(CA) | 2 | $\min+a_1(x_1-x_2)^++a_2(x_2-x_1)^+$ | (M): $[0,1]^2$ exactly (42 ineqs) |
| (CA)+(LI) | 2 | $F(1,1)\min+F(1,0)(\max-\min)$ | (M): $0\le F(1,0)\le F(1,1)$ exactly; (I): $F(1,1)=1$, $F(1,0)\in[0,1]$ |

This confirms the theorem and Remarks (a), (b) and (c) on the finite model, as solution sets rather than as membership tests. On a grid the Cauchy pathology cannot appear, so Part A does not test trap 3; the analytic argument covers it.

**Part B (witnesses).** The grid is $\{-3,-\tfrac52,\dots,3\}\cup\{\tfrac13,-\tfrac73,\tfrac57\}$ squared, which is 256 points and includes ties, both orderings and non-integers. Shifts are $c\in\{-2,-\tfrac32,\dots,2,\tfrac13\}$. The script evaluated 99,840 instances of (C), 1,432,704 comonotone pairs for (CA), 721,344 ordered pairs for (M) and 9,984 instances of (LI).
- $T(0)=\min$, $T(1)=\max$, $T(\tfrac12)$ and $T(\tfrac27)$ pass all four axioms and lie in the class.
- $T(-1)$ and $T(2)=2\max-\min$ fail only (M).
- $2\max$, $0$ and $3\max+\min$ fail only (C).
- $5+\min$ and $\min\{\max,\min+1\}$ fail only (CA).
- $2\min-\max$ fails only (M).
- $x_1$ and the $(\tfrac14,\tfrac34)$ two-weight functional fail only (LI).

The identity for the (CA)-witness holds on the grid. Over $a_1,a_2\in\{-1,0,\tfrac13,1,\tfrac32\}$, the two-weight family satisfies (C) and (CA) always, (M) iff $a_1,a_2\in[0,1]$, and (LI) iff $a_1=a_2$; all 25 cases agree with this.

## 6. Risks and formalization

- **Risks.** I see no mathematical risk in the theorem. The remaining risks are presentational:
  - If the limits text is reused, its two garbled bullets must be fixed (see §1).
  - The direct proposal uses $e_i$ in a gap note. That notation is not in §6 of the context; write $(s,0)$ and $(0,s)$ instead.
  - Using $5+\min$ as the only (CA)-witness understates the role of (CA).
- **Draft text.** This is a toy panel and no section of the manuscript is affected. If it is typeset, use §3 verbatim.
- **Formalization (Lean).**
  - The one non-trivial lemma is that a monotone additive $g:[0,\infty)\to\mathbb{R}$ is linear (the rational sandwich). Formalize it as a standalone lemma. Mathlib may already have a monotone-additive-implies-linear result that can be reused; I did not verify the exact name.
  - The rest is case analysis on $x_1\le x_2$: $\max$ and $\min$ under comonotone sums, and the decomposition $x=(m,m)+(d,0)$ or $(m,m)+(0,d)$.
  - The independence witnesses are concrete evaluations, for example $F(2,0)\ne 2F(1,0)$ for $\min\{\max,\min+1\}$, and $F(-1,0)>F(0,0)$ for $2\max-\min$.
  - The Hamel statement in §4.4 should *not* be formalized as part of this result. It is a side remark that depends on choice.

Report file: <scratch>/judge_report.md