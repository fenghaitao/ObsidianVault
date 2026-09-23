---
title: "Halting Problem"
type: concept
tags: [computability, complexity-theory, mathematics]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

The halting problem is the problem of deciding, for an arbitrary program, whether it halts; it is the canonical undecidable (uncomputable) problem.

## Key Information

- Wigderson cites Turing's paper as establishing that "there are problems that are simply unsolvable by computers" — so the first complexity class is the set of solvable/decidable problems, which does not include everything.
- Most complexity-class diagrams implicitly depict decidable problems, with the undecidable ones "in the corner... unreachable."
- MIP* = RE, the quantum interactive proof result, shows uncomputable (halting-type) statements can be verified by an efficient verifier with entangled quantum provers — "things that are uncomputable by any classical [computer] are verifiable in this interactive probabilistic sense."
- Xavier Leroy: computability theory means no algorithm can decide termination for every program, but specific programs of interest can still be proved to terminate (automatic termination analyzers, or hand proofs); all program-verification tasks are essentially undecidable in general, yet useful on the programs you care about.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Alan Turing]] — the undecidability result
- [[Computational Complexity Theory]] — the decidable vs undecidable boundary
- [[Interactive Proofs]] — MIP* = RE
- [[Quantum Computation]] — the quantum proof system
- [[P vs NP]] — the decidable-vs-undecidable boundary
- [[Formal Verification]] — termination proofs despite undecidability
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
