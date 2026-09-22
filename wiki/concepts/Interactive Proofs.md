---
title: "Interactive Proofs"
type: concept
tags: [complexity-theory, cryptography, proof-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Interactive proofs are a model in which a prover convinces a randomized verifier of a claim through a randomized conversation, rather than handing over a static written proof.

## Key Information

- Defined in the Goldwasser–Micali–Rackoff paper (which also defined zero-knowledge proofs), and in a parallel paper by Babai from different motivations.
- Generalizes NP: instead of a single message the verifier checks, the prover and randomized verifier interact, allowing a small error probability (which can be reduced arbitrarily — one in a billion or less).
- Generalized to multiple provers, which surprisingly led to the PCP theorem.
- Generalized to quantum provers/verifiers, culminating in MIP* = RE: entangled quantum provers can convince an efficient verifier of uncomputable (halting-type) statements — a 200-page result still in review that resolved long-standing conjectures in mathematics and physics.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Zero-Knowledge Proofs]] — the restricted notion from the same paper
- [[NP-Completeness]] — what interactive proofs generalize
- [[Shafi Goldwasser]] — co-author of the definition
- [[László Babai]] — parallel originator
- [[Quantum Computation]] — quantum proof systems
- [[Halting Problem]] — what MIP* = RE verifies
- [[Charles Rackoff]] — co-author of the definition
- [[Silvio Micali]] — co-author of the definition
