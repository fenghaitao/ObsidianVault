---
title: "Subset Sum"
type: concept
tags: [algorithms, complexity-theory, np-complete]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

The subset sum problem asks whether some subset of a set of n integers sums to a given target value; it is a canonical NP-complete problem.

## Key Information

- The naive algorithm enumerates all 2ⁿ possible subsets, taking 2ⁿ time.
- Using meet-in-the-middle, it can be solved in about 2^(n/2) time: partition the numbers into two halves, enumerate the 2^(n/2) subset sums of each half, and then solve a two-sum problem over the two lists (sort one and binary-search, or hash).
- Ryan Williams uses this as the central example of how fine-grained complexity relates an NP-complete problem to a polynomial problem (two-sum) — a reduction that classical P vs NP theory cannot make, because the reduction blows up the instance size.

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[NP-Completeness]] — the class it belongs to
- [[Meet-in-the-Middle]] — speedup technique
- [[Fine-Grained Complexity]] — field relating it to polynomial problems
