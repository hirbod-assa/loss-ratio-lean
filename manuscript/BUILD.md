# Building the manuscript

Requires a LaTeX distribution with `pdflatex` and `bibtex` (TeX Live 2023 or later) and the packages
`mathptmx`, `microtype`, `pgfplots`, `tikz`, `natbib`, `hyperref`, `newunicodechar`, `enumitem`, `booktabs`.

```
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

`main.tex` includes `sec1_intro.tex` ... `sec12_collaboration.tex`, `app_proofs.tex`, `declaration.tex`.
`sec12_collaboration.tex` itself includes `fig_panelpic.tex` and `sec13_lean.tex` (subsection 12.6).
`loss_ratio_paper_v18.pdf` is the compiled result of this source.
