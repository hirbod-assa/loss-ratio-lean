import Mathlib

/-!
# Implied premium and implied risk measure of a loss ratio

Formalization of the loss-ratio specific part of
"An Axiomatic Characterization of the Loss Ratio" (H. Assa, draft of 24 October 2026):
Steps (A) and (B) of Section 6,
i.e. Lemmas 7.1--7.4, Proposition 4.7, the association (Corollary 10.1(a)), extended
pooling (Corollary 10.3), the converse/uniqueness of the representing pair, and the
algebraic core of Proposition 4.14 (no monotone loss ratio).

The classical representation step (Step (C): comonotonic additive functionals are signed
Choquet integrals) is *not* formalized; `main_conditional` states the theorem
conditionally on it.

## Setting
Positions form an additive commutative group `X` with an additive embedding of sure
losses `const : ℝ →+ X`, a comonotonicity relation (constants are comonotone with
everything, shifts by constants preserve comonotonicity) and an equality-in-law relation
preserved by shifts. A loss ratio is a map `LR : X → Option ℝ`; `none` is a non-finite
value. As in the paper, the labels `∞` and `⋆` are not distinguished.
-/

noncomputable section
open Classical

namespace LossRatio

/-- Abstract space of positions. -/
structure Space (X : Type*) [AddCommGroup X] where
  const : ℝ →+ X
  comon : X → X → Prop
  comon_const : ∀ (x : X) (c : ℝ), comon x (const c)
  comon_shift : ∀ {x y : X} (a b : ℝ), comon x y → comon (x + const a) (y + const b)
  eqd : X → X → Prop
  eqd_shift : ∀ {x y : X} (c : ℝ), eqd x y → eqd (x + const c) (y + const c)

variable {X : Type*} [AddCommGroup X]

section Axioms
variable (S : Space X) (LR : X → Option ℝ)

/-- Axiom (P): each cash line has exactly one non-finite point. -/
def AxP : Prop := ∀ x : X, ∃! c : ℝ, LR (x + S.const c) = none

/-- Axiom (N): a sure loss has loss ratio one. -/
def AxN : Prop := ∀ c : ℝ, c ≠ 0 → LR (S.const c) = some 1

/-- Axiom (LI); non-finite values are identified. -/
def AxLI : Prop := ∀ x y : X, S.eqd x y → LR x = LR y

end Axioms

/-- Real part of an extended value. -/
def val (o : Option ℝ) : ℝ := o.getD 0

lemma eq_some_val {o : Option ℝ} (h : o ≠ none) : o = some (val o) := by
  cases o with
  | none => exact absurd rfl h
  | some r => rfl

variable {S : Space X} {LR : X → Option ℝ}

lemma const_add_const (x : X) (a b : ℝ) :
    x + S.const a + S.const b = x + S.const (a + b) := by
  rw [add_assoc, map_add]

/-! ### The implied premium (Definition 4.2, Lemma 7.1) -/

/-- The implied premium: minus the price point. -/
def prem (hP : AxP S LR) (x : X) : ℝ := -Classical.choose (hP x).exists

lemma prem_spec (hP : AxP S LR) (x : X) : LR (x + S.const (-prem hP x)) = none := by
  simp only [prem, neg_neg]
  exact Classical.choose_spec (hP x).exists

lemma prem_unique (hP : AxP S LR) (x : X) {c : ℝ} (hc : LR (x + S.const c) = none) :
    c = -prem hP x :=
  (hP x).unique hc (prem_spec hP x)

/-- Equation (4.1): the implied premium is cash additive. -/
lemma prem_shift (hP : AxP S LR) (x : X) (c : ℝ) :
    prem hP (x + S.const c) = prem hP x + c := by
  have h : LR (x + S.const c + S.const (-prem hP x - c)) = none := by
    rw [const_add_const]
    have e : c + (-prem hP x - c) = -prem hP x := by ring
    rw [e]
    exact prem_spec hP x
  have := prem_unique hP (x + S.const c) h
  linarith

/-- The finite domain is `{Π ≠ 0}`. -/
lemma finite_iff (hP : AxP S LR) (x : X) : LR x ≠ none ↔ prem hP x ≠ 0 := by
  constructor
  · intro h hp
    apply h
    have := prem_spec hP x
    rwa [hp, neg_zero, map_zero, add_zero] at this
  · intro hp h
    apply hp
    have h' : LR (x + S.const 0) = none := by rwa [map_zero, add_zero]
    have := prem_unique hP x h'
    linarith

