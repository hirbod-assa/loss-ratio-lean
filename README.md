# Lean formalization: An Axiomatic Characterization of the Loss Ratio

This repository contains a Lean 4 formalization of the loss-ratio-specific results of

> H. Assa, *An Axiomatic Characterization of the Loss Ratio* (2026).

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
| `manuscript/` | LaTeX source of the paper, `refs.bib`, and the compiled PDF `loss_ratio_paper_v18.pdf`. See `manuscript/BUILD.md`. |
| `ai_process/` | Records behind Section 12 ("Use of artificial intelligence"): the literature-panel digest (`digest.md`), the ten candidate formulations (`proposals.md`), one judge report (`judge1.md`) and the chair agent's note (`chair_note_final.tex`). |
| `lean_snapshot_2026-10-25/build_log.txt` | Build log of the Lean file exactly as reported in subsection 12.6 (build successful, no `sorry`). |

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
definitions of the axioms `AxP`, `AxN`, `AxCM`, `AxLI` match the paper should be checked by the reader;
they are at the top of `Basic.lean`.

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
