# Chair's note: two-point Choquet characterization (toy panel)

## 1. Question put to the panel

Setting: Ω = {w1, w2}, each state with probability 1/2. A loss is x = (x1, x2), and F: R² → R. The panel was asked for an exact iff characterization of F(x) = a max(x) + (1−a) min(x) with a ∈ [0,1]. The candidate axioms were (C) cash additivity, (CA) comonotonic additivity, (M) monotonicity and (LI) law invariance. The author's constraints were that axioms are stated on F only and that the result is kept short. The panel had to handle four traps: ties x1 = x2, the two orderings, the Cauchy equation, and the boundary values a ∈ {0, 1}.

## 2. Proposals, ranked

| Rank | Angle | Statement | Why ranked here |
|---|---|---|---|
| 1 | direct | (C)+(CA)+(M)+(LI) ⇔ F = a max + (1−a) min, with a = F(1,0) unique. One independence witness per axiom. A remark gives the two-weight family when (LI) is dropped. | Correct and complete. Short, as the author asked. Handles all four traps explicitly. |
| 2 | limits | Three equivalent conditions: (i) the formula; (ii) the four axioms; (iii) (CA)+(LI)+internality min ≤ F ≤ max. Also the weakening of (C) to F(1,1)=1, six witnesses, and the claim that neither half of internality can be dropped. | Correct. Longer than the author asked. Two witness bullets are garbled and one step is only sketched; all are repaired below. |

The judge recommends the *direct* theorem and proof, with two changes:
- replace its (CA)-witness 5+min, which fails (CA) only because F(0) ≠ 0, with the *limits* witness min{max(x), min(x)+1}, which has F(0) = 0;
- fold the *limits* weakenings into an optional remark.

Both adversarial verdicts and the judge agree on the mathematics. Agreement among agents is not proof. The evidence is as follows:
- Each verdict re-derived the hand proofs independently.
- Three separate exact-arithmetic scripts confirm all finite claims:
  - `<scratch>/adv_direct/chk.py`
  - `<scratch>/adv_limits/chk.py`
  - `<scratch>/judge/judge_check.py`
- The judge's Part A solves the linear system on a 5×5 grid. It confirms the solution sets, not just membership tests.
- No grid check can test trap 3 (Cauchy). That part rests on the rational-sandwich argument alone.

I checked the judge's output file. It matches the report:
- the (C)+(CA)+(LI) solution space has dimension 1, and the feasible set under (M) is exactly [0,1];
- every witness fails exactly the axiom it is meant to fail.

## 3. What survived, and the error log

**Survived.** The synthesized theorem in §3 of the judge report survives, with its proof and its Remarks (a)–(c). The four independence witnesses are:
- 2max fails (C);
- min{max, min+1} fails (CA);
- 2max − min fails (M);
- x1 fails (LI).

**Errors found.** These are reproduced verbatim for the error log.

*direct* had no errors (verdict: "survives"). Its verdict listed two optional repairs:
- "Optional wording fix: Step 2 says (M) is used 'here, and only here', but (M) is also used for the bounds 0 <= a <= 1. Both uses are in Step 2, so the claim holds, but naming both uses would be clearer."
- "Optional: the e_i notation in the third gap is not in the context's notation section. Write it as (s,0),(t,0) and (0,s),(0,t) to keep the notation fixed."

*direct* also self-reported a script error: "A first run printed a spurious "mismatch". The cause was a Python chained-comparison bug in the test line, not a counterexample. After fixing it, everything passed."

