---
title: "Zero-Knowledge Proofs"
type: concept
tags: [cryptography, proof-systems, privacy]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

A zero-knowledge proof is an interactive proof in which the verifier learns nothing beyond the fact that the statement is true — not the proof itself.

## Key Information

- Sounds "totally ridiculous" — convincing someone of something while teaching them nothing new — but is universal: the GMW result (Goldreich–Micali–Wigderson) shows anything that has a mathematical proof also has a zero-knowledge interactive proof, assuming one-way functions.
- Built on commitment schemes: a prover commits to a value so the verifier can't see it (hiding) but the prover can't change it (binding).
- The 3-coloring protocol: the prover commits a coloring on every vertex; the verifier randomly picks an edge and asks to open the two endpoints, checking they are legal and distinct. Repeat many times; cheating is caught with probability 1/|E| per round so error drops exponentially (but never reaches exactly 0 — you can only be exponentially sure, not 100%).
- The zero-knowledge secret: the honest prover randomizes among the 6 color-permutations of a valid coloring, so each revealed pair is just two random distinct colors — the verifier genuinely learns nothing.
- Extended to all provable statements via NP-completeness, because reductions translate witnesses (proofs), not just yes/no answers.
- Wigderson once predicted ZK would never be implemented because the protocol is so costly — "I was wrong": it became central to blockchains and protocol design.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Interactive Proofs]] — the parent model
- [[One-Way Functions]] — the cryptographic assumption
- [[Cryptographic Commitment]] — the building block
- [[NP-Completeness]] — why ZK is universal
- [[Avi Wigderson]] — co-author of the universality result
- [[Silvio Micali]] — co-author
- [[Oded Goldreich]] — co-author
- [[Charles Rackoff]] — co-author of the definition
- [[László Babai]] — parallel originator
- [[Shafi Goldwasser]] — co-author of the definition
