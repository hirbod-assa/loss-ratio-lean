# Judge's report: a pure-LR replacement for CM

I recommend replacing P, N and CM with two axioms: **P∃** (each cash line has a non-finite point) and **R** (comonotone pooling of zero-premium books). The regularity axioms become **RC_LR / RM_LR**, which only use the predicates "LR is not finite" and "the book is loss-free". With LI unchanged, every axiom is a statement about values of LR. P (uniqueness of the non-finite point), N and CM become theorems. All four panel proposals survived their adversarial checks. My own exact check of the combined system, described in section 5, found no failure.

---

## 1. Ranking

| Rank | Proposal | Pure LR | Correct | Break-even books and h=g | RC/RM tiers | Elegance and economics |
|---|---|---|---|---|---|---|
| **1** | **R**, pooling of zero-premium books (angle "boundary") | yes | yes, checked independently | yes, through the pole clause | yes | One identity; N and uniqueness in P are derived. Reading: underwriting results of comonotone books add. |
| 2 | **CM0**, pooling of unpriced books with cash premiums (angle "cashalgebra") | yes | yes | yes | yes | Keeps the premium-weighted-average reading. Still needs N. Given P∃, R is equivalent to N + CM0 (§2.3). |
| 3 | **M + Z**, Möbius cash lines plus pooling at levels 0 and ∞ (angle "levels") | yes, after the verdict's repair to a finite predicate | yes | yes | yes; I adopt its form of RC/RM | M is a cash-line shape axiom (the old CP in LR form) and Z(ii) is awkward. Its negative result on level-stability is valuable (§3). |
| 4 | **CM_LR**, CM with weights a such that LR(X−a) is not finite (angle "weightfree") | technically yes | yes | yes | yes | Given P it is CM word for word: the weight a is the price point c^∞ under its defining predicate, which is what the author rejected ("even c^∞ … is just a shortcut to Π"). Its entropic counterexample LR° is useful. |

**Why R is ranked above CM_LR.** In R, the condition "LR(X) is not finite" only selects which books the axiom applies to. No number is read off a cash line and then used in arithmetic. In CM_LR, the read-off number a multiplies LR values. That is the role the author objects to.

**Why R is ranked above CM0.** R contains CM0 (take u = s+t) and also yields N and the cash-line law. So the axiom list shrinks from P, N, CM to P∃, R.

---

## 2. The synthesized axiom system

### 2.1 Axioms (LaTeX-ready)

```latex
\begin{axiom}[\ax{P}$_\exists$: a price point on each cash line]\label{ax:Pex}
For every $X\in L^\infty$ there is $c\in\R$ with $\LR(X+c)\notin\R$.
\end{axiom}

\begin{axiom}[\ax{R}: comonotone pooling of zero-premium books]\label{ax:R}
Let $X,Y\in L^\infty$ be comonotone with $\LR(X)\notin\R$ and $\LR(Y)\notin\R$. Then for all
$s,t,u\in\R\setminus\{0\}$ the values $\LR(X+s)$, $\LR(Y+t)$ and $\LR(X+Y+u)$ are real, and
\[
 u\,\bigl(\LR(X+Y+u)-1\bigr)\;=\;s\,\bigl(\LR(X+s)-1\bigr)\;+\;t\,\bigl(\LR(Y+t)-1\bigr).
\]
\end{axiom}

\begin{axiom}[\axLI]  % unchanged
If $X\eqd Y$, then either $\LR(X)=\LR(Y)$ or both values are non-finite.
\end{axiom}
```

For the regularity axioms, call a book $W$ **loss-free** if
$$\LR(W)=0,\quad\text{or}\quad \LR(W)\notin\R\ \text{and}\ \LR(W+1)=1 .$$
In the paper this predicate should be written out inside the axioms rather than named, to meet the "not even as an abbreviation" standard.

