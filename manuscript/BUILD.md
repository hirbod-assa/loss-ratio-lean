# Building the manuscript

Requires a LaTeX distribution with `pdflatex` and `bibtex` (TeX Live 2023 or later) and the packages
`mathptmx`, `microtype`, `pgfplots`, `tikz`, `natbib`, `hyperref`, `xr-hyper`, `newunicodechar`, `enumitem`,
`booktabs`, `tcolorbox`.

The paper (`main.tex`) and the Supplement (`supplement.tex`) share `preamble.tex` and refer to each other through
`xr-hyper`, so they are built together:

```
pdflatex main.tex && pdflatex supplement.tex
bibtex main && bibtex supplement
pdflatex main.tex && pdflatex supplement.tex
pdflatex main.tex && pdflatex supplement.tex
```

Paper: `sec1_intro`, `sec_standard`, `sec2_literature`, `sec3_setting`, `sec4_axioms`, `sec5_results`,
`sec9_necessity`, `sec12_collaboration` (which includes `fig_panelpic` and `sec13_lean`), `sec11_discussion`,
`declaration`.
Supplement: `sec7_proofs`, `sec6_triviality`, `supp_remarks`, `supp_A0`, `supp_A0_proof`, `sec8_actuarial`,
`supp_act`, `supp_C_proof`, `sec10_consequences`, `supp_lit`, `supp_lean`.
`loss_ratio_paper_v19.pdf` and `loss_ratio_supplement_v19.pdf` are the compiled result.
