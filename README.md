# An Axiomatic Characterization of the Loss Ratio — Lean formalization

Companion repository for the paper *An Axiomatic Characterization of the Loss Ratio*
(Hirbod Assa, working version v18, 25 October 2026).

## Contents

| Path | What it holds |
|---|---|
| `LossRatioLean/Basic.lean` | The Lean 4 formalization (Mathlib). |
| `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` | Lake project files (Lean and Mathlib `v4.36.0-rc1`). |
| `manuscript/` | LaTeX source of the paper, `refs.bib`, and the compiled PDF `loss_ratio_paper_v18.pdf`. See `manuscript/BUILD.md`. |
| `ai_process/` | Records behind Section 12 ("Use of artificial intelligence"): the literature-panel digest (`digest.md`), the ten candidate formulations (`proposals.md`), one judge report (`judge1.md`) and the chair agent's note (`chair_note_final.tex`). |
| `lean_snapshot_2026-10-25/build_log.txt` | Build log of the Lean file exactly as reported in subsection 12.6 (build successful, no `sorry`). |

## What is formalized

The loss-ratio-specific part of the paper: Steps (A) and (B) of Section 6, i.e. Lemmas 7.1–7.4,
Proposition 4.7, the association (Corollary 10.1(a)), extended pooling (Corollary 10.3), the
converse and uniqueness of the representing pair, and the algebraic core of Proposition 4.14
(no monotone loss ratio). Axioms (P), (N), (CM) and (LI) are `AxP`, `AxN`, `AxCM` and `AxLI`.

The classical representation step (Step (C): comonotonic additive functionals are signed Choquet
integrals) is **not** formalized; `main_conditional` states the main theorem conditionally on it.
`main_conditional` depends only on the standard axioms `propext`, `choice` and `Quot.sound`.

## Building

```
lake exe cache get
lake build
```

## Building the manuscript

```
cd manuscript
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```
