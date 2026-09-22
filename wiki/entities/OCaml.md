---
title: "OCaml"
type: entity
tags: [language, functional-programming, ML, strict]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
OCaml is a statically typed, strict (call-by-value) functional language that grew out of the ML tradition.

## Key Information
- Strict / call-by-value: `F (3+4)` evaluates the argument before calling F, giving a defined order of evaluation.
- Because evaluation order is defined, OCaml allows I/O directly ("print hello; print goodbye" works) — it is impure by default, in contrast to Haskell, which laziness forced to stay pure.
- Gained a very fancy type system and, recently, an effect system and many new extensions; described as "a hotbed of innovation at the moment."
- Explored functor-style module systems much more deeply than Haskell ever did.
- SPJ describes OCaml and Haskell as siblings: they learn from and compete with each other, and are converging toward the middle on strictness versus laziness.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — its lazy sibling
- [[ML (Programming Language)]] — its ancestor
- [[Lazy Evaluation]] — the opposing default
- [[Effect Systems]] — a feature it recently gained
- [[Type System]] — its strong static typing
