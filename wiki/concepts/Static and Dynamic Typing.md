---
title: "Static and Dynamic Typing"
type: concept
tags: [concept, type-systems, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---
## Definition
Static typing checks types at compile time; dynamic typing checks them at runtime. The trade-off is early error detection and performance versus flexibility.

## Key Information
- Bjarne chose static typing for C++ because of the problems he attacked: a telephone switch can't drop into a debugger on a runtime error, and you want performance and small programs for memory-constrained embedded systems (99% of computers).
- Runtime resolution requires carrying extra data, which conflicts with fitting into 100k–1MB memories (still relevant for cameras, phones, and battery life).
- Dynamic languages (Python, JavaScript) are easier to start in and popular, but errors the type system would catch appear later at runtime; large systems need far more unit testing because the compiler doesn't check for you.
- Raw Python runs ~70x slower than raw C++; its viability comes from key libraries written in C/C++ — the same "two languages" split Bjarne designed C++ to avoid.
- Guarantees that critical systems (telephone switch, car, plane) must not crash are harder in a flexible dynamic type system.
- Xavier Leroy calls JavaScript "the ultimate dynamic language": dynamic type checking plus runtime-redefinable semantics and introspection (a method can inspect its call stack and callers' code) — a "security nightmare" that is "easily abused."
- OCaml, by contrast, is static: static typing and static binding; nearly everything is fixed at compile time, and type inference keeps the code less verbose than fully annotated static typing.
- Roberto Ierusalimschy: scripting and dynamic are different axes — a dynamic language is defined by creating code at runtime (`eval` is the hallmark), while scripting is about coordinating a host program.
- "Compiled" vs "interpreted" is a toolchain property, not a language property — you could compile Python or write an interpreter for C — but `eval` is what keeps dynamic languages mostly interpreted (a compiled dynamic language must ship its compiler as a runtime library).
- Types drive compilation: with known operand types the compiler sizes variables and emits a single integer-add instruction; in a dynamic language `a + b` must inspect and convert operand types at runtime.
- Types that don't guarantee anything (TypeScript-style) can't be used to compile, and type inference for dynamic languages is generally not computable.
- Roberto (2026 clip): knowing operand types at compile time means `a + b` becomes a single typed add; a dynamic language instead compiles `+` to a generic virtual instruction and must check, convert, or concatenate at runtime.

### Anders Hejlsberg on gradual typing
- Hejlsberg frames TypeScript as a "gradual" system between static and dynamic: part of the code is typed while the rest is `any`, and the types are erased at runtime — existing purely for tooling.
- JavaScript's quirks (automatic conversions, `==` vs `===`) are exactly the kind of thing a type checker can track for you, so TypeScript "captures all the badness and parks it."

### Martin Odersky on Scala vs Python
- Python now has optional type syntax plus type checkers, and pattern matching — the gap to Scala is closing, but Scala's always-on strong type system gives real guarantees ("certain bad states can't happen") versus Python where types are "just syntax."
- Scala's inferred types made it "feel like a dynamic language" while retaining the solidity of a good platform — the key to bridging the dynamic and statically typed worlds.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — a statically typed language
- [[Python]] — a dynamically typed language
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[JavaScript]] — the "ultimate dynamic language"
- [[OCaml]] — the static contrast
- [[Type Inference]] — static typing's less-verbose variant
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[TypeScript]] — the gradual typing example
- [[JavaScript]] — whose quirks TypeScript tracks
- [[Anders Hejlsberg]] — on gradual typing
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[Martin Odersky]] — Scala vs Python trade-off
- [[Scala]] — statically typed but feels dynamic
- [[Python]] — optional types close the gap
- [[Type Inference]] — what made Scala feel dynamic
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy]] — source summary
