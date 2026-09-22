---
title: "SKI Combinators"
type: concept
tags: [concept, combinators, functional-programming, hardware]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
SKI combinators are three combinators (S, K, I) with simple reduction rules, used as a "machine code" for functional programs.

## Key Information
- Reduction rules: `I x = x`; `K x y = x`; `S x y z = x z (y z)`.
- Any lambda calculus program can be translated into a tree of S and K combinators (David Turner's translation, "half a dozen lines"), and reduction is program execution.
- The SKI machine (SKIM) — built by Thomas Clark, Joe Stoy and others in England — executed SK trees directly in hardware.
- microHS (Lennart Augustsson) implements Haskell via SK combinator reduction and can display the S's and K's it produces.
- SPJ now considers building such hardware a "fun mistake": it did at runtime what a compiler can do at compile time.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Lambda Calculus]] — what gets encoded
- [[David Turner]] — the lambda-to-SK translation
- [[Lennart Augustsson]] — microHS
- [[Dataflow Architecture]] — the other FP-hardware thread
