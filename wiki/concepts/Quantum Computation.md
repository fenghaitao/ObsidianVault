---
title: "Quantum Computation"
type: concept
tags: [quantum-computing, complexity-theory, cryptography]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Quantum computation is a model of computation in which bits are manipulated in superposition using unitary operations per the rules of quantum mechanics — roughly, "probability theory with negative numbers," where events can cancel via interference.

## Key Information

- Proposed in the 1980s by Feynman and Manin, originally to simulate quantum systems directly.
- A quantum computer is at least as strong as a probabilistic one: you can measure quantum bits to obtain random bits.
- Shor (1994) found efficient quantum algorithms for factoring and discrete log — the two underpinnings of all security systems — setting off billions in investment to build quantum computers and to find quantum-resistant assumptions.
- The central engineering obstacle is noise/decoherence ("everything depends on everything"); holding bits in superposition is extremely hard, and quantum error-correcting codes are part of the fix.
- Prompted post-quantum cryptography: lattice-based problems (e.g., learning with errors) with no known quantum algorithm, pursued with governments like the NSA pushing for quantum-resilient assumptions.
- Transformed proof systems: MIP* = RE shows entangled quantum provers can convince an efficient verifier of uncomputable statements — a ~200-page result (six years in review) with fundamental implications for mathematics and physics (resolving long-standing conjectures).
- Deepened the interaction between computer scientists and physicists, reaching into quantum gravity and black holes.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Peter Shor]] — quantum factoring/discrete log
- [[Richard Feynman]] — proposed the model
- [[Interactive Proofs]] — quantum proof systems
- [[Halting Problem]] — what MIP* = RE verifies
- [[One-Way Functions]] — assumptions it threatens
- [[P vs NP]] — complexity backdrop
- [[Alan Turing]] — the model it generalizes
- [[Avi Wigderson]] — discusses its impact