```latex
\begin{axiom}[\axRC]\label{ax:RC}
For every $\varepsilon>0$ there is $\delta>0$ such that for all $X,Y$ with $\|X-Y\|_\infty<\delta$ and all
$a,b\in\R$:
(i) if $\LR(X-a)\notin\R$ and $\LR(Y-b)\notin\R$, then $|a-b|<\varepsilon$;
(ii) if each $W\in\{X-a,\,Y-b\}$ satisfies [$\LR(W)=0$, or $\LR(W)\notin\R$ and $\LR(W+1)=1$],
then $|a-b|<\varepsilon$.
\end{axiom}

\begin{axiom}[\axRM]\label{ax:RM}
Let $X\le Y$ a.s.\ and $a,b\in\R$.
(i) If $\LR(X-a)\notin\R$ and $\LR(Y-b)\notin\R$, then $a\le b$.
(ii) If each $W\in\{X-a,\,Y-b\}$ satisfies [$\LR(W)=0$, or $\LR(W)\notin\R$ and $\LR(W+1)=1$], then $a\le b$.
\end{axiom}

% Optional, replaces convention S (only needed for equality on all of L^infty):
\begin{center}\ax{S}$_{\LR}$\quad If $\LR(X)\notin\R$, then $\LR(X)=\star$ if and only if $\LR(X+1)=1$.\end{center}
```

Notes on these regularity axioms:

- **They make sense on their own.** Taking $X=Y$ forces the two shifts in each clause to be unique. So the "at most one zero" clause, $c^0$ and Corollary `cor:zero` are no longer needed in any axiom.
- **They keep the cube example as a witness.** The axioms only ask whether LR is not finite, equal to 0, or equal to 1. Relabelling by $x\mapsto x^3$ preserves all three, so it satisfies RC_LR and RM_LR. Under the alternative form below, which uses $(a+c)\LR(X+c)$, the cube fails regularity (verdicts on CM0 and CM_LR). With the form above, Example `ex:cube` remains a valid witness for the independence of R.
- **Alternative form.** One can instead require $a\le b$ and $(a+c)\LR(X+c)\le(b+c)\LR(Y+c)$ for every $c$ at which both values are real. I recommend against it because of the cube problem just described.

### 2.2 Theorems

- **Theorem A.** The following are equivalent: (i) LR satisfies P∃, R, LI and RC_LR; (ii) there are $(h,g)\in\Hset_1^2$ with $\LR=I_h/I_g$ on $\{I_g\neq0\}$ and $\LR\notin\R$ on $\{I_g=0\}$. Under S_LR, $\LR=[I_h:I_g]$ on all of $L^\infty$.
- **Theorem B.** The same with RM_LR in place of RC_LR, and $h,g$ distortion functions. Under the other axioms, RM_LR implies RC_LR: monotone plus cash additive gives 1-Lipschitz, as in Lemma `cashlip`.
- **Theorem A0.** The same without LI, with the capacity representation of the appendix.
- **Derived results.** These become a proposition:
  - P: the price point is unique;
  - N;
  - CM, which keeps the relative-cost reading as a theorem;
  - unit-slope Möbius cash lines, the old CP;
  - cash and comonotone additivity of Π and ρ.

### 2.3 Proof sketch: sufficiency

Assume P∃ and R. The symbols Π, ρ and r below appear only in the proof, never in an axiom.

**Step 0 (P).** Suppose $\LR(X+c_0)\notin\R$. The book $X+c_0$ is comonotone with itself, so R applied to the pair $(X+c_0,X+c_0)$ gives $\LR(X+c_0+s)\in\R$ for every $s\neq0$. So the non-finite point is unique. Set $\Pi(X):=-c_0$. Then $\Pi(X+c)=\Pi(X)+c$.

