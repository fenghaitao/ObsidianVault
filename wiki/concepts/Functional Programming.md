---
title: "Functional Programming"
type: concept
tags: [concept, programming-paradigm, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---
## Definition
Functional programming is programming with values instead of mutation — excluding side effects by default so computation resembles mathematics.

## Key Information
- SPJ's definition: "programming with values instead of mutation"; imperative programming proceeds by mutating cells over time, while functional programs resemble declarative formulas (like a spreadsheet cell).
- Its essence is the lambda calculus; computation proceeds by reduction, with no notion of a program counter.
- Excluding side effects by default makes programs easier to write, maintain, and reason about; it forces hidden coupling (shared mutable state) into the open, encouraging modular programs.
- Downside: pure functional code is sometimes tiresome/inconvenient — e.g., simply reading the time of day is a side effect; Haskell's escape hatch is `unsafePerformIO`.
- Many ideas "born" in functional programming crossed into the mainstream: garbage collection, lambdas, language-integrated query, type systems, polymorphism, static typing.
- SPJ's stance: "start from functional programming and do imperative programming where necessary."
- SPJ caveats that the case for memory-safe languages is "not just functional programming" — it is specifically about why he considers C an insecure, unsafe language.
- Odersky's definition: "functional programming is programming with values" — values plus functions that transform values into other values, deferring state/side effects until late for predictability and fewer bugs from undocumented effects.
- FP is closely linked to mathematics: theories of polynomials, strings, and lists have no concept of mutation — you transform one into another rather than changing a single coefficient in place.
- Odersky's pragmatic stance: FP is great for ~95% of a program; the remaining 5% may use well-documented side effects, since pure FP that wraps effects in monads can get inconvenient very quickly.
- Roberto Ierusalimschy recommends Haskell as the language with "everything you need to really learn about functional programming," retelling the Haskell joke that in C you spend a week making code efficient and a year making it correct, while in Haskell you make it correct in a week and may spend a year making it efficient.

### Anders Hejlsberg on FP in TypeScript
- Hejlsberg credits JavaScript's first-class functions — functions within functions, closures, passing functions as values — as the thing Brendan Eich got "very right."
- Large portions of the TypeScript compiler are written in a highly functional style over immutable data structures, which enables shared-memory concurrency: threads/processes that don't mutate data can share one structure.
- FP is "much closer to math than machines," and writing "islands of pure functional programming inside an imperative program" combined with concurrency is powerful but complex.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — the pure functional language
- [[Lambda Calculus]] — its essence
- [[Simon Peyton Jones]] — its lifelong advocate
- [[Garbage Collection]] — an FP idea adopted by mainstream
- [[Immutability]] — programming with values
- [[Side Effects]] — what it excludes by default
- [[Monads]] — how pure FP sequences effects
- [[Lisp]] — a mostly functional language
- [[Verse]] — a functional logic descendant
- [[Excel]] — the world's most-used functional language
- [[John Backus]] — advocated FP in his Turing lecture
- [[Alonzo Church]] — seeded it with the lambda calculus
- [[John Hughes]] — "Why Functional Programming Matters"
- [[Pat Helland]] — "programming with values changes everything"
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[Martin Odersky]] — "programming with values"
- [[Scala]] — an impure but FP-first language
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[JavaScript]] — first-class functions
- [[TypeScript]] — compiler written in a functional style
- [[Anders Hejlsberg]] — on FP enabling concurrency
- [[Concurrency]] — immutability enables shared structures
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
