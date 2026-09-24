---
title: "Memory Safety"
type: concept
tags: [concept, security, C++, safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
Memory safety is freedom from bugs like buffer overflows and use-after-free; a major, often-misunderstood topic in modern C++.

## Key Information
- Bjarne is "so tired" of C++'s unsafe reputation; he says he hasn't had those problems in years and that >90% of buffer-overflow vulnerabilities come from people writing C-style code with raw pointers.
- Modern C++ offers spans (fat pointers with element counts), vectors, and hardened libraries (Apple, Google, and Microsoft all ship them); a hardened mode became standard in C++ 26.
- His "profiles" work provides enforced guidelines as a way to guarantee you don't do "the stupid things" — applicable beyond memory safety, to learning and domain-specific work.
- Theoretically the problem "was solved many years ago"; the gap is practice, education, and enforcement.
- Simon Peyton Jones: the internet is insecure primarily because infrastructure and operating systems are written in unsafe languages like C, where any function can mutate any memory with no bounds checks.
- Writing that infrastructure in memory-safe languages (Haskell, OCaml, ML) would remove ~99% of exploits "by construction"; Rust with bounds checks on is "much, much better."
- Xavier Leroy: a crash is always "code that can be attacked" — often a security hole — so proving no-crash and array-in-bounds is a simple but powerful formal-verification property, hard to ensure by type system or testing alone.
- seL4, an ~8,000-line microkernel/hypervisor in C that manipulates processes, capabilities, and security tokens, has "every line... proved correct."
- Odersky: a language that is not memory safe "is immediately out because you can't guarantee anything" — memory safety is table stakes, a drive he notes was even promoted by the American government.
- The big memory-unsafe languages are C and C++; he suspects most other low-level systems languages (e.g., Zig or Nim) are not memory safe either.
- But you need more than memory safety: capability safety (agents must not forget or forge capabilities) — "without memory safety you have nothing, because you can fake everything."

### Anders Hejlsberg on Go vs Rust
- Go is "type safe and memory safe" — you don't get stray pointers — whereas Rust's manual strategies (ref counting and others) always carry "that little bit of unsafe"; garbage collection engineered into the language provides those safety guarantees as a separate concern.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language in question
- [[Resource Acquisition Is Initialization (RAII)]] — the lifetime discipline
- [[Herb Sutter]] — provided the vulnerability data
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[Buffer Overflow]] — the exploit class enabled by memory-unsafety
- [[C (Programming Language)]] — the unsafe language
- [[Formal Verification]] — proves the no-crash properties
- [[seL4]] — a proved-correct microkernel
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Martin Odersky]] — memory safety as table stakes
- [[Capability-Based Security]] — the safety that goes beyond memory
- [[Rust]] — the language that made low-level memory safety possible
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
