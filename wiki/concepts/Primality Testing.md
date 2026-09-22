---
title: "Primality Testing"
type: concept
tags: [algorithms, number-theory, randomness]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Primality testing is the problem of determining whether a given integer is prime.

## Key Information

- Gauss already asked (in complexity-theoretic terms of his day) for an efficient, "indefatigable-calculator" primality test for large numbers.
- In the 1970s, Miller–Rabin and Solovay–Strassen provided fast probabilistic primality tests, but the deterministic case remained open.
- In the early 2000s, the AKS algorithm (Agrawal–Kayal–Saxena) gave a deterministic test; the path was understanding how randomness is used in the probabilistic analysis, then generating structured pseudo-random bits from very few bits.
- The general lesson: deterministic versions of probabilistic algorithms are often discovered by understanding how the algorithm uses randomness, not by new input randomness.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Randomized Algorithms]] — the probabilistic tests
- [[Randomness Extraction]] — structured vs true randomness
- [[Pseudorandomness]] — structured bit generation
