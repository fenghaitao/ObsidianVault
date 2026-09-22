---
title: "Protein Folding"
type: concept
tags: [biology, algorithms, np-hard, machine-learning]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Protein folding is the problem of predicting a protein's three-dimensional structure from its amino-acid sequence; formulated as energy minimization under constraints, it is NP-hard.

## Key Information

- The optimization version (minimize energy subject to chemical constraints) is easily provable NP-hard.
- Yet the body folds proteins "extremely efficiently" — Wigderson's explanation is evolution designed a small, restricted set of proteins (not exponentially many) that are naturally prone to efficient energy minimization.
- It illustrates the key point that real-world instances are not worst-case instances: the inputs that arise have structure that makes efficient or heuristic methods work.
- AlphaFold tackles it with a learned heuristic that returns a structure plus a confidence score; it is not 100% accurate on all cases, but succeeds on realistic inputs.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[AlphaFold]] — the heuristic that tackles it
- [[NP-Completeness]] — the hardness of the optimization form
