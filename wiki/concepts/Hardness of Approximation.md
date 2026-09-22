---
title: "Hardness of Approximation"
type: concept
tags: [complexity-theory, approximation, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Hardness of approximation studies how close to optimal you can get when exact optimization is NP-hard, by characterizing which approximation factors remain hard.

## Key Information

- A natural relaxation when a problem is NP-complete/NP-hard: settle for within a factor of 2, or 10%, of the optimum instead of the exact optimum.
- The PCP theorem (early 1990s) allowed arguing hardness of even approximation, not just exact solutions.
- Håstad's strengthening gives a tight example: with three variables per constraint, guessing at random satisfies 7/8 of the constraints, and the PCP theorem + Håstad shows satisfying 7/8 + ε is already NP-hard — for any ε > 0, "just as hard as finding the optimum."
- This applies to large classes of constraint-optimization problems, showing how precisely theorists can now locate the exact threshold of tractability.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[NP-Completeness]] — the hardness being relaxed
- [[Boolean Satisfiability]] — the constraint problems studied
- [[Johan Håstad]] — the tight inapproximability result
