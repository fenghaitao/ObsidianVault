---
title: "Haskell"
type: entity
tags: [language, functional-programming, lazy, statically-typed]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md"]
last_updated: 2026-09-23
---
## Definition
Haskell is a pure, lazy, statically typed functional programming language co-created by Simon Peyton Jones and others.

## Key Information
- Defined by one core principle: side effects are excluded by default; the episode's shorthand is "Immutability changes everything."
- Lazy (call-by-need) by default: `F (3+4)` builds a suspension that may never be evaluated; this laziness forced Haskell to stay pure.
- Originally had no I/O at all — a program was just a function of type `String -> String`. I/O arrived safely via monads.
- Provides an escape hatch `unsafePerformIO` for imperative work, with "unsafe" in the name signaling the programmer's obligation.
- Statically typed with parametric polymorphism; SPJ ranks Haskell (with Scala) at the "bleeding edge" of type systems.
- Its compiler of record is GHC, itself written in Haskell and 35+ years old.
- On SPJ's "useful vs safe" graph, early Haskell was "very safe but useless"; it has since gained usefulness while staying safe.
- Culture: "avoid success at all costs" — never give up the one core principle, even at the cost of a smaller community of users.
- SPJ notes Haskell is "talked about more than used" (Stack Overflow vs GitHub volume) because it asks programmers to genuinely rewire how they think.
- SPJ: if internet software and operating systems had been written in Haskell (or OCaml/ML), ~99% of security exploits would be "removed by construction."

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Simon Peyton Jones]] — co-creator
- [[GHC]] — its compiler
- [[OCaml]] — its strict sibling
- [[ML (Programming Language)]] — its strict ancestor
- [[Scala]] — type-system peer
- [[Verse]] — SPJ's more-expressive project
- [[Functional Programming]] — its paradigm
- [[Lazy Evaluation]] — its default strategy
- [[Monads]] — how it sequences effects
- [[Type System]] — its static types
- [[Effect Systems]] — a finer-grained refinement
- [[Immutability]] — its core value
- [[Side Effects]] — excluded by default
- [[Memory Safety]] — its safety argument
- [[C (Programming Language)]] — the imperative contrast
- [[John Hughes]] — argued for lazy evaluation
- [[Pat Helland]] — "programming with values changes everything"
- [[David Turner]] — lambda-to-SK translation
- [[Lennart Augustsson]] — built microHS
- [[Butler Lampson]] — in the "Haskell is useless" video
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
