---
title: "Boolean Satisfiability"
type: concept
tags: [complexity-theory, algorithms, logic]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Boolean satisfiability (SAT) is the problem of deciding whether a Boolean formula has some assignment of truth values that makes it true; it is the canonical NP-complete problem.

## Key Information

- The first problem proven NP-complete (Cook–Levin); every NP problem reduces to it because computation is local — a machine's time evolution becomes local Boolean constraints about which states are consistent.
- Example reductions: graph coloring reduces to SAT (local constraints on adjacent vertices), and factoring reduces to SAT (multiplying and checking the factors is a simple local algorithm).
- SAT solvers: satisfiability is the one problem theorists optimized hardest, with clever heuristics — choose "pivotal" variable assignments that, like dominoes, force many other values and cut down the search space.
- Verification/testing translates naturally into satisfiability questions of Boolean formulas, with instances that usually have exploitable structure.
- The (strong) conjecture is that SAT requires ~2^(c·n) time — yet solvers work in practice because real formulas have structure and the worst case rarely occurs.
- Ryan Williams details SAT's representations: CNF/DIMACS (each line a clause, an AND of ORs of literals; clause width K gives K-SAT), formula SAT (arbitrary nested AND/OR/NOT), constant-depth AC circuits, and threshold (TC) circuits built from majority gates.
- The Strong Exponential Time Hypothesis (SETH) posits there is no 1.999…9ⁿ algorithm for SAT (for every string of nines); Williams is on the record as not believing it.
- For 3-SAT, branching on seven of a clause's eight variable assignments (avoiding the single falsifying one) yields roughly 1.9ⁿ; as K grows, known K-SAT algorithms' exponents approach 2ⁿ (1.99, 1.999, …).
- A hypothesis for why SAT solvers work in practice: real-world instances (hardware designs, etc.) are highly structured and extremely compressible, not arbitrary.

- SMT extends SAT with background theories (arithmetic, arrays, etc.); Leonardo de Moura's Z3 is such a solver — push-button and strong at finding bugs, but not at proving their absence (see [[Satisfiability Modulo Theories]] and [[Z3]]).

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[NP-Completeness]] — SAT is the canonical complete problem
- [[Stephen Cook]] — proved SAT NP-complete
- [[Hardness of Approximation]] — the 7/8 threshold
- [[Johan Håstad]] — the 7/8 + ε hardness
- [[Leonid Levin]] — co-proved SAT NP-complete
- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Strong Exponential Time Hypothesis (SETH)]] — hypothesis about SAT's hardness
- [[Circuit Complexity]] — circuit SAT variants
- [[Satisfiability Modulo Theories]] — SAT extended with background theories
- [[Z3]] — the SMT solver built on SAT-style techniques
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
