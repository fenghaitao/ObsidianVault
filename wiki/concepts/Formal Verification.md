---
title: "Formal Verification"
type: concept
tags: [formal-methods, verification, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Formal verification is the use of mathematical reasoning and static-analysis algorithms to prove, for all possible inputs and executions, that a program satisfies a specification — guarantees that testing and code review cannot provide.

## Key Information

- Dijkstra's dictum frames it: "testing can only show the presence of bugs, but not their complete absence," because there are infinitely many inputs and you can only sample them.
- Specifications range from simple (the program never crashes on well-formed inputs; all array accesses are in bounds) to precise (it terminates, leaks no confidential data, or computes a function to within a stated floating-point error).
- A crash is always "code that can be attacked" — often a security hole — so even the simple no-crash property is valuable and hard to guarantee by type system or testing alone.
- Techniques span fully automatic static analysis (good at proving absence of bugs like out-of-bounds accesses) to interactive, human-guided program proofs of mathematical statements about the program.
- A subtle trap: an unsatisfiable precondition (e.g., "arguments must not be too big" that can never be met) makes the body trivially verifiable — a false sense of confidence; testing a specification is one countermeasure.
- Formal methods people dislike assignment/imperative features because pure functional style is much closer to mathematical style and easier to reason about.
- A hot topic in software science since the 1970s; Leroy hopes this may become "the decade of formal verification of software."

- Leonardo de Moura: a specification/proof is a superset of a test suite — with a proof you cover all possible cases and can say "there's no point testing anymore; I prove it."
- The real cost was developing and *maintaining* proofs (historically ~10x program time, e.g. seL4); AI now drafts and maintains proofs, which de Moura calls the key to making formal verification mainstream.
- An inefficient (naive) implementation can act as the specification: ask the AI to optimize, and prove the optimized code equivalent to the naive one — "inefficient program is a spec."
- AWS used formal verification for a decade but only on safety-critical components because it was expensive — "until now," AI changes the economics.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Proof Assistants]] — the interactive tools used
- [[Semantics of Programming Languages]] — the mathematical meaning verification relies on
- [[CompCert]] — a landmark verified artifact
- [[seL4]] — a fully proved microkernel
- [[Edsger Dijkstra]] — the "testing shows presence, not absence" dictum
- [[Memory Safety]] — the no-crash/no-overflow properties verification establishes
- [[Leonardo de Moura]] — Lean's creator on AI + verification
- [[Interactive Theorem Proving]] — how proofs are built
- [[Formalization of Mathematics]] — the math-only flavor
- [[Satisfiability Modulo Theories]] — the automatic (SMT) contrast
- [[Z3]] — the automatic solver that couldn't prove absence
- [[mathlib]] — the library for math formalization
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