**Step 1 (N).** Let $p_0$ be the non-finite point of the cash line of 0. Apply R to the constant pair $(p_0,p_0)$: $\LR(2p_0+u)\in\R$ for all $u\neq0$. Since $\LR(p_0)\notin\R$, this forces $p_0=2p_0$, so $p_0=0$. Now apply R to $(0,0)$ with $s=t=u$, and put $f(u):=u(\LR(u)-1)$. Then $f=2f$, so $f=0$ and $\LR(u)=1$ for $u\neq0$.

**Step 2 (cash-line law and Möbius form).** Let $\LR(W)\notin\R$. Apply R to $(W,0)$; the term in $t$ vanishes by Step 1. So $r(W):=s(\LR(W+s)-1)$ does not depend on $s\neq0$.

For any $X$, put $X_0:=X-\Pi(X)$ and $\rho(X):=\Pi(X)+r(X_0)$. Then for $c\neq-\Pi(X)$,
$$\LR(X+c)=\frac{\rho(X)+c}{\Pi(X)+c}.$$
Also $\rho(c)=\Pi(c)=c$, and ρ is cash additive. This gives Lemmas `premium` and `implied`.

**Step 3 (comonotone additivity on all pairs).** Let $X,Y$ be comonotone. Cash shifts preserve comonotonicity, so $X_0,Y_0$ are comonotone and both have non-finite LR.

- *Premiums add.* R says $\LR(X_0+Y_0+u)\in\R$ for every $u\neq0$. By P∃ the only non-finite point of that cash line is 0. Hence $\Pi(X+Y)=\Pi(X)+\Pi(Y)$.
- *Risk measures add.* The identity in R with $s=t=u$ gives $r(X_0+Y_0)=r(X_0)+r(Y_0)$. Hence $\rho(X+Y)=\rho(X)+\rho(Y)$.

No premium is ever recovered from finite values. So the argument covers every case without a split:

- break-even books ($r=0$);
- mixed pairs (one break-even book, one not);
- $h=g$ (where $r\equiv0$);
- pools whose premiums cancel (pooling is done after moving each book to zero premium).

Lemma `comon(b)` then yields CM. The implied risk measure is identified with ρ here, not earlier: this repairs the circular citation the verdict on R found.

**Step 4 (regularity).** Let $W=X-a$.

- *Unpriced shift.* $\LR(W)\notin\R$ if and only if $a=\Pi(X)$.
- *Loss-free shift.* $W$ is loss-free if and only if $a=\rho(X)$. If $\Pi(W)\neq0$, then $\LR(W)=\rho(W)/\Pi(W)$, which is 0 exactly when $\rho(W)=0$. If $\Pi(W)=0$, then $\LR(W+1)=1+\rho(W)$, which is 1 exactly when $\rho(W)=0$. In both cases this means $a=\rho(X)$.

So RC_LR says that Π and ρ are uniformly continuous, and RM_LR says they are monotone. Lemma `cashlip` keeps its proof, with "by Definition `impliedprem` and Corollary `zero`" replaced by Step 4.

**Step 5 (rest of the proof).** Lemmas `LI`, `cashlip`, `layer`, `bv` and `rep` apply as written, giving $\Pi=I_g$ and $\rho=I_h$. Under S_LR, a book with $\LR(X)\notin\R$ is labelled ⋆ exactly when $r(X)=0$, which is convention S.

- **GAP (Theorem A0).** The panel member checking R reports that `app_proofs.tex` uses only Lemmas `premium`, `implied`, `comon` and `cashlip`. I have not re-read it myself.

**Equivalences.**

- Given P: R ⇔ N + CM.
- Given P∃: R ⇔ N + CM0 ⇔ (C) + CM0. Here (C) is the cash-line law of Step 2, and CM0 is R with $u=s+t$, which reads $\LR(X+Y+s+t)=\dfrac{s\,\LR(X+s)+t\,\LR(Y+t)}{s+t}$, an average weighted by the cash premiums. This averaged form can be printed as a remark under R, so the relative-cost reading stays in the paper.

### 2.4 Proof sketch: necessity

