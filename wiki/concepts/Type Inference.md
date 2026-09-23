---
title: "Type Inference"
type: concept
tags: [type-systems, programming-languages, OCaml]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
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

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Type System]] — what type inference sits within
- [[Parametric Polymorphism]] — emerges for free from inference
- [[Robin Milner]] — the inventor of ML-style type inference
- [[ML (Programming Language)]] — where it was born
- [[OCaml]] — a language with type inference
