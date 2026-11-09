export const meta = {
  name: 'lr-only-pooling-axiom',
  description: 'Panel: replace axiom CM by a pooling axiom stated only in loss-ratio values; adversarially verify; judge',
  phases: [
    { title: 'Propose', detail: '4 proposers, distinct angles' },
    { title: 'Refute', detail: 'one adversarial checker per proposal' },
    { title: 'Judge', detail: 'rank and synthesize' },
  ],
}

const DRAFT = '<draft>'
const SCRATCH = '<scratch>'

const CONTEXT = `
You are a member of a research panel working on the paper "An Axiomatic Characterization of the Loss Ratio" (author Hirbod Assa).
The working draft is in ${DRAFT} (LaTeX: main.tex, sec3_setting.tex, sec4_axioms.tex, sec5_results.tex, sec7_proofs.tex, sec9_necessity.tex, app_proofs.tex).
Read sec3_setting.tex, sec4_axioms.tex, sec5_results.tex and sec7_proofs.tex first. Files are READ-ONLY for you: do not edit any file in the draft or in ~/Documents, and never run git commit/push. You may write scratch scripts (python3, no sympy installed; plain floats/fractions are fine) under ${SCRATCH}/<your-label>/.

SETTING. LR: L^infty -> R ∪ {∞, ⋆} (atomless space). Cash line phi_X(c)=LR(X+c). Target representation (Theorems A/B): LR = I_h / I_g with signed Choquet integrals I_h, I_g, h,g in H_1 (bounded variation, k(0)=0, k(1)=1); LR non-finite exactly where I_g=0 (⋆ if also I_h=0, else ∞, convention S). Under the representation, Π=I_g and ρ=I_h are comonotonic additive with cash slope 1, so every cash line is the unit-slope Möbius map (ρ+c)/(Π+c).
Current axioms: P (each cash line has exactly one non-finite point), N (LR(c)=1 for constants c≠0), CM (for comonotone X,Y: LR(X+Y)=w_{X,Y}LR(X)+w_{Y,X}LR(Y), w_{X,Y}=Π(X)/(Π(X)+Π(Y)), Π := minus the price point), LI (law invariance), RC/RM (regularity of price point and zero). The proof's core (Lemma comon) shows P+N+CM give comonotone additivity of Π and ρ on ALL comonotone pairs, including break-even books (LR=1, i.e. ρ=Π) and the trivial ratio h=g; then classical representation theory finishes.

THE AUTHOR'S REQUIREMENT. Replace CM by a pooling axiom stated ONLY in terms of values of LR: formulas built from LR evaluated at books such as X, Y, X+Y and cash shifts X+a, Y+b, X+Y+c (a,b,c real), using arithmetic, quantifiers over reals/books, and the predicate "LR(Z) is finite / not finite". FORBIDDEN inside the axiom: Π, ρ, the price point c^∞, the zero c^0, the margin M, any named derived functional or weight, even as an abbreviation. (Saying "LR(X+a) is not finite" is allowed: it is a value of LR.) Ideally the regularity axioms RC/RM can be restated in the same pure-LR style too; that is a secondary goal.

KNOWN FACTS / TRAPS (established, do not rediscover):
1. Relabeling trap: if F is a bijection of the extended reals with F(1)=1, F(∞)=∞ (e.g. F(x)=x^3), then F∘(I_h/I_g) has the same level sets, satisfies P, N, LI and regularity, but is not a ratio of Choquet integrals. So any pooling axiom that only says "level sets are stable under comonotone addition" is too weak; the axiom must pin down the VALUES (e.g. via cash-line shape or a quantitative identity).
2. Break-even books: if LR(X)=1 then LR(X+c)=1 for all c except one point where it is non-finite. Finite values of LR along such a cash line carry no information about the premium; only the location of the non-finite point does. Any formula for the premium from finite values (e.g. Π=c(1-LR(X+c))/(LR(X+c)-LR(X)) or Π=lim c(1-LR(X+c)) / (1-LR(X))) is 0/0 there. For the trivial ratio h=g every finite value is 1. So the axiom must use non-finite values (in pure-LR form) to cover break-even books, or the panel must explain precisely why that is impossible.
3. Pure-LR facts already available under the representation: for X not break-even, c -> 1/(1-LR(X+c)) is a non-constant affine function (with 1/(1-∞):=0); it vanishes at minus the premium and equals 1 at minus the risk measure; its slope is 1/(Π-ρ). Comonotone pooling makes premiums additive and risk measures additive.
4. Pools with cancelling premiums: if X,Y comonotone with Π(X)+Π(Y)=0, LR(X+Y) is non-finite; any identity must allow for this.

DELIVERABLE (be rigorous; mark any step you have not fully proved as GAP):
(a) the proposed axiom(s), stated in pure LR form exactly as they would appear in the paper (LaTeX-ready);
(b) proof that every LR = [I_h : I_g] satisfies them (necessity);
(c) proof that the new axiom together with P, N (and LI, RC/RM as needed; you may replace P, N by pure-LR variants) implies what the existing proof needs — comonotone additivity of Π and ρ (Π := minus the non-finite point of the cash line, ρ := Π·LR extended by cash shifts) on all comonotone pairs, including break-even books and h=g — or directly implies CM;
(d) the economic/actuarial justification in two or three sentences;
(e) a numerical sanity check (script output) on a concrete ratio with non-constant break-even books, e.g. 4-point uniform space, h(p)=1{p>1/2}, g(p)=sqrt(p);
(f) open gaps.
`

