---
title: "Meet-in-the-Middle"
type: concept
tags: [algorithms, technique]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

Meet-in-the-middle is an algorithmic technique that splits a problem into two halves, enumerates the possible answers on each half, and combines them (often via a two-sum step) to beat naive exhaustive search.

## Key Information

- Applied to subset sum: enumerate the 2^(n/2) subset sums of each half, then look for a pair — one sum from each list — that hits the target; this is exactly the two-sum problem.
- The two-sum over the lists is solved by sorting and binary search (or hashing), reducing subset sum from 2ⁿ to about 2^(n/2) time.
- Williams notes this "meet in the middle" approach is commonly used in cryptanalysis.

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Subset Sum]] — canonical use
- [[NP-Completeness]] — speedup of an NP-complete problem
