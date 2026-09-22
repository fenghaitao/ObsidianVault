---
title: "Lazy Evaluation"
type: concept
tags: [concept, evaluation-strategy, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
Lazy evaluation (call-by-need) defers the evaluation of an expression until its value is actually required; it is Haskell's default and a key part of its design.

## Key Information
- In Haskell, `F (3+4)` builds a suspension of `3+4` and passes it to F; the addition runs only if F needs it.
- Laziness forced Haskell to stay pure: deferred expressions have no defined order, so I/O effects could fire in unpredictable order (or not at all).
- John Hughes's "Why Functional Programming Matters" argues lazy evaluation is powerful glue for modular composition (e.g., generating an infinite chess-move tree and pruning it separately).
- Strict languages provide lazy constructs too (iterators/generators in Python and OCaml); the real question is the default, not availability.
- Haskell can opt into strictness (`!`); OCaml can opt into laziness.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — lazy by default
- [[OCaml]] — strict by default
- [[John Hughes]] — argued its importance
