---
title: "Space Complexity"
type: concept
tags: [complexity-theory, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Space complexity classifies problems by the amount of memory/space used during a computation.

## Key Information

- Time-space tradeoff: space is at most time (you never visit more cells than steps), so saving space usually blows up time, and vice versa — but the exact relationship is profound.
- A ~50-year-old bound improved by Ryan Williams (2025): any time-t computation can now be simulated in √t space (building on an earlier result of James Cook and Ian Mertz), far less than the old t/log t bound.
- Barrington's theorem shows majority (counting zeros vs ones) is computable in constant space with random access — surprising, since representing n seems to need log n bits.
- Barrington's trick uses non-commutative algebra: encode input bits as permutations of a 5-element set, where commutators (rotate, flip, rotate back, flip back) simulate AND gates; the "hang a painting on two nails" riddle captures it. Unlike Williams's result, this one is efficient (quadratic time) and is used in cryptography.
- The deeper lesson: information can be "encoded in the sequence of operations," letting you do in small space things you thought impossible.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Time Complexity]] — the traded-off resource
- [[David Barrington]] — constant-space majority
- [[Ryan Williams]] — the √t space bound
- [[Computational Complexity Theory]] — the field
