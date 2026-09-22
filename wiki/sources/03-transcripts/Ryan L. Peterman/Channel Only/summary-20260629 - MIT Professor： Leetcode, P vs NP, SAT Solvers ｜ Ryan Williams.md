---
title: "summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Core Summary

MIT professor and Gödel Prize winner Ryan Williams opens with the three-sum problem, walking from brute-force O(n³) to the classic O(n²) two-pointer "finger search" and then to the surprising fact that three-sum can be solved subquadratically by preprocessing groups and speeding up finger moves. He explains fine-grained complexity — asking whether canonical textbook time bounds (n², n³, 2ⁿ) are optimal — and the Strong Exponential Time Hypothesis, stressing that these tools can relate problems (like NP-complete subset sum and polynomial two-sum) that classical P vs NP theory cannot. He assigns contrarian confidence levels to complexity conjectures (80% P ≠ NP, 45% EXP ≠ NEXP, 80% NEXP = coNEXP), arguing we don't understand polynomial-time computation nearly as deeply as we think. He also recounts the intuition behind his √T-space simulation breakthrough, describes SAT's many forms (CNF, K-SAT, AC/TC circuits, and their neural-network analogue), and closes with research philosophy and career advice around permissionless, self-evaluated work.

## Key Points

- Three-sum: brute force is O(n³); the popular O(n²) algorithm sorts and then, for each element A, runs a two-pointer "finger search" over the rest — start fingers at min and max, sum them with A, and move the right finger down if too large or the left finger up if too small until the pair is found or the fingers cross.
- Three-sum can be beaten subquadratically: break the sorted list into small groups, preprocess a fast lookup structure, and perform finger searches over groups rather than single elements; known bounds include n² / ((log n)(log log n))^(2/3). Williams stresses these ideas grow directly out of the finger-search solution (often via the linear decision tree model).
- Fine-grained complexity asks whether canonical textbook algorithms are optimal — whether n², n³, or 2ⁿ can be improved by any constant epsilon — and builds a theory of "improving one problem a little bit implies improving another a little bit."
- It can relate problems that classical P vs NP theory cannot: subset sum (NP-complete, naive 2ⁿ) reduces to two-sum (polynomial, naive n²) via meet-in-the-middle — split numbers into halves, enumerate 2^(n/2) sums per half, then solve a two-sum — yielding about 2^(n/2) time even though the reduction blows up the instance size.
- Strong Exponential Time Hypothesis (SETH): SAT cannot be solved substantially faster than 2ⁿ (no 1.999…9ⁿ algorithm, however many nines). Williams is "on the record as not believing" SETH, but finds assuming it false operationally useful because it sends his thinking in new directions; "hypotheses at the edge of our understanding can be enlightening."
- Williams's contrarian confidence in a paper on the likelihood of complexity conjectures: P ≠ NP only 80% (Scott Aaronson nudged him up from ~75%), EXP ≠ NEXP only 45% (he believes NEXP = EXP more likely than not), and 80% for NEXP = coNEXP. His rationale: algorithms constantly produce surprises while lower bounds rarely do.
- SAT forms: CNF (DIMACS format, an AND of clauses that are ORs of literals; clause width K gives K-SAT), formula SAT (arbitrary nested AND/OR/NOT expression), constant-depth AC circuits (alternating AND/OR layers), and threshold (TC) circuits built from majority gates.
- For K-SAT, as K grows the known algorithms' exponents approach 2ⁿ (1.99, 1.999, …). For 3-SAT, branch on seven of a clause's eight variable assignments (ruling out the one falsifying assignment) to get roughly 1.9ⁿ.
- Neural nets as circuits: a majority gate (outputs 1 iff at least half its inputs are 1), plus negations, can simulate standard neural networks — constant-depth networks become constant-depth threshold circuits. With real/floating-point inputs, lower bounds become much easier (e.g., depth 3 vs depth 2).
- Time–space simulation: Hopcroft, Paul, and Valiant (1975, based on Paterson and Valiant) showed time-T computations can be simulated in space T/log T; Williams's 2025 result improves this to √T space (still requiring exponential time). The insight came from reading James Cook and Ian Mertz's tree-evaluation paper: XORing into existing memory (like XOR-swapping two registers without a temp) avoids the erasure-based style, and √T is the sweet spot balancing the number of intervals against steps per interval.
- Research philosophy: seek "win-win" setups where a hypothesis H and its negation both yield progress; he works on methods and spaces of ideas rather than single problems. Career advice: you don't need permission to work on hard problems, and avoid inertia through periodic self-evaluation (comparing past vs present self).
- Book recommendations for complexity theory: Avi Wigderson's book, the early chapters of Lance Fortnow's The Golden Ticket, Moore and Mertens' The Nature of Computation, and Sipser's Introduction to the Theory of Computation.

## Related

- [[Ryan Williams]] — guest
- [[MIT]] — his institution
- [[Gödel Prize]] — his award
- [[LeetCode]] — three-sum interview framing
- [[Scott Aaronson]] — confidence calibration
- [[Avi Wigderson]] — book recommendation
- [[Lance Fortnow]] — book recommendation
- [[Michael Sipser]] — book recommendation
- [[P vs NP]] — debated confidence
- [[NP-Completeness]] — reductions / subset sum
- [[Boolean Satisfiability]] — SAT and its variants
- [[Computational Complexity Theory]] — the field
- [[Time Complexity]] — fine-grained focus
- [[Space Complexity]] — the √T result
- [[Fine-Grained Complexity]] — his research field
- [[Strong Exponential Time Hypothesis (SETH)]] — contrarian take
- [[Three-Sum Problem]] — opening problem
- [[Subset Sum]] — reduction example
- [[Meet-in-the-Middle]] — technique
- [[Circuit Complexity]] — threshold circuits
