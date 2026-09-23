---
title: "Effect Systems"
type: concept
tags: [concept, type-systems, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
An effect system enriches a type system to describe which specific effects a computation may perform, rather than a binary pure-vs-impure distinction.

## Key Information
- Extends the "pure int-to-int" vs "dirty int-to-int" blunt instrument by enumerating effects: exceptions, spawning threads, reading files, etc.
- Expressible in Haskell's type system, and OCaml "is rapidly becoming same"; a good entry point in Haskell is the Bluefin library designed by Tom Ellis.
- The transcript's "Brazilian programming language papers" is speech-to-text garble; the point is that many papers exist on effect systems.
- Odersky: pure functional programming delays side effects by wrapping them in monads "or whatnot," which "can get very inconvenient very quickly"; he recommends side effects in moderation (~5%) and documenting them well.
- Scala's capability tracking is an effect-like type discipline: a returned value must declare the capabilities it holds (e.g., a stream that secretly holds a file), letting the type system enforce where capabilities may flow.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Monads]] — the coarser mechanism it refines
- [[OCaml]] — recently gained an effect system
- [[Haskell]] — expresses it via Bluefin
- [[Capability-Based Security]] — an effect/capability discipline
- [[Martin Odersky]] — moderation + capability tracking
- [[Scala]] — the language with experimental capability tracking
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
