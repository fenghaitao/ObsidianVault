---
title: "Effect Systems"
type: concept
tags: [concept, type-systems, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
An effect system enriches a type system to describe which specific effects a computation may perform, rather than a binary pure-vs-impure distinction.

## Key Information
- Extends the "pure int-to-int" vs "dirty int-to-int" blunt instrument by enumerating effects: exceptions, spawning threads, reading files, etc.
- Expressible in Haskell's type system, and OCaml "is rapidly becoming same"; a good entry point in Haskell is the Bluefin library designed by Tom Ellis.
- The transcript's "Brazilian programming language papers" is speech-to-text garble; the point is that many papers exist on effect systems.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Monads]] — the coarser mechanism it refines
- [[OCaml]] — recently gained an effect system
- [[Haskell]] — expresses it via Bluefin
