---
title: "Computational Complexity Theory"
type: concept
tags: [complexity-theory, computer-science, theory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

Computational complexity theory classifies computational problems by the amount of resources they require (time, space, communication, randomness, parallelism) and studies how problems relate to each other through efficient reductions.

## Key Information

- Resources beyond time include memory/space, communication (e.g., minimizing what you send a satellite), energy, and parallel time (speeding up with n computers).
- Starting with Turing's paper, the first class is the decidable/solvable problems — and there are natural problems that are not decidable at all.
- The field has a "zoo" of hundreds of complexity classes (cataloged on the Complexity Zoo site), and researchers build a "partial order" of hardness via efficient reductions between problems whose complexity is unknown.
- Wigderson calls it "a major theme in the methodology of complexity theory" to relate problems to each other even when their individual complexity is unknown.
- Theoretical computer science lives in both mathematics (produces theorems and proofs) and computer science (motivated by understanding computation); Wigderson says the field is still "in the embryo stage" of understanding computation.
- The field's core activity is modeling — creating definitions and models (e.g., adversarial models in cryptography, a new definition of randomness) that give rise to surprising, practical theorems.
- Ryan Williams on confidence: complexity theory is "littered with statements" that are easy to phrase but hard to settle; algorithms keep surprising us while lower bounds rarely do, which corrodes confidence in claims like P ≠ NP.
- His contrarian probabilities for exponential-time classes: 45% for EXP ≠ NEXP (he thinks NEXP = EXP more likely than not) and 80% for NEXP = coNEXP. The NEXP = coNEXP argument: a "little birdie" can hand an NEXP machine a compact count of the "yes" inputs, letting it exhaustively guess and rule out all the "no" inputs.
- Fine-grained complexity (Williams's research area) studies exact polynomial-time exponents and can relate problems — such as NP-complete subset sum and polynomial two-sum — that P vs NP theory cannot relate.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[P vs NP]] — central question
- [[NP-Completeness]] — reductions and hardness
- [[Time Complexity]] — a resource
- [[Space Complexity]] — a resource
- [[Complexity Zoo]] — the catalog of classes
- [[Halting Problem]] — undecidability
- [[Alan Turing]] — founded the field
- [[David Barrington]] — constant-space result
- [[Ryan Williams]] — time-space result
- [[Scott Aaronson]] — Complexity Zoo
- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Fine-Grained Complexity]] — subfield
- [[Strong Exponential Time Hypothesis (SETH)]] — hypothesis
- [[Circuit Complexity]] — subarea
- [[Michael Sipser]] — textbook author
