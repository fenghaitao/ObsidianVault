---
title: "Sum-Product Theorem"
type: concept
tags: [mathematics, combinatorics, randomness]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

The sum-product theorem states that, for a finite set of numbers, sums and products grow the set in complementary ways: if one fails to expand it, the other must.

## Key Information

- Suggested by Erdős and first solved by Erdős and Szemerédi, then refined (in the form needed for extraction) using later work.
- Adding all pairs can fail to grow a set (an interval of integers only roughly doubles), and multiplying all pairs can fail (a geometric progression only roughly doubles) — but sums and products are "orthogonal," so at least one always grows it significantly.
- Used in multi-source randomness extraction: treat weak-source outputs as numbers and combine them via sums and products, which guarantees the number of distinct values (the entropy) increases.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Randomness Extraction]] — where the theorem is applied
