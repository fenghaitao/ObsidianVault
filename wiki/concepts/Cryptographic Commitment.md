---
title: "Cryptographic Commitment"
type: concept
tags: [cryptography, protocols, zero-knowledge]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

A commitment scheme lets a party commit to a secret value such that it is hidden from everyone else, yet the committer cannot later change their mind.

## Key Information

- Two guaranteed properties: hiding (you can't tell what the secret is from the committed value) and binding (the committer is locked in and can only later reveal the value they committed to).
- Built "very simply" from one-way functions; Wigderson's concrete example: the product of two primes commits to its factors, since a number uniquely defines its factorization.
- The essential building block of the three-coloring zero-knowledge protocol: commit each vertex's color, then open two adjacent colors on demand.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[One-Way Functions]] — what commitments are built from
- [[Zero-Knowledge Proofs]] — where commitments are used
