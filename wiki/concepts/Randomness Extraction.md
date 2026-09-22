---
title: "Randomness Extraction"
type: concept
tags: [randomness, complexity-theory, information-theory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Randomness extraction (or purification) is the theory of turning weak — biased or correlated — physical randomness into high-quality random bits usable by algorithms.

## Key Information

- Weak sources are unpredictable-but-not-perfect events: weather, sunspots, stock prices, quantum phenomena — they have biases and correlations, and only partial entropy.
- Model: n bits from a distribution with some entropy k (say √n); you want to "massage" it into usable randomness. You cannot produce one perfectly random string, but you can produce polynomially many blocks each of length ≈ k, guaranteed that 99% of them are truly perfect.
- The practical payoff: run the algorithm on each of the many blocks and take a majority vote — as useful as having one perfect block.
- It's related to, but distinct from, pseudorandomness theory, and formally very intricate.
- Extracting from one weak source is hardest; you can also assume several independent weak sources. The sum-product theorem underpins multi-source extraction — mixing sum and product is what guaranteed growth of the number of distinct values (entropy).

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Pseudorandomness]] — the related (observer-relative) theory
- [[Sum-Product Theorem]] — the multi-source ingredient
- [[Randomized Algorithms]] — the consumers of the randomness
- [[Claude Shannon]] — entropy of secrets
- [[Primality Testing]] — derandomization example
