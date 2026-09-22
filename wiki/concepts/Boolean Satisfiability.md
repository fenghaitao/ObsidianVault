---
title: "Boolean Satisfiability"
type: concept
tags: [complexity-theory, algorithms, logic]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Definition

Boolean satisfiability (SAT) is the problem of deciding whether a Boolean formula has some assignment of truth values that makes it true; it is the canonical NP-complete problem.

## Key Information

- The first problem proven NP-complete (Cook–Levin); every NP problem reduces to it because computation is local — a machine's time evolution becomes local Boolean constraints about which states are consistent.
- Example reductions: graph coloring reduces to SAT (local constraints on adjacent vertices), and factoring reduces to SAT (multiplying and checking the factors is a simple local algorithm).
- SAT solvers: satisfiability is the one problem theorists optimized hardest, with clever heuristics — choose "pivotal" variable assignments that, like dominoes, force many other values and cut down the search space.
- Verification/testing translates naturally into satisfiability questions of Boolean formulas, with instances that usually have exploitable structure.
- The (strong) conjecture is that SAT requires ~2^(c·n) time — yet solvers work in practice because real formulas have structure and the worst case rarely occurs.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[NP-Completeness]] — SAT is the canonical complete problem
- [[Stephen Cook]] — proved SAT NP-complete
- [[Hardness of Approximation]] — the 7/8 threshold
- [[Johan Håstad]] — the 7/8 + ε hardness
- [[Leonid Levin]] — co-proved SAT NP-complete
