---
title: "Fine-Grained Complexity"
type: concept
tags: [complexity-theory, algorithms, computer-science]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

Fine-grained complexity studies whether the canonical polynomial-time (and subexponential) running times of well-known algorithms are optimal, by relating problems through reductions that preserve small running-time improvements.

## Key Information

- Where P vs NP is coarse (polynomial vs super-polynomial), fine-grained complexity focuses on exact exponents: can an elegant O(n³) or O(n²) algorithm be improved to n^(3−ε) or n^(2−ε)?
- It builds a theory of "lowering lower bounds" via reductions of the form: if problem B can be improved a little, then problem A can be improved a little — a finer notion of reduction.
- It can relate problems that classical P vs NP reductions cannot: an NP-complete problem (subset sum, naive 2ⁿ) reduces to a polynomial problem (two-sum, naive n²), because the reduction may blow up the instance size (n numbers become about 2^(n/2) numbers).
- Canonical problems include three-sum, subset sum, edit distance, and pattern matching; the running times of their textbook algorithms have "resisted any major improvements in decades."
- Williams frames it as: take the well-known algorithm's starting point, and find small pre-processing tricks (e.g., faster group-level finger searches) that shave the exponent.
- The orthogonal-vectors problem is a central fine-grained target: solving it in near-linear time would improve SAT to roughly √(2ⁿ), radically breaking SETH.

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Ryan Williams]] — leading researcher
- [[Computational Complexity Theory]] — parent field
- [[Time Complexity]] — the resource it studies
- [[Strong Exponential Time Hypothesis (SETH)]] — central hypothesis
- [[Three-Sum Problem]] — canonical problem
- [[Subset Sum]] — canonical problem
- [[NP-Completeness]] — relates NP-complete and polynomial problems