const PROPOSAL = {
  type: 'object',
  properties: {
    name: { type: 'string', description: 'short name of the proposed axiom' },
    axiom_latex: { type: 'string', description: 'pure-LR statement, LaTeX-ready' },
    uses_nonfinite_values: { type: 'boolean' },
    replaces: { type: 'string', description: 'which current axioms it replaces (CM only, CM+P, CM+N, ...)' },
    necessity_proof: { type: 'string' },
    sufficiency_proof: { type: 'string', description: 'proof that it yields comonotone additivity of Π and ρ incl. break-even books and h=g, or yields CM' },
    regularity_pure_LR: { type: 'string', description: 'optional pure-LR restatement of RC/RM, or empty' },
    justification: { type: 'string' },
    numerics: { type: 'string', description: 'script path and key output' },
    gaps: { type: 'array', items: { type: 'string' } },
    self_confidence: { type: 'string', enum: ['proved', 'mostly proved', 'sketch', 'speculative'] },
  },
  required: ['name', 'axiom_latex', 'uses_nonfinite_values', 'replaces', 'necessity_proof', 'sufficiency_proof', 'justification', 'numerics', 'gaps', 'self_confidence'],
}

const VERDICT = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    pure_LR: { type: 'boolean', description: 'axiom really mentions only LR values (no Π, ρ, price point, zero, margin, weights)' },
    necessity_ok: { type: 'boolean' },
    sufficiency_ok: { type: 'boolean' },
    counterexample: { type: 'string', description: 'explicit LR satisfying the proposed axioms (+P,N,LI,RC) but not a Choquet ratio, or failing necessity; empty if none found' },
    errors: { type: 'array', items: { type: 'string' } },
    repairs: { type: 'array', items: { type: 'string' }, description: 'concrete fixes that would make it work' },
    overall: { type: 'string', enum: ['survives', 'survives with repairs', 'refuted'] },
    notes: { type: 'string' },
  },
  required: ['name', 'pure_LR', 'necessity_ok', 'sufficiency_ok', 'counterexample', 'errors', 'repairs', 'overall', 'notes'],
}