*limits* (verdict: "survives with repairs"). The errors, verbatim:
1. "No mathematical error found. Each step of (i)=>(ii), (ii)=>(iii), (iii)=>(i), the uniqueness a=F(1,0), the weakening of (C) to F(1,1)=1, and all six independence examples were checked by hand and in exact arithmetic."
2. "Presentation (drop-M bullet): the text contains a false start, '(M) fails: (0,0)<=(0,1) but F(0,1)=2... check the other way'. F(0,1)=2>=F(0,0)=0 agrees with (M), so the first pair is not a violation. Only the second pair (-1,0)<=(0,0) with F(-1,0)=1>0=F(0,0) is one. As written, a reader could take the first pair as the witness."
3. "Presentation ((iii) bullet): 'drop the upper half of (I): 2min-max satisfies (CA),(LI), F>=... no: it satisfies F<=max but fails F>=min' is garbled and attaches the wrong example to the label. Dropping the upper half is witnessed by 2max-min, which satisfies F>=min and fails F<=max. Dropping the lower half is witnessed by 2min-max."
4. "Presentation (drop-CA monotonicity): the argument is piecewise, and the proposer admits the crossing case is only sketched. It is correct, but it is not a complete proof as written."
5. "Constraint tension, minor: the author asked for a short result. The statement bundles a third equivalent condition (iii), a weakening of (C), and two independence results. None of this is wrong or forbidden, and all axioms are stated on F only, but it goes beyond 'keep it short'."

**Repairs.**
- Error 2: keep only the pair (−1,0) ≤ (0,0).
- Error 3: swap the labels.
- Error 4: use the identity min(x) + min{max(x)−min(x), 1} = min{max(x), min(x)+1}. This is a minimum of two monotone maps, so the crossing case disappears. The judge confirmed the identity analytically and on the grid.
- Error 5: move (iii) and the weakenings into a remark.

The judge added two presentational points:
- 5+min as the only (CA)-witness understates what (CA) does;
- the e_i notation must not be used.

## 4. Open gaps and impossibility results

**GAP.** The existence of a non-linear additive g on [0,∞) needs a Hamel basis, and therefore the axiom of choice. It is asserted and cited, but not proved, and no reference was supplied. The theorem does not use it.

**Unverified side claims.** These are not GAPs in the theorem:
- *direct* observes that the theorem should still hold if (CA) is required only for pairs on the same ray, plus F(0)=0. *limits* raises the same idea and declines to state it. No one proved it as a theorem.
- The judge suggests that Mathlib may already have a "monotone additive implies linear" lemma. The judge did not verify its name.

**Impossibility results.** All were checked analytically and on grids.
1. No three of the four axioms suffice; the four witnesses above show this.
2. Without (LI), the solutions form a two-parameter family: min + a1(x1−x2)⁺ + a2(x2−x1)⁺ with a1, a2 ∈ [0,1].
3. Without (C), the solutions form the cone {a max + b min : a, b ≥ 0}.
4. Without (M), the solutions are F = min + g(max−min) with g additive. This family includes slopes outside [0,1], such as 2max−min and 2min−max, and also the Hamel solutions (this is the GAP).
5. Given (CA)+(LI), neither half of internality is enough on its own.

## 5. Decisions for the author

1. **Form of the statement.**
   - (A) The *direct* iff with four axioms. It is short, as you asked. This is the judge's recommendation.
   - (B) The *limits* three-way equivalence. It is more informative but longer, and it requires repairs 2–4 above.
2. **(CA) witness.**
   - Use min{max, min+1}. It shows that (CA) does more than normalize F(0). This is the recommended choice.
   - Or keep 5+min. It is simpler, but (CA) then looks like a mere normalization.
   - Or give both, at the cost of one more line.
3. **Remark (a)**, the case without (LI). Keep it: it costs one line and makes trap 2 visible. Or drop it, for the shortest version.
4. **Remarks (b) and (c)**, the weakenings F(1,1)=1 and internality. The judge marks them optional. Including them adds about four lines. Omitting them loses the observation that (C)+(M) can be replaced by internality.
5. **Hamel GAP.**
   - Supply a citation and keep the sentence about non-linear solutions.
   - Or delete the sentence. The independence of (M) is already shown by 2max−min, which does not use choice. Deleting removes the only GAP.
6. **Formalization.** If you formalize this in Lean:
   - prove monotone additive ⇒ linear as a standalone lemma, or locate the Mathlib lemma, whose name is unverified;
   - leave the Hamel remark out of scope.
   
   Otherwise, record that the result is checked by hand and on finite grids only.
7. **Use.** This is a toy panel and no section of the manuscript is affected. Decide whether to typeset §3 of the judge report, or to keep it only as a test of the agents.

Judge report: `<scratch>/judge_report.md`