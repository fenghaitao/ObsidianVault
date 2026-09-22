---
title: "summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Core Summary
Simon Peyton Jones, co-creator of Haskell, explains functional programming as "programming with values instead of mutation" and traces its intellectual roots to Alonzo Church's lambda calculus versus Alan Turing's mutation-based Turing machine. He contrasts Haskell's pure, lazy, statically typed design with OCaml's strict, impure-by-default approach, and explains how monads and type systems keep effects visible and programs maintainable. He walks through GHC's compiler pipeline (parse → rename → type check → desugar into a typed Core based on System F, then lower to C--) and revisits the "fun mistake" of building hardware directly for functional programs (SKI/SKIM and MIT's Monsoon dataflow machine). The conversation ends with his views on programming languages in the LLM era, his new Verse language at Epic Games, Excel as the world's most-used functional language, and advice that "co-pilots need pilots."

## Key Points
- Functional programming is about values, not mutation; its essence is the lambda calculus, which is computationally equivalent to the Turing machine.
- Haskell is pure (side effects excluded by default) and lazy by default; laziness forced Haskell to stay pure, whereas OCaml's strictness let it be impure by default.
- Laziness is "powerful glue" for modular composition — the classic example is John Hughes's chess-tree generator + independent pruner.
- Monads (via do notation) sequence effectful I/O while keeping the language pure; effect systems such as Bluefin enumerate which effects a computation may have.
- Type systems reject "silly" programs at compile time; parametric polymorphism is essential, and the biggest payoff is long-term maintainability — he refactors 35-year-old GHC "fearlessly."
- On the "useful vs safe" graph, C is useful but dangerous, early Haskell was safe but useless; Rust moved along the useful axis toward safety.
- Hardware built to execute functional programs (SKI/SKIM, MIT's dataflow Monsoon) was a "fun mistake" — it did at runtime what a compiler does better at compile time.
- "Immutability changes everything" and "avoid success at all costs" capture Haskell's one-key-idea culture.
- Statically typed languages are "a huge boon for LLMs" because the compiler rejects implausible programs immediately.
- Future direction: Verse (a functional logic language at Epic Games); Excel is the world's most-used functional (and, by orders of magnitude, programming) language.
- Career advice: successful people are "making it up as they go along"; luck finds people who take risks.

## Related
- [[Simon Peyton Jones]] — guest and Haskell co-creator
- [[Haskell]] — the language at the center of the episode
- [[GHC]] — Glasgow Haskell Compiler
- [[Functional Programming]] — the core concept
- [[Lambda Calculus]] — the theoretical foundation
- [[Type System]] — a major topic
- [[Monads]] — how Haskell handles effects
- [[Lazy Evaluation]] — Haskell's defining evaluation strategy
- [[OCaml]] — Haskell's strict sibling language
- [[ML (Programming Language)]] — Haskell's strict ancestor
- [[Scala]] — type-system peer
- [[Lisp]] — mostly functional language / Lisp machine
- [[Verse]] — the guest's current project
- [[Excel]] — the world's most-used functional language
- [[C--]] — GHC's portable assembly stage
- [[Alonzo Church]] — inventor of the lambda calculus
- [[Alan Turing]] — Turing machine vs lambda calculus
- [[John Backus]] — Turing Award lecture on functional programming
- [[Robin Milner]] — "well-typed programs don't go wrong"
- [[John Hughes]] — "Why Functional Programming Matters"
- [[Pat Helland]] — "programming with values changes everything"
- [[David Turner]] — lambda-to-SK translation
- [[Lennart Augustsson]] — built microHS
- [[Arvind]] — led MIT's dataflow group
- [[Symbolics]] — the Lisp machine company
- [[Epic Games]] — employer behind Verse
- [[Butler Lampson]] — in the "Haskell is useless" video
- [[Rust]] — the safer useful-language benchmark
- [[C (Programming Language)]] — useful but dangerous
- [[Microsoft]] — SPJ's former employer; Excel
- [[MIT]] — dataflow group
- [[LLVM]] — GHC backend option
- [[Immutability]] — "changes everything"
- [[Side Effects]] — excluded by default
- [[Parametric Polymorphism]] — types that work for all A
- [[Effect Systems]] — enumerating effects
- [[SKI Combinators]] — machine code of functional programming
- [[Dataflow Architecture]] — hardware for functional programs
- [[Memory Safety]] — why unsafe languages failed us
- [[Static and Dynamic Typing]] — the typing trade-off
- [[Turing Completeness]] — lambda and Excel
- [[Object-Oriented Programming]] — subtype polymorphism
- [[Programming Language Design]] — future of languages
- [[Garbage Collection]] — an FP idea adopted by mainstream
