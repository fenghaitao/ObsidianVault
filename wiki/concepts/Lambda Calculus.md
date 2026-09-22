---
title: "Lambda Calculus"
type: concept
tags: [concept, computer-science, lambda-calculus, computability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
The lambda calculus is Alonzo Church's formal model of computation with no notion of mutation, in which programs execute "just by reduction" — the essence of functional programming.

## Key Information
- Developed by Alonzo Church around 1930, at the same time Alan Turing was developing the mutation-based Turing machine.
- Anything computable by a Turing machine is computable by the lambda calculus and vice versa — the two have identical computational power.
- Lambda terms can be translated into SK combinators (David Turner's translation), giving a simple rewrite-based "machine code" for functional programs.
- GHC's Core language is a statically typed lambda calculus (System F, from Girard).

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Alonzo Church]] — its inventor
- [[Alan Turing]] — the equivalent model's inventor
- [[Functional Programming]] — the paradigm it underpins
- [[SKI Combinators]] — a rewrite encoding of it
- [[Turing Completeness]] — the shared power of both models
- [[GHC]] — whose Core is a typed lambda calculus
- [[C--]] — the stage GHC lowers it to
- [[John Backus]] — advocated FP built on this model
- [[David Turner]] — the lambda-to-SK translation
- [[Lennart Augustsson]] — microHS reduction
- [[Lisp]] — a mostly functional language in its lineage
- [[Excel]] — gained LAMBDA for Turing completeness
