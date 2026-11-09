# Problem context (toy test of the proof panel)

## 1. Setting
Omega = {w1, w2} with P(w1) = P(w2) = 1/2. A loss is a vector x = (x1, x2) in R^2 (positive = loss). A sure loss is
c = (c, c). x and y are comonotone if (x1 - x2)(y1 - y2) >= 0. A functional is a map F: R^2 -> R.
Write max(x) = max(x1, x2) and min(x) = min(x1, x2).

## 2. Target
Necessary and sufficient conditions characterizing functionals of the form F(x) = a max(x) + (1 - a) min(x) with a
in [0, 1]. Candidate axioms: (C) cash additivity F(x + c) = F(x) + c; (CA) comonotonic additivity
F(x + y) = F(x) + F(y) for comonotone x, y; (M) monotonicity x <= y componentwise implies F(x) <= F(y);
(LI) law invariance F(x1, x2) = F(x2, x1). Find the exact iff statement and prove it.

## 3. Established facts (do not rediscover)
1. Every vector x is the sum of the sure loss min(x) and a nonnegative vector with a zero coordinate.
2. Vectors with the same ordering of coordinates are comonotone; any vector is comonotone with any constant.

## 4. Traps and degenerate cases
1. x1 = x2 (constants).
2. Vectors with x1 > x2 versus x1 < x2: without (LI) the two orderings can carry different weights.
3. Additive functionals on R without monotonicity need not be linear (Cauchy equation); check where monotonicity or
   continuity is used.
4. The weight a at the boundary values 0 and 1.

## 5. Constraints set by the author
Axioms must be stated on F only. Keep it short: this is a test of the agents, not a research problem.

## 6. Notation
As above. Do not change it.

## 7. Files and permissions
Scratch scripts go under the scratch folder named in your task. Never edit files elsewhere, never commit.

## 8. Deliverable
As specified in your agent instructions.
