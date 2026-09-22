---
title: "AlphaFold"
type: entity
tags: [product, machine-learning, biology, DeepMind]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

AlphaFold is a DeepMind machine-learning system that predicts protein structures from amino-acid sequences, returning a predicted structure alongside a confidence score.

## Key Information

- Brought up as an example of an NP-hard problem (protein folding) tackled with a heuristic: it doesn't solve 100% of cases, providing a solution plus a confidence score rather than a fully-computed, guaranteed-correct answer.
- It is "an algorithm, a heuristic, that was learned from existing proteins" and works well on unseen but realistic instances.
- Even perfect accuracy on real proteins would not contradict NP-hardness, because it operates on the restricted, structured set of instances found in the body, not worst-case instances.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Protein Folding]] — the NP-hard problem it addresses
- [[NP-Completeness]] — why exact solutions are hard
