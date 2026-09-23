---
title: "C (Programming Language)"
type: entity
tags: [programming-language, systems-programming, C]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
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
- David J. Malan (2026): C is "about as close as you can get to the hardware" before code "devolves, at least aesthetically, into assembly code"; beyond that are "zeros and ones."
- Pedagogically it "strikes this really nice balance" of English-like syntax and abstractions over lower-level primitives, letting students explore procedural programming (loops, conditions, functions, variables, return values).
- It is "a pretty small language" with "not a very large standard library" (unless you add third-party code), so most things must be built yourself — C has no instantiable built-in data structures like Java/C++'s STL.
- That forces students to build hash tables, singly/doubly linked lists, tries, trees, and abstract data types (stacks, queues) themselves, which Malan values for bottom-up understanding rather than for later reuse.
- C remains ranked #1/#2 annually in omnipresence because it is "very highly performant," though more challenging to write than some languages.
- Simon Peyton Jones: C is unsafe because any function can mutate any memory at any time via raw pointers with no array-bounds checks — "super unsafe."
- SPJ argues most internet exploits stem from C-style buffer overruns and pointer manipulation, and that memory-safe languages would remove ~99% of them "by construction."
- Xavier Leroy's CompCert is a formally verified C compiler, proved to translate C to assembly while faithfully preserving program semantics (no miscompilation).
- In shared-memory concurrency, C and C++ say a race is "undefined behavior"; the C/C++11 memory model is a real improvement over Java's several iterations but remains extremely complex.
- Depending on the host's toolchain, OCaml programs call into C via a foreign function interface, joining the C linker when statically linked.

### Roberto Ierusalimschy on C and Lua
- Lua's C interop works through C function pointers: C registers a pointer under a name in a Lua state, and the Lua interpreter calls that pointer; a Lua function is just bytecode data that C asks the interpreter to run — calls can nest recursively across the boundary.
- Lua's portability rests on C's portability: the interpreter (a loop-with-switch virtual machine) is written in C and compiled per platform.
- C's long absence of a Boolean type (using integers as truth values up to C99) influenced Lua's own lack of Booleans for years.
- C's "indexing" is really pointer arithmetic (an offset from an address), which is why zero-based indexing arose; languages without pointer arithmetic copied the convention anyway.

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
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[summary-20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan]] — source summary
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[Buffer Overflow]] — the vulnerability class tied to C
- [[Memory Safety]] — what C lacks by default
- [[CompCert]] — the verified C compiler
- [[Memory Model]] — C/C++ concurrency semantics
- [[Xavier Leroy]] — verified a C compiler's correctness
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
