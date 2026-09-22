---
title: "Functional Programming"
type: concept
tags: [concept, programming-paradigm, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
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
