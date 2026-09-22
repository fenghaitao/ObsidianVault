---
title: "Type System"
type: concept
tags: [concept, type-systems, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
A type system lets a compiler reject "silly" programs up front — programs that would fail at run time — before they ever execute.

## Key Information
- Fundamentally, type systems are "about rejecting at compile time programs that you do not want to run."
- Weak type systems get in the way: a Pascal function that reverses a list of integers can't also reverse a list of characters, forcing duplicated code.
- Parametric polymorphism fixes this (`forall A. [A] -> [A]`) and was born in ML ("well-typed programs don't go wrong").
- SPJ's biggest benefit of static typing is maintainability: he does large-scale refactors of 35-year-old GHC "fearlessly" because the type system keeps him safe; types are also how he designs programs.
- Static typing avoids runtime type tags; where a program genuinely can't be typed, escape into dynamic typing (pair a value with its type representation) — Haskell supports this.
- SPJ ranks Haskell and Scala at the type-system frontier, with OCaml close behind.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — a type-system leader
- [[Parametric Polymorphism]] — the essential feature
- [[Monads]] — effects in the type system
- [[Static and Dynamic Typing]] — the typing trade-off
- [[Scala]] — the other type-system leader
- [[Robin Milner]] — "well-typed programs don't go wrong"
- [[Programming Language Design]] — types as a design tool
- [[OCaml]] — close behind in type-system power
