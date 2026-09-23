---
title: "Satisfiability Modulo Theories"
type: concept
tags: [logic, algorithms, formal-methods, automated-reasoning]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Satisfiability Modulo Theories (SMT) extends SAT solving with decision procedures for useful background theories (arithmetic, arrays, and others), producing a push-button constraint solver.

## Key Information

- Leonardo de Moura's Z3 is an SMT solver: "a SAT solver, but you have background theories" — arithmetic and arrays, chosen because they are needed for software test-case generation and verification.
- Concrete use: encode a Sudoku puzzle as constraints and Z3 returns a solution instantly; a reachable-vulnerable-code-path query returns a concrete counterexample input or "unsatisfiable" (the path is impossible).
- SMT sits atop the full complexity ladder (NP-complete, PSPACE-complete, and undecidable problems), yet is effective in practice when queries are bounded ("find a bug in the first 10 steps").
- SMT-LIB is the simple, tool-facing input language; unlike Lean, an SMT solver is not a programming language, cannot do abstract mathematics, and can only prove simple properties.
- Its one-step, opaque reasoning contrasts with interactive theorem proving: you cannot easily influence what the solver does, which is why de Moura built Lean for proving the absence of bugs.

## Related

- [[Boolean Satisfiability]] — SAT, which SMT extends
- [[Z3]] — the canonical SMT solver
- [[Formal Verification]] — a primary application
- [[Lean]] — the interactive alternative for proving absence of bugs
- [[Computational Complexity Theory]] — the complexity classes SMT spans
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