const ANGLES = [
  { key: 'levels', text: `ANGLE: comonotone level stability plus cash-line shape. Starting idea (test it, do not assume it): (CL) for comonotone X,Y and every β ∈ R∪{non-finite}: if LR(X)=LR(Y)=β then LR(X+Y)=β or LR(X+Y) is not finite; combined with a pure-LR cash-line shape axiom such as "c -> 1/(1-LR(X+c)) is a non-constant affine function, or LR(X+c)=1 for all c but one, where LR is not finite". Note that applying CL to cash-shifted books X+a, Y+b yields additivity of cash offsets at every level, in particular of the non-finite point (premium) and the zero (risk measure). Work out whether break-even books (no zero) and mixed pairs (X break-even, Y not) are covered, whether the shape axiom can be weakened, and whether CL at only the levels 0 and "non-finite" suffices.` },
  { key: 'cashalgebra', text: `ANGLE: a single quantitative pooling identity on cash lines. Look for an identity relating LR(X+a), LR(Y+b), LR(X+Y+a+b) for comonotone X,Y and all reals a,b (e.g. via the affine functions A_X(c)=1/(1-LR(X+c)), a cross-ratio, or a "pole positions add" statement written as an implication between non-finite values), that is necessary under the representation, covers break-even books, and alone (with N, maybe P) forces both cash-line shape and additivity — so that it could replace CM and possibly P at once. Aim for the most elegant single statement.` },
  { key: 'weightfree', text: `ANGLE: eliminate the weight from CM. CM says LR(X+Y) is the premium-weighted average of LR(X) and LR(Y). Express the weight using only LR values (e.g. via two quotes on each cash line, or via the non-finite points written as implications), substitute, and simplify to an identity in LR values only. Then deal with the cases where the weight is not identified by finite values (break-even books, h=g, cancelling premiums). Compare the result with the original CM: is it equivalent given P and N?` },
  { key: 'boundary', text: `ANGLE: limits and minimality. Determine precisely what a pure-LR pooling axiom must contain. Prove or refute: (1) no axiom using only FINITE values of LR can replace CM (use the trivial ratio h=g and the relabeling trap); (2) with non-finite values allowed, find the weakest pure-LR pooling axiom that together with P, N, LI, RC yields the theorem, and check the RM tier (no continuity) separately. Produce your own best proposal in the required format, and in the gaps field list the impossibility results you proved.` },
]

const results = await pipeline(
  ANGLES,
  (a) => agent(`${CONTEXT}\n\n${a.text}\n\nReturn your best single proposal in the structured format.`,
    { label: `propose:${a.key}`, phase: 'Propose', schema: PROPOSAL, effort: 'high' }),
  (p, a) => p && agent(`${CONTEXT}\n\nYou are an ADVERSARIAL CHECKER. Another panel member proposed the following replacement for CM. Try hard to REFUTE it: check that the axiom is truly pure-LR (no hidden Π, ρ, price point, zero, margin, weights), check necessity against LR=[I_h:I_g] including cancelling premiums, ⋆ values and signed premiums, and look for an explicit LR that satisfies the proposed axioms together with P, N, LI and RC but is not a Choquet ratio (try relabelings F∘LR, break-even books, h=g, mixed break-even pairs, non-Möbius cash lines). Verify numerics independently with your own script. If it survives, list exact repairs for any gap.\n\nPROPOSAL:\n${JSON.stringify(p, null, 2)}`,
    { label: `refute:${a.key}`, phase: 'Refute', schema: VERDICT, effort: 'high' })
    .then(v => ({ angle: a.key, proposal: p, verdict: v })),
)

const ok = results.filter(Boolean)
log(`${ok.length}/${ANGLES.length} proposals went through proposal and refutation`)

phase('Judge')
const final = await agent(`${CONTEXT}\n\nYou are the JUDGE of the panel. Below are the proposals and their adversarial verdicts. Do your own checks where verdicts disagree with proposals. Then:
1. Rank the proposals (pure-LR, correctness, covers break-even books and h=g, covers RC and RM tiers, elegance, economic justification).
2. Synthesize the single best replacement for CM (graft repairs and good ideas from runners-up), stated LaTeX-ready, with: the full new axiom list for Theorems A and B (all pure-LR if possible, including RC/RM restated), a complete proof sketch of sufficiency and necessity with every unproved step marked GAP, and the justification paragraph.
3. State clearly any impossibility result: what cannot be done with pure-LR axioms and why.
4. List remaining risks and what should be formalized in Lean.
Write in plain mathematical prose (markdown with LaTeX), as a report to the author.

PANEL RESULTS:
${JSON.stringify(ok, null, 2)}`, { label: 'judge', phase: 'Judge', effort: 'high' })

return { final, results: ok }
