# Lean formalization: Reporting AI-Assisted Proofs in Mathematical Risk Management: A Proposed Standard, with an Axiomatic Characterization of the Loss Ratio as a Case Study

This repository contains a Lean 4 formalization of the loss-ratio-specific results of

> H. Assa, *Reporting AI-Assisted Proofs in Mathematical Risk Management: A Proposed Standard, with an Axiomatic Characterization of the Loss Ratio as a Case Study* (2026).

The loss ratio of a book `X` is `LR(X) = ρ(X)/Π(X)`. The paper shows that the premium `Π` and the loss
measure `ρ` are *implied* by the loss ratio: the implied premium is minus the unique non-finite point of
the cash line `c ↦ LR(X + c)`, and the implied risk measure follows from loss = loss ratio × premium.
The file [`LossRatioLean/Basic.lean`](LossRatioLean/Basic.lean) checks the steps of the argument that are
specific to loss ratios.

## Contents

| Path | What it holds |
|---|---|
| `LossRatioLean/Basic.lean` | The Lean 4 formalization (Mathlib). |
| `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` | Lake project files (Lean and Mathlib `v4.36.0-rc1`). |
| `manuscript/` | LaTeX source of the paper and of its Supplement, `refs.bib`, and the compiled PDFs `loss_ratio_paper_v19.pdf` and `loss_ratio_supplement_v19.pdf`. See `manuscript/BUILD.md`. |
| `ai_process/` | Records behind Section 8 of the paper (the report of the AI process; item 9 of the proposed reporting standard): the literature-panel digest (`digest.md`), the ten candidate formulations (`proposals.md`), one judge report (`judge1.md`), the chair agent's note (`chair_note_final.tex`), and, for the revision with axioms on the loss ratio alone (Section 8.7), the panel's workflow script with its prompts (`revision_pureLR_workflow.js`), the judge's report (`revision_pureLR_judge.md`) and its check script (`revision_pureLR_check.py`). |
| `skill/` | A skill file (`ai-assisted-proof-case-study/SKILL.md`) that packages the method of the case study and the reporting standard for others (Section 2.7 of the paper). |
| `agents/` | Reusable definitions of the agent roles (proposer, adversarial checker, judge, chair, prover, checking run, literature strand, Lean formalizer, second-provider review), a context template, a generic panel workflow, and a worked example (Section 2.7). See `agents/README.md`. |
| `lean_snapshot_2026-10-25/build_log.txt` | Build log of the Lean file exactly as reported in Section 8.6 (build successful, no `sorry`). |

## What is checked

| Result in the paper | Lean name |
|---|---|
| Implied premium: existence, uniqueness, cash additivity (Lemma 7.1) | `prem`, `prem_shift`, `prem_const` |
| Implied risk measure and cash additivity (Lemma 7.2) | `rho`, `rho_cash` |
| Möbius form of cash lines and residue (Proposition 4.7(a)–(c)) | `mobius`, `rho_eq`, `residue` |
| Comonotonic additivity, also on the break-even set (Lemma 7.3) | `comon_additive` |
| Law invariance of the implied pair (Lemma 7.4) | `LI_transfer` |
| Converse construction and uniqueness of the pair | `converse`, `unique_pair` |
| Association (Corollary 10.1(a)) | `association` |
| Pooling at non-finite values (Corollary 10.3) | `pooling_extended` |
| Algebraic core of "no monotone loss ratio" (Proposition 4.14) | `no_monotone_core` |
| Theorem 5.1, given the representation step | `main_conditional` |

Theorem and lemma numbers refer to the version of the paper dated 25 October 2026.

## Scope

* **Abstract setting.** Positions form an additive commutative group with an embedding of the sure
  losses, a comonotonicity relation (constants are comonotone with everything; comonotonicity is preserved
  by cash shifts) and an equality-in-law relation preserved by cash shifts. A loss ratio is a map to
  `Option ℝ`, where `none` is a non-finite value. That `L^∞` with comonotonicity and equality in law is
  an instance of this setting is standard but not formalized.
* **Hypothesis.** `main_conditional` takes the classical representation step (comonotonic additive,
  law-invariant, regular functionals are signed Choquet integrals; Wang, Wei and Willmot 2020) as a
  hypothesis.
* **Not formalized.** The representation step itself, the layer formula, and the examples and
  counterexamples of the paper.

A successful build shows that the formal statements follow from the formal definitions. Whether the
definitions `AxP`, `AxN`, `AxCM`, `AxLI` match the paper should be checked by the reader; they are at the top
of `Basic.lean`. In the current manuscript `AxLI` is an axiom, while `AxP`, `AxN` and `AxCM` are properties that
the manuscript derives from its axioms (P∃) and (R), which refer only to values of the loss ratio; that derivation
(Lemma S1.1 of the Supplement) is not yet formalized.

## Building

Requirements: [elan](https://github.com/leanprover/elan) (the Lean toolchain manager) and git. The
toolchain (`lean-toolchain`) and the exact Mathlib commit (`lake-manifest.json`) are pinned.

```
git clone <this repository>
cd loss_ratio_lean
lake exe cache get    # download precompiled Mathlib
lake build
```

Expected result: `Build completed successfully`, with the axiom report

```
'LossRatio.main_conditional' depends on axioms: [propext, choice, Quot.sound]
```

and the same three standard axioms for the other nine theorems listed at the end of `Basic.lean`.
The file contains no `sorry`. The remaining warnings concern style and renamed library lemmas.

Versions: Lean `v4.36.0-rc1`, Mathlib `v4.36.0-rc1`.

## Building the manuscript

```
cd manuscript
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

## How this was produced

The Lean file was written with AI assistance (Claude, Anthropic) and compiled by the author; the process,
including the build history, is described in Section 12.6 of the paper.

## License

MIT; see [LICENSE](LICENSE).
