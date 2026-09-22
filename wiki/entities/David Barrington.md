---
title: "David Barrington"
type: entity
tags: [person, computer-scientist, complexity-theory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

David Barrington is a computer scientist known for Barrington's theorem, which uses non-commutative algebra to evaluate formulas in constant space.

## Key Information

- Discovered that the majority problem (are there more zeros than ones) can be solved in constant space with random access, surprising even Wigderson, who "just didn't believe it's possible."
- The trick: encode input bits as permutations of a 5-element set ("rotate" for a 1, "flip" for a 0); because permutations don't commute, rotations/flips can simulate general formulas of ANDs, ORs, and NOTs.
- A commutator (rotate, flip, rotate back, flip back) simulates an AND gate; Wigderson relates it to the "hang a painting on two nails" riddle.
- Unlike Ryan Williams's result, Barrington's method is efficient — time only quadratic — so it is actually usable, and is used in cryptography in fundamental ways.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Space Complexity]] — constant-space computation
- [[Computational Complexity Theory]] — the field
