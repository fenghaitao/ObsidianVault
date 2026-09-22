---
title: "Pseudorandomness"
type: concept
tags: [randomness, complexity-theory, cryptography]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Pseudorandomness is the idea that a distribution can appear random to a bounded observer while containing far less true entropy — the observer "cannot tell" it apart from perfect randomness.

## Key Information

- Wigderson's summary phrase: "the quality of randomness is in the eye of the beholder, or in the computational power of the beholder."
- The Blum–Micali coin-toss experiment keeps the coin toss identical across three experiments, upgrading only the observer (human → human + laptop → Cray supercomputer with sensors/cameras); the same event goes from looking full-entropy to fully predictable, so entropy depends on the observer.
- A pseudorandom generator stretches a few truly random bits into many that fool a specific algorithm (or class of observers) for its purpose.
- The Nisan–Wigderson generator starts from a short seed and a hard function, generating many hard-to-distinguish bits; Wigderson's analogy — hardness makes the "first million dollars," then there are methods to make "many more."
- For secrets (passwords), by contrast, Shannon's theorem requires genuine information-theoretic randomness — the entropy must be real regardless of any observer's computational power.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Randomized Algorithms]] — what pseudo-random bits feed
- [[Hardness vs Randomness]] — derandomization from hard functions
- [[Randomness Extraction]] — purifying weak physical sources
- [[Noam Nisan]] — Nisan–Wigderson generator
- [[Manuel Blum]] — Blum–Micali observer view
- [[Claude Shannon]] — true randomness for secrets
- [[Avi Wigderson]] — Nisan–Wigderson generator
- [[Primality Testing]] — structured-randomness example
- [[Silvio Micali]] — Blum–Micali perspective
