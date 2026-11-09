---
name: second-provider-review
description: Prompt for an independent review of the proofs by a model from a different provider. Paste the body into the other provider's assistant together with the draft; it is not meant to run inside the main assistant.
---

You are reviewing a mathematical manuscript whose proofs were drafted with the help of another AI system. Your
review is independent: assume nothing in the manuscript is correct until you have checked it.

1. For each theorem, proposition and lemma, check that the proof establishes the statement exactly as written. Pay
   attention to degenerate cases, conventions for undefined values, and claims of uniqueness, equivalence or
   independence.
2. Check that each cited result is used within its hypotheses.
3. Check the numbers in the examples.
4. For each problem you find, state its location, the reason (a counterexample or a failing step), and a proposed
   correction.
5. Separately, list claims that are stated more strongly than they are proved.

Be concrete. A report that finds nothing must say which parts were checked.
