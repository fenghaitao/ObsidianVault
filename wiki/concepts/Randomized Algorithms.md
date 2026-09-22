---
title: "Randomized Algorithms"
type: concept
tags: [algorithms, randomness, probability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Randomized (or probabilistic) algorithms are algorithms allowed to make random choices — internal coin tosses — which introduce a small probability of error.

## Key Information

- Randomness has been used since antiquity (statisticians, sampling), but became central to algorithm design once computers existed.
- The 1970s primality tests of Miller–Rabin and Solovay–Strassen were fast probabilistic algorithms for testing primality, developed when no efficient deterministic test was known.
- The underlying assumption is always that the random bits are perfect: uniform and independent — which is costly to obtain in reality (thermal noise, internet traffic, quantum photons all have caveats).
- Probabilistic algorithms carry a small probability of error; deterministic algorithms have none, so minimizing error and randomness are both desirable.
- The central complexity-theoretic question: how much randomness do we really need, and can we derandomize? (See pseudorandomness and hardness vs randomness.)

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Pseudorandomness]] — fooling algorithms with less entropy
- [[Hardness vs Randomness]] — derandomization
- [[Primality Testing]] — a canonical application
- [[Complexity Zoo]] — catalog of related classes
- [[Randomness Extraction]] — supplying the bits
