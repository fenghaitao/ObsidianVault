---
title: "One-Way Functions"
type: concept
tags: [cryptography, complexity-theory, hardness]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

A one-way function is a function that is easy to compute but believed hard to invert — multiplying two primes is easy, but factoring the product back is (believed) hard.

## Key Information

- The foundation of modern cryptography: "the whole world is using cryptographic systems which rest on this; all electronic commerce assumes this."
- Commitment schemes are built "very simply" from one-way functions.
- Trapdoor functions — like factoring or discrete log, from which you can build public-key systems — are rare ("we don't know many"); Wigderson contrasts them with physical one-way functions like making an omelette from an egg, which are everywhere in nature.
- Shor's 1994 quantum algorithm broke the two most basic trapdoor functions (factoring and discrete log), forcing cryptography toward new, quantum-resistant assumptions such as lattice problems (e.g., learning with errors), for which no efficient quantum algorithm is known.
- Even a classical polynomial-time factoring algorithm would cause "chaos in the world," since most security systems still rely on it.
- Martin Hellman uses the trapdoor-quiz analogy: a professor gives a one-way function Y = f(X) and asks students to recover X; after "a million years," the professor proves he knew X simply by recomputing f(X) = Y — easy to check, infeasible to invert.
- Diffie-Hellman key exchange uses a commutative one-way function (modular exponentiation over a finite field).
- Hellman notes one-way functions also "figure importantly" in blockchains.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Cryptographic Commitment]] — built from one-way functions
- [[Zero-Knowledge Proofs]] — assumes them
- [[Quantum Computation]] — threatens them
- [[Peter Shor]] — broke factoring/discrete log
- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary (Hellman interview)
- [[Martin Hellman]] — the trapdoor-quiz framing
- [[Public Key Cryptography]] — built on trapdoor one-way functions
- [[Diffie-Hellman Key Exchange]] — uses a commutative one-way function
- [[P vs NP]] — the hardness question behind them