Let $\LR=[I_h:I_g]$. Then $\LR(X)\notin\R$ if and only if $I_g(X)=0$.

- *P∃.* Take $c=-I_g(X)$.
- *R.* Let $I_g(X)=I_g(Y)=0$. Then $I_g(X+s)=s\neq0$, so $s(\LR(X+s)-1)=I_h(X)$. Comonotonic additivity gives $I_g(X+Y)=0$, so $\LR(X+Y+u)$ is real and $u(\LR(X+Y+u)-1)=I_h(X)+I_h(Y)$. Nothing is divided by a premium and the labels are never used.
- *RC_LR, RM_LR.* The unpriced shift is $a=I_g(X)$ and the loss-free shift is $a=I_h(X)$. Then $|I_k(X)-I_k(Y)|\le\TV(k)\,\|X-Y\|$, and $I_k$ is monotone when $k$ is a distortion.
- *S_LR.* When $I_g(X)=0$, $\LR(X+1)=I_h(X)+1$.

### 2.5 Justification paragraph (for the paper)

> A book whose loss ratio is not finite has been transferred together with exactly its premium: it commands no further premium. Adding a sure loss $s$ to it creates a book whose premium is $s$, since sure amounts are priced at face value, and $s(\LR(X+s)-1)$ is that book's underwriting result, claims minus premium, in units of cash. Axiom R says two things. First, the underwriting result does not depend on the sure amount added, since a sure loss carries no underwriting result. Second, the underwriting results of comonotone books, which cannot hedge each other, add up when the books are pooled, and a pool of zero-premium books again commands no premium. This is the accounting identity "premium × (LR − 1) = underwriting result", stated in loss ratios alone. That sure losses are priced at cost (N), and that comonotone pools combine at relative cost (CM), follow from it. The regularity axioms say that the sure amount needed to remove a book's premium, or to remove its loss, depends continuously (RC), respectively monotonically (RM), on the book. This is the Cherny–Madan monotonicity of cash offsets at the levels ∞ and 0.

---

## 3. Impossibility results (what pure-LR axioms cannot do)

1. **Finite values alone cannot work (I1, proved).** Take any property that depends on LR only through its finite part, with poles replaced by 1, and that holds for every $[I_h:I_g]$. Together with P, N, LI and RC/RM it does not imply the representation.
   - *Witness:* $[\Pi':\Pi']$ with $\Pi'=\max(I_{\sqrt{\cdot}},I_{\min(1,1.5p)})$. Every finite value is 1, and P, N, LI, RC_LR and RM_LR all hold (I checked RC_LR/RM_LR myself). But Π′ is not comonotone additive.
   - *Consequence:* the pooling axiom itself must relate the non-finite points of X, Y and X+Y. P locates each pole separately but does not link them. Break-even books and $h=g$ are exactly where this matters.
   - The entropic LR° (angle "weightfree") is a second witness.
   - **GAP:** this is proved in the semantic form. A syntactic, first-order version has not been formalized.
2. **Ordinal pooling axioms are too weak (I2).** The cube relabelling $x\mapsto x^3$ satisfies P∃, N, LI, RC_LR and RM_LR. The pooling axiom must be cardinal.
3. **Level stability at every level, even with Möbius cash lines, is too weak (angle "levels", proved).**
   - *Witness:* $\rho'=\E+(\varepsilon I_k)^+$ with $k=\sin 2\pi p$, and the ratio $\rho'/\E$.
   - *Why level stability misses it:* a mixed pair (one break-even book, one not) never shares a level, so a level condition says nothing about it.
4. **R cannot be split or restricted.**
   - (C) without additivity fails: $[\max:\E]$ is a witness.
   - Additivity at a common shift ($s=t=u$) without (C) fails: $1+(I_h-I_g)/(I_g+I_g^3)$ is a witness.
   - Restricting R to books that are not break-even fails: the witness of item 1 satisfies the restricted axiom vacuously.
