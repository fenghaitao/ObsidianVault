---
title: "OCaml"
type: entity
tags: [language, functional-programming, ML, strict]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
OCaml is a statically typed, strict (call-by-value) functional language that grew out of the ML tradition.

## Key Information
- Strict / call-by-value: `F (3+4)` evaluates the argument before calling F, giving a defined order of evaluation.
- Because evaluation order is defined, OCaml allows I/O directly ("print hello; print goodbye" works) — it is impure by default, in contrast to Haskell, which laziness forced to stay pure.
- Gained a very fancy type system and, recently, an effect system and many new extensions; described as "a hotbed of innovation at the moment."
- Explored functor-style module systems much more deeply than Haskell ever did.
- SPJ describes OCaml and Haskell as siblings: they learn from and compete with each other, and are converging toward the middle on strictness versus laziness.
- SPJ names OCaml as one of the memory-safe languages that, had the internet's software been written in it, would remove ~99% of exploits "by construction."
- Xavier Leroy describes OCaml as both "a fine functional language" and "a fairly decent systems programming language": a full functional core plus imperative control (exceptions, threads, user-defined effect handlers) and a predictable cost model with a low-latency allocator/GC.
- Originally aimed at theorem proving and DSLs, OCaml became a systems language after Cornell's Ensemble project (late 1990s) rewrote its reliable-multicast C stack in OCaml with roughly C-level performance; Ensemble PhD student Yaron Minsky then built Jane Street's trading infrastructure in OCaml.
- Gained multicore support in 2022 after a runtime GC/allocator rewrite and agreement on a memory model, done mostly by OCaml Labs at Cambridge.
- Leroy contrasts OCaml's static typing and static binding with JavaScript being "the ultimate dynamic language."
- Odersky names OCaml (with Standard ML) as a core Scala influence, contributing the language's module and component system.
- The claim that sold Twitter's engineers on Scala: it is "actually quite a lot like OCaml," but unlike OCaml it runs on the JVM.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — its lazy sibling
- [[ML (Programming Language)]] — its ancestor
- [[Lazy Evaluation]] — the opposing default
- [[Effect Systems]] — a feature it recently gained
- [[Type System]] — its strong static typing
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Xavier Leroy]] — the language's creator
- [[Yaron Minsky]] — Ensemble PhD student who brought OCaml to Jane Street
- [[Jane Street]] — major trading user
- [[MirageOS]] — unikernel project in OCaml
- [[Memory Model]] — the multicore design challenge
- [[Martin Odersky]] — Scala's OCaml/ML lineage
- [[Scala]] — "quite a lot like OCaml" on the JVM
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
