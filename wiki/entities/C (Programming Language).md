---
title: "C (Programming Language)"
type: entity
tags: [programming-language, systems-programming, C]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
C is the low-level systems programming language created at Bell Labs (co-created by Dennis Ritchie), used as the foundation for C++.

## Key Information
- Its creators (Dennis Ritchie and Brian Kernighan, per the episode's telling) were "down the hall" from Bjarne at Bell Labs.
- Chosen as C++'s low-level foundation because it could manipulate hardware and was very good at the low level.
- Bjarne compiled C++ to C, using C as a portable "assembler" to avoid touching roughly 25 different linkers and dozens of optimizers.
- C compatibility was partly practical ("take Dennis's mistakes, which we know, rather than my mistakes, which we don't know yet") and partly cultural/tooling.
- C's weak legacy type system (implicit narrowing conversions, casts arriving ~5 years after floating point) is "a fundamental flaw in the type system of C and C++" Bjarne tried and failed to remove.
- C borrowed the C++ 11 memory model; identical code yields identical results, though C++ compilers often do more at compile time.
- Dennis Ritchie's "fat pointer" (pointer + size) proposal was rejected by early C for memory reasons but survives as C++ `span`.
- The "C vs C++ language war" is misplaced: the creators were friends, and Ritchie called C++ the obvious successor to C.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Dennis Ritchie]] — co-creator
- [[Brian Kernighan]] — the language's co-documenter
- [[Bell Labs]] — where it was built
- [[Bjarne Stroustrup]] — used it as C++'s base
- [[C++]] — its successor
- [[Simula]] — the other half of C++'s origin
- [[BCPL]] — precursor "that makes C look high-level"
- [[Unix]] — the OS C was written for
- [[Bootstrapping (Compilers)]] — starting point for C++'s bootstrap