5. **P∃ cannot be dropped.** $\LR\equiv1$ satisfies R, LI and RC_LR/RM_LR vacuously.
6. **N cannot be separated from CM0 alone.** $[I_h:\kappa I_g]$ satisfies CM0. R, which contains (C), excludes it.

Nothing else on the author's list turned out to be impossible. Labels (S_LR), regularity and pooling can all be written purely in LR.

---

## 4. Remaining risks and Lean targets

**Risks**

- A referee may call the hypothesis "LR(X) is not finite" a hidden price point. The defence is that it is a value of LR, used only to select books, and that by item 1 of §3 some such clause is unavoidable.
- **GAP (Section 8).** The actuarial variant (non-negative losses, shifts $c\ge0$) is not addressed. R needs the zero-premium books $X-\Pi(X)$, which leave $L^\infty_+$, and axioms A1/A4 there still use $\bar\Pi$.
- Text that must be rewritten:
  - the opening of Section 4 and Table `tab:axioms`;
  - Figure `fig:flow` (P, N and CM become lemmas);
  - remarks `rem:primitive`, `rem:weightfree` and `rem:oldCP`;
  - equation (pool), now a consequence;
  - Example `ex:cube`, which becomes the independence witness for R;
  - the sentence in Section 9 that "P defines the price point, through which CM, RC, RM are formulated".
- New independence table:
  - P∃: $\LR\equiv1$;
  - R: the cube, or $[\max:\E]$;
  - LI: $\E_Q/\E$;
  - RC: the Hamel-basis example;
  - the N row is dropped, or kept as an illustration that R implies N.
  - **GAP:** these witnesses have not been re-checked line by line against RC_LR(ii).
- The numerical checks use 4-point spaces only. The proofs above are general.

**Lean targets.** All of these are elementary algebra over ℝ with a non-finite tag.

- From P∃ and R, derive uniqueness of the pole, N, the cash-line law, the Möbius form, and additivity of Π and ρ (Steps 0–3).
- Given P∃: R ⇔ N + CM ⇔ N + CM0.
- The loss-free predicate holds exactly when $a=\rho(X)$, and RC_LR/RM_LR are equivalent to continuity/monotonicity of Π and ρ.
- Necessity of R, RC_LR, RM_LR and S_LR for $[I_h:I_g]$, given comonotonic additivity.
- The cube satisfies RC_LR/RM_LR but fails R.

---

## 5. Numerical check

I checked the combined system with exact fractions on a 4-point uniform space. The concave $g$ used was the rational $(\tfrac12,\tfrac7{10},\tfrac{87}{100})$ rather than √p, so that arithmetic stays exact.

- **Representations:** $h=1\{p>\tfrac12\}$ with that $g$; $h=g$; and a signed, non-monotone pair.
  - R held on all test pairs, with 0 failures: 300 generic, 75 break-even (non-constant break-even books), 75 mixed and 150 with cancelling premiums.
  - Unpriced shift $=I_g$ and loss-free shift $=I_h$ exactly, break-even books included.
  - RM_LR had 0 violations, and the RC Lipschitz ratio was 1.0.
  - N held and $\LR(0)$ is not finite.
- **Witnesses** (out of 400 test pairs each):

| Witness | Result under R |
|---|---|
| cube | identity fails in 400 |
| $[\Pi':\Pi']$ | pole clause fails in 212, using the targeted shift $u$ |
| $[\max:\E]$ | identity fails in 192 |
| $[I_h:2I_g]$ | fails in 400 |
| $1+(I_h-I_g)/(I_g+I_g^3)$ | fails in 400 |

  For $[\Pi':\Pi']$, the loss-free shift equals Π′, so it does satisfy RC_LR/RM_LR, as item 1 of §3 requires.

Script: `ai_process/revision_pureLR_check.py` (run with `python3 -I`; exact rational arithmetic, no dependencies).