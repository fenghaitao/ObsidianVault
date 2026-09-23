---
title: "Type Inference"
type: concept
tags: [type-systems, programming-languages, OCaml]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Type inference is the compiler's deduction of types from how variables are used, so the programmer does not have to declare the type of every variable, parameter, or local.

## Key Information

- Basic idea: from `x = string_length(s)` you deduce `s` is a string and `x` is an integer, from the type of `string_length`.
- Mechanically, the compiler collects constraints and solves them; no solution is a type error, and several solutions require criteria so the result is predictable for programmers.
- A worked example: `if x = y` constrains x and y to the same type but leaves it unspecified; later knowledge about x propagates to y.
- Under-constrained types yield polymorphism "for free" — the type checker sees no constraints and generalizes to "any type" — Robin Milner's great insight behind ML.
- Main advantage: less verbose code — annotate types only where they document and clarify, and omit them for short-lived locals.
- Trade-offs: type-error messages can be confusing and may not point at the actual source of the error; subtyping (from object-oriented languages) is hard to combine with full inference, forcing a choice between powerful inference and a richer type system.
- Roberto Ierusalimschy: whole-program type inference for dynamic languages is "not computable"; many people have tried, but it is very hard to get useful performance — inference either demands a rigid coding style or yields very generic types.
- The same idea applies to LuaJIT: performance improves a lot if the programmer follows an informal type discipline (not reusing a variable for integers and then strings), even though the language does not enforce it.
- Odersky lists type inference among the hard, competing demands on a compiler: programmers expect the compiler to infer types that "make sense" while also generating efficient code quickly.
- Scala's inferred types let it feel like a dynamic language while retaining the solidity of a good platform — the key reason it bridged dynamic and statically typed worlds (e.g., Twitter's migration from Ruby).
- Asked directly whether you could run type inference on Lua to get an unambiguous set of types for compilation, Roberto answers no: with the right types a compiler is much easier to write, but for dynamic languages you must instead write with implicit type discipline — otherwise inference either fails or infers overly generic types you can't exploit.
- Roberto cites Haskell as the positive case for inference: its types are optional everywhere, yet the language can infer the types of everything correctly.

### Anders Hejlsberg on Flow
- Facebook's Flow "was doing type inference on top of JavaScript" as a rival to TypeScript, but it was written in OCaml (transcribed "camel"), which made community contribution harder, and it didn't focus on IDE-based tooling — a key reason TypeScript won the competition to type JavaScript.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Type System]] — what type inference sits within
- [[Parametric Polymorphism]] — emerges for free from inference
- [[Robin Milner]] — the inventor of ML-style type inference
- [[ML (Programming Language)]] — where it was born
- [[OCaml]] — a language with type inference
- [[Scala]] — felt dynamic thanks to inferred types
- [[Martin Odersky]] — type inference as compiler demand
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[TypeScript]] — beat Flow's inferred-types rival
- [[Anders Hejlsberg]] — on Flow vs TypeScript
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy]] — source summary
- [[summary-20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy]] — source summary
