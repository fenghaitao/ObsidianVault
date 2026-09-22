---
title: "Circuit Complexity"
type: concept
tags: [complexity-theory, circuits, computer-science]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

Circuit complexity studies the size and depth of Boolean circuits (AND/OR/NOT and generalizations such as threshold gates) required to compute functions.

## Key Information

- Boolean formulas can be represented as circuits of varying structure: CNF (an AND of ORs) is a special depth-2 case; arbitrary nested AND/OR/NOT expressions give formula SAT; constant-depth AC circuits alternate unbounded-fan-in AND/OR layers.
- Threshold (TC) circuits use majority gates, which output 1 if and only if at least half of their inputs are 1; with negations, majority gates can simulate standard neural networks, so constant-depth neural networks correspond to constant-depth threshold circuits.
- With larger input spaces (reals/floating points instead of booleans), proving lower bounds becomes much easier — e.g., functions needing depth 3 that cannot be computed in depth 2.
- Ryan Williams proved circuit lower bounds by accident: an algorithm meant to speed up SAT failed, but worked for a large class of circuits for which lower bounds were previously unknown, yielding his first circuit-complexity results (and, he notes, helping him get a job at Stanford).

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Boolean Satisfiability]] — circuit SAT variants
- [[Computational Complexity Theory]] — parent field