lemma prem_zero (hP : AxP S LR) (hN : AxN S LR) : prem hP (0 : X) = 0 := by
  by_contra hne
  have h := prem_spec hP (0 : X)
  have hne' : -prem hP (0 : X) ≠ 0 := neg_ne_zero.mpr hne
  have h1 := hN _ hne'
  rw [zero_add] at h
  rw [h] at h1
  simp at h1

/-- Under (P) and (N): `Π(c) = c`. -/
lemma prem_const (hP : AxP S LR) (hN : AxN S LR) (c : ℝ) : prem hP (S.const c) = c := by
  have := prem_shift hP (0 : X) c
  rw [zero_add, prem_zero hP hN, zero_add] at this
  exact this

/-! ### The implied risk measure (Definition 4.6, Lemma 7.2, Proposition 4.7) -/

/-- Loss = loss ratio × premium, on the finite domain. -/
def rhoD (hP : AxP S LR) (x : X) : ℝ := prem hP x * val (LR x)

/-- Axiom (CM): premium-weighted comonotone pooling. -/
def AxCM (hP : AxP S LR) : Prop :=
  ∀ x y : X, S.comon x y → LR x ≠ none → LR y ≠ none → prem hP x + prem hP y ≠ 0 →
    LR (x + y) = some ((rhoD hP x + rhoD hP y) / (prem hP x + prem hP y))

section Implied
variable (hP : AxP S LR) (hN : AxN S LR) (hCM : AxCM hP)
include hN hCM

/-- Lemma 7.2, first part: pooling with a sure loss. -/
lemma rhoD_shift (x : X) (hx : LR x ≠ none) (c : ℝ) (hc : prem hP x + c ≠ 0) :
    rhoD hP (x + S.const c) = rhoD hP x + c := by
  by_cases h0 : c = 0
  · subst h0; simp
  · have hconst : LR (S.const c) = some 1 := hN c h0
    have hcd : LR (S.const c) ≠ none := by rw [hconst]; exact Option.some_ne_none 1
    have hpc : prem hP (S.const c) = c := prem_const hP hN c
    have hrc : rhoD hP (S.const c) = c := by simp [rhoD, hpc, hconst, val]
    have key := hCM x (S.const c) (S.comon_const x c) hx hcd (by rw [hpc]; exact hc)
    rw [hpc, hrc] at key
    show prem hP (x + S.const c) * val (LR (x + S.const c)) = rhoD hP x + c
    rw [key, prem_shift hP x c]
    simp only [val, Option.getD_some]
    field_simp

