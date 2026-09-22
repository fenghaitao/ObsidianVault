---
title: "Time Complexity"
type: concept
tags: [complexity-theory, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

Time complexity classifies problems by how much time an algorithm needs as a function of the input size.

## Key Information

- P (polynomial time) is the class of problems solvable in time that grows polynomially with data size; linear, quadratic, or cubic time are all "at least theoretically efficient."
- There are many time functions beyond polynomial and exponential — including doubly exponential and beyond.
- Basic tradeoff: if you run in time t you never use more than space t (you only visit so many cells). Ryan Williams's 2025 result shows time-t computations can be simulated in √t space, at the cost of much more time.
- Fine-grained complexity focuses on exact exponents: whether n², n³, or 2ⁿ can be improved by a small epsilon, rather than the coarse P vs NP question.
- The three-sum problem's popular O(n²) bound can actually be improved subquadratically (e.g., n² / ((log n)(log log n))^(2/3)) — one of the canonical fine-grained questions Williams discusses.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[Space Complexity]] — the traded-off resource
- [[Computational Complexity Theory]] — the field
- [[Ryan Williams]] — time-space breakthrough
- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Fine-Grained Complexity]] — studies polynomial-time optimality
- [[Three-Sum Problem]] — subquadratic example
