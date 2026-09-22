---
title: "Hardness vs Randomness"
type: concept
tags: [complexity-theory, randomness, derandomization]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

The hardness vs randomness paradigm is the deep connection between computational hardness and derandomization: if hard functions exist, then randomness can be removed from efficient algorithms.

## Key Information

- Under the assumption that some problem requires exponential-size circuits (a strengthening of P ≠ NP), we get P = BPP — every efficient probabilistic algorithm has an efficient deterministic algorithm.
- The connection is surprising because the hardness assumption says nothing about randomness, yet it resolves whether randomness helps.
- It goes both ways: if you can derandomize certain algorithms, you've found a hard function — a near if-and-only-if, with variants that are exact equivalences.
- Intuitive starting point: to a limited (polynomial-time) observer, a hard problem's answer carries some entropy; amplify that tiny uncertainty until the answer looks like a fair coin toss, then use it as a seed.
- Because hard problems are widely believed to exist, theorists believe randomness in algorithms is weak and removable.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Pseudorandomness]] — the generator at its core
- [[Randomized Algorithms]] — what gets derandomized
- [[Noam Nisan]] — Nisan–Wigderson generator
- [[P vs NP]] — the hardness assumption's cousin
- [[Manuel Blum]] — Blum–Micali observer view