lemma rhoD_shift' (x : X) {c c' : ℝ} (hc : prem hP x + c ≠ 0) (hc' : prem hP x + c' ≠ 0) :
    rhoD hP (x + S.const c') = rhoD hP (x + S.const c) + (c' - c) := by
  have hx' : LR (x + S.const c) ≠ none := by
    rw [finite_iff hP, prem_shift]; exact hc
  have hsum : prem hP (x + S.const c) + (c' - c) ≠ 0 := by
    rw [prem_shift]
    have e : prem hP x + c + (c' - c) = prem hP x + c' := by ring
    rw [e]; exact hc'
  have h := rhoD_shift hP hN hCM (x + S.const c) hx' (c' - c) hsum
  rw [const_add_const] at h
  have e : c + (c' - c) = c' := by ring
  rw [e] at h
  exact h

end Implied

/-- A shift that moves `x` into the finite domain. -/
def shiftPt (hP : AxP S LR) (x : X) : ℝ := if prem hP x = 0 then 1 else 0

lemma shiftPt_ne (hP : AxP S LR) (x : X) : prem hP x + shiftPt hP x ≠ 0 := by
  unfold shiftPt
  split_ifs with h
  · simp [h]
  · simpa using h

/-- The implied risk measure on all positions. -/
def rho (hP : AxP S LR) (x : X) : ℝ :=
  rhoD hP (x + S.const (shiftPt hP x)) - shiftPt hP x

section Implied2
variable (hP : AxP S LR) (hN : AxN S LR) (hCM : AxCM hP)
include hN hCM

/-- Proposition 4.7(b): the accounting reading. -/
lemma rho_eq (x : X) {c : ℝ} (hc : prem hP x + c ≠ 0) :
    rho hP x = rhoD hP (x + S.const c) - c := by
  unfold rho
  rw [rhoD_shift' hP hN hCM x (shiftPt_ne hP x) hc]
  ring

lemma rho_eq_rhoD (x : X) (hx : prem hP x ≠ 0) : rho hP x = rhoD hP x := by
  rw [rho_eq hP hN hCM x (c := 0) (by simpa using hx)]
  simp

/-- The implied risk measure is cash additive. -/
lemma rho_cash (x : X) (c : ℝ) : rho hP (x + S.const c) = rho hP x + c := by
  have hne : prem hP (x + S.const c) + (shiftPt hP x - c) ≠ 0 := by
    rw [prem_shift]
    have e : prem hP x + c + (shiftPt hP x - c) = prem hP x + shiftPt hP x := by ring
    rw [e]; exact shiftPt_ne hP x
  rw [rho_eq hP hN hCM (x + S.const c) hne, const_add_const]
  have e2 : c + (shiftPt hP x - c) = shiftPt hP x := by ring
  rw [e2]
  unfold rho
  ring

/-- Proposition 4.7(a): every cash line is a unit-slope Möbius map. -/
theorem mobius (x : X) (c : ℝ) (hc : prem hP x + c ≠ 0) :
    LR (x + S.const c) = some ((rho hP x + c) / (prem hP x + c)) := by
  have hfin : LR (x + S.const c) ≠ none := by
    rw [finite_iff hP, prem_shift]; exact hc
  rw [eq_some_val hfin]
  congr 1
  have h := rho_eq hP hN hCM x hc
  unfold rhoD at h
  rw [prem_shift] at h
  rw [h]
  field_simp
  ring

/-- Proposition 4.7(c): the residue at the price point. -/
theorem residue (x : X) :
    Filter.Tendsto (fun c => (c + prem hP x) * val (LR (x + S.const c)))
      (nhdsWithin (-prem hP x) {-prem hP x}ᶜ) (nhds (rho hP x - prem hP x)) := by
  have hev : ∀ᶠ c in nhdsWithin (-prem hP x) {-prem hP x}ᶜ,
      (c + prem hP x) * val (LR (x + S.const c)) = rho hP x + c := by
    filter_upwards [self_mem_nhdsWithin] with c hc
    have hc' : prem hP x + c ≠ 0 := by
      intro h; apply hc; simp only [Set.mem_singleton_iff]; linarith
    rw [mobius hP hN hCM x c hc']
    simp only [val, Option.getD_some]
    have : c + prem hP x = prem hP x + c := by ring
    rw [this]
    field_simp
  have hlim : Filter.Tendsto (fun c => rho hP x + c)
      (nhdsWithin (-prem hP x) {-prem hP x}ᶜ) (nhds (rho hP x - prem hP x)) := by
    have : rho hP x - prem hP x = rho hP x + -prem hP x := by ring
    rw [this]
    exact ((continuous_const.add continuous_id).tendsto _).mono_left nhdsWithin_le_nhds
  exact hlim.congr' (hev.mono fun c hc => hc.symm)

/-! ### Lemma 7.3: comonotonic additivity, including on the break-even set -/

theorem comon_additive {x y : X} (hxy : S.comon x y) :
    prem hP (x + y) = prem hP x + prem hP y ∧ rho hP (x + y) = rho hP x + rho hP y := by
  have line : ∀ s : ℝ, prem hP x + prem hP y + s ≠ 0 →
      LR (x + y + S.const s) =
        some ((rho hP x + rho hP y + s) / (prem hP x + prem hP y + s)) := by
    intro s hs
    let u : ℝ := 1 + |prem hP x| + |s + prem hP y|
    have hu1 : prem hP x + u ≠ 0 := by
      have h1 := neg_abs_le (prem hP x)
      have h2 := abs_nonneg (s + prem hP y)
      intro h
      have : prem hP x + u = prem hP x + (1 + |prem hP x| + |s + prem hP y|) := rfl
      linarith
    have hu2 : prem hP y + (s - u) ≠ 0 := by
      have h1 := le_abs_self (s + prem hP y)
      have h2 := abs_nonneg (prem hP x)
      intro h
      have : prem hP y + (s - u) = prem hP y + (s - (1 + |prem hP x| + |s + prem hP y|)) := rfl
      linarith
    have hc := S.comon_shift u (s - u) hxy
    have hx' : LR (x + S.const u) ≠ none := by
      rw [finite_iff hP, prem_shift]; exact hu1
    have hy' : LR (y + S.const (s - u)) ≠ none := by
      rw [finite_iff hP, prem_shift]; exact hu2
    have hsum : prem hP (x + S.const u) + prem hP (y + S.const (s - u)) ≠ 0 := by
      rw [prem_shift, prem_shift]
      have e : prem hP x + u + (prem hP y + (s - u)) = prem hP x + prem hP y + s := by ring
      rw [e]; exact hs
    have key := hCM _ _ hc hx' hy' hsum
    have exy : x + S.const u + (y + S.const (s - u)) = x + y + S.const s := by
      have : S.const s = S.const u + S.const (s - u) := by
        rw [← map_add]; congr 1; ring
      rw [this]; abel
    rw [exy] at key
    rw [key]
    have h1 : rhoD hP (x + S.const u) = rho hP x + u := by
      rw [← rho_eq_rhoD hP hN hCM _ (by rw [prem_shift]; exact hu1), rho_cash hP hN hCM]
    have h2 : rhoD hP (y + S.const (s - u)) = rho hP y + (s - u) := by
      rw [← rho_eq_rhoD hP hN hCM _ (by rw [prem_shift]; exact hu2), rho_cash hP hN hCM]
    rw [h1, h2, prem_shift, prem_shift]
    congr 1
    congr 1 <;> ring
  have hp : prem hP (x + y) = prem hP x + prem hP y := by
    by_contra hne
    have hs : prem hP x + prem hP y + -prem hP (x + y) ≠ 0 := by
      intro h; apply hne; linarith
    have h1 := line _ hs
    rw [prem_spec hP (x + y)] at h1
    simp at h1
  refine ⟨hp, ?_⟩
  set q := prem hP x + prem hP y with hq
  have e1 : q + (1 - q) = 1 := by ring
  have hs1 : prem hP (x + y) + (1 - q) ≠ 0 := by rw [hp, e1]; norm_num
  rw [rho_eq hP hN hCM (x + y) hs1]
  have hl := line (1 - q) (by rw [e1]; norm_num)
  unfold rhoD
  rw [hl, prem_shift, hp, e1]
  simp only [val, Option.getD_some, one_mul, div_one]
  ring

/-! ### Lemma 7.4: law invariance passes to the implied pair -/

theorem LI_transfer (hLI : AxLI S LR) {x y : X} (h : S.eqd x y) :
    prem hP x = prem hP y ∧ rho hP x = rho hP y := by
  have line : ∀ c, LR (x + S.const c) = LR (y + S.const c) :=
    fun c => hLI _ _ (S.eqd_shift c h)
  have hp : prem hP x = prem hP y := by
    have h1 : LR (y + S.const (-prem hP x)) = none := by
      rw [← line]; exact prem_spec hP x
    have := prem_unique hP y h1
    linarith
  refine ⟨hp, ?_⟩
  have hs := shiftPt_ne hP x
  have hs' : prem hP y + shiftPt hP x ≠ 0 := by rw [← hp]; exact hs
  rw [rho_eq hP hN hCM x hs, rho_eq hP hN hCM y hs']
  unfold rhoD
  rw [prem_shift, prem_shift, hp, line]

/-! ### Corollary 10.3: pooling at non-finite values -/

theorem pooling_extended {x y : X} (hxy : S.comon x y) :
    LR (x + y) = if prem hP x + prem hP y = 0 then none
      else some ((rho hP x + rho hP y) / (prem hP x + prem hP y)) := by
  obtain ⟨hp, hr⟩ := comon_additive hP hN hCM hxy
  split_ifs with h
  · by_contra hne
    exact ((finite_iff hP (x + y)).mp hne) (by rw [hp]; exact h)
  · have hm := mobius hP hN hCM (x + y) 0 (by rw [hp]; simpa using h)
    simp only [map_zero, add_zero] at hm
    rw [hm, hp, hr]

/-! ### Corollary 10.1(a): Assa's association -/

theorem association (x : X) (β : ℝ) (hβ : β ≠ 1) :
    (rho hP x - β * prem hP x) / (1 - β) = 0 ↔
      LR x = some β ∨ (prem hP x = 0 ∧ rho hP x = 0) := by
  have h1β : (1 - β) ≠ 0 := sub_ne_zero.mpr (Ne.symm hβ)
  rw [div_eq_zero_iff, or_iff_left h1β, sub_eq_zero]
  by_cases hp : prem hP x = 0
  · have hnone : LR x = none := by
      by_contra h; exact ((finite_iff hP x).mp h) hp
    simp [hp, hnone]
  · have hm := mobius hP hN hCM x 0 (by simpa using hp)
    simp only [map_zero, add_zero] at hm
    rw [hm]
    simp only [Option.some.injEq, hp, false_and, or_false]
    constructor
    · intro h; rw [h]; field_simp
    · intro h; field_simp at h; linarith

end Implied2

/-! ### Converse and uniqueness of the representing pair -/

/-- The extended ratio of two functionals. -/
def ratio (r p : X → ℝ) (x : X) : Option ℝ := if p x = 0 then none else some (r x / p x)

/-- Converse direction (Lemma 7.3(b) and the algebraic part of (ii) ⇒ (i) in Theorem 5.1):
the ratio of a cash-additive, comonotonic additive pair satisfies (P), (N), (CM), and its
implied premium and implied risk measure are the pair itself. -/
theorem converse (r p : X → ℝ)
    (hr : ∀ x c, r (x + S.const c) = r x + c) (hp : ∀ x c, p (x + S.const c) = p x + c)
    (hr0 : r 0 = 0) (hp0 : p 0 = 0)
    (hrc : ∀ x y, S.comon x y → r (x + y) = r x + r y)
    (hpc : ∀ x y, S.comon x y → p (x + y) = p x + p y) :
    ∃ hP : AxP S (ratio r p), (∀ x, prem hP x = p x) ∧ AxN S (ratio r p) ∧ AxCM hP ∧
      ∀ x, rho hP x = r x := by
  have hP : AxP S (ratio r p) := by
    intro x
    have h0 : p (x + S.const (-p x)) = 0 := by rw [hp]; ring
    refine ⟨-p x, ?_, ?_⟩
    · change ratio r p (x + S.const (-p x)) = none
      unfold ratio; rw [if_pos h0]
    · intro c hc
      by_contra hne
      have h' : p (x + S.const c) ≠ 0 := by
        rw [hp]; intro h; exact hne (by linarith)
      simp [ratio, h'] at hc
  have hprem : ∀ x, prem hP x = p x := by
    intro x
    have h0 : p (x + S.const (-p x)) = 0 := by rw [hp]; ring
    have h : ratio r p (x + S.const (-p x)) = none := by unfold ratio; rw [if_pos h0]
    have := prem_unique hP x h
    linarith
  have hpconst : ∀ c, p (S.const c) = c := fun c => by simpa [hp0] using hp 0 c
  have hrconst : ∀ c, r (S.const c) = c := fun c => by simpa [hr0] using hr 0 c
  have hN : AxN S (ratio r p) := by
    intro c hc
    simp [ratio, hpconst, hrconst, hc]
  have hrhoD : ∀ x, p x ≠ 0 → rhoD hP x = r x := by
    intro x hx
    simp only [rhoD, hprem, ratio, if_neg hx, val, Option.getD_some]
    field_simp
  have hCM : AxCM hP := by
    intro x y hxy hx hy hs
    rw [hprem, hprem] at hs
    have hx' : p x ≠ 0 := by rw [← hprem]; exact (finite_iff hP x).mp hx
    have hy' : p y ≠ 0 := by rw [← hprem]; exact (finite_iff hP y).mp hy
    rw [hrhoD x hx', hrhoD y hy', hprem, hprem]
    simp only [ratio, hpc x y hxy, hrc x y hxy, if_neg hs]
  refine ⟨hP, hprem, hN, hCM, ?_⟩
  intro x
  have hs := shiftPt_ne hP x
  unfold rho
  rw [hrhoD _ (by rw [hp, ← hprem]; exact hs), hr]
  ring

/-- Uniqueness: under (P), any cash-additive pair whose ratio is the loss ratio is the
implied pair. -/
theorem unique_pair (hP : AxP S LR) (r p : X → ℝ)
    (hr : ∀ x c, r (x + S.const c) = r x + c) (hp : ∀ x c, p (x + S.const c) = p x + c)
    (hLR : ∀ x, LR x = ratio r p x) :
    (∀ x, prem hP x = p x) ∧ ∀ x, rho hP x = r x := by
  have hprem : ∀ x, prem hP x = p x := by
    intro x
    have h0 : p (x + S.const (-p x)) = 0 := by rw [hp]; ring
    have h : LR (x + S.const (-p x)) = none := by rw [hLR]; unfold ratio; rw [if_pos h0]
    have := prem_unique hP x h
    linarith
  refine ⟨hprem, ?_⟩
  intro x
  have hs := shiftPt_ne hP x
  have hne : p (x + S.const (shiftPt hP x)) ≠ 0 := by rw [hp, ← hprem]; exact hs
  unfold rho rhoD
  rw [hLR (x + S.const (shiftPt hP x)), hprem]
  simp only [ratio, if_neg hne, val, Option.getD_some]
  rw [hr]
  field_simp
  ring

/-! ### Proposition 4.14: the algebraic core of "no monotone loss ratio"

For the Bernoulli book `1_A` with `P(A) = p`, `I_k(1_A + c) = k(p) + c`, and for
`1 + t 1_E` with `P(E) = q`, `I_k(1 + t 1_E) = 1 + t k(q)` (layer formula, not formalized).
Monotonicity of the loss ratio along `1_A ≤ 1_A + 1` and `1 ≤ 1 + 1_E` gives the two
inequalities below, which force `h = g`. -/

lemma le_of_ratio_mono {a b : ℝ} (hb : 0 < b) (h : a / b ≤ (a + 1) / (b + 1)) : a ≤ b := by
  have hb1 : 0 < b + 1 := by linarith
  have key : (a + 1) / (b + 1) - a / b = (b - a) / (b * (b + 1)) := by
    field_simp
    ring
  have hd : 0 < b * (b + 1) := mul_pos hb hb1
  by_contra hlt
  push_neg at hlt
  have : (b - a) / (b * (b + 1)) < 0 := div_neg_of_neg_of_pos (by linarith) hd
  linarith

lemma ge_of_ratio_mono {a b : ℝ} (hb : 0 < 1 + b) (h : 1 ≤ (1 + a) / (1 + b)) : b ≤ a := by
  by_contra hlt
  push_neg at hlt
  have : (1 + a) / (1 + b) < 1 := (div_lt_one hb).mpr (by linarith)
  linarith

theorem no_monotone_core (h g : ℝ → ℝ) (p : ℝ) (hg : 0 < g p)
    (h1 : h p / g p ≤ (h p + 1) / (g p + 1))
    (h2 : 1 ≤ (1 + h p) / (1 + g p)) : h p = g p :=
  le_antisymm (le_of_ratio_mono hg h1) (ge_of_ratio_mono (by linarith) h2)

/-! ### The main theorem, conditional on the classical representation step -/

/-- Theorem 5.1, conditional on Step (C). `Rep F` stands for "F is a signed Choquet integral
`I_k` with `k` of bounded variation and `k(1) = 1`" and `classical` for the theorem of
Wang, Wei and Willmot (2020) (or Schmeidler (1986) in the monotone tier). Regularity is
imposed directly on the implied pair. -/
theorem main_conditional (Regular Rep : (X → ℝ) → Prop)
    (classical : ∀ F : X → ℝ, (∀ x c, F (x + S.const c) = F x + c) →
        (∀ x y, S.comon x y → F (x + y) = F x + F y) → (∀ x y, S.eqd x y → F x = F y) →
        Regular F → Rep F)
    (hP : AxP S LR) (hN : AxN S LR) (hCM : AxCM hP) (hLI : AxLI S LR)
    (hreg : Regular (prem hP) ∧ Regular (rho hP)) :
    Rep (prem hP) ∧ Rep (rho hP) ∧ ∀ x, LR x = ratio (rho hP) (prem hP) x := by
  refine ⟨classical _ (prem_shift hP) (fun x y hxy => (comon_additive hP hN hCM hxy).1)
      (fun x y hxy => (LI_transfer hP hN hCM hLI hxy).1) hreg.1,
    classical _ (rho_cash hP hN hCM) (fun x y hxy => (comon_additive hP hN hCM hxy).2)
      (fun x y hxy => (LI_transfer hP hN hCM hLI hxy).2) hreg.2, ?_⟩
  intro x
  unfold ratio
  split_ifs with h
  · by_contra hne
    exact ((finite_iff hP x).mp hne) h
  · have hm := mobius hP hN hCM x 0 (by simpa using h)
    simpa using hm

end LossRatio

/-! ### Axiom audit: each line should list only `propext`, `Classical.choice`, `Quot.sound`. -/
#print axioms LossRatio.mobius
#print axioms LossRatio.residue
#print axioms LossRatio.comon_additive
#print axioms LossRatio.LI_transfer
#print axioms LossRatio.pooling_extended
#print axioms LossRatio.association
#print axioms LossRatio.converse
#print axioms LossRatio.unique_pair
#print axioms LossRatio.no_monotone_core
#print axioms LossRatio.main_conditional
