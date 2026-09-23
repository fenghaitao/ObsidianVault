---
title: "Memory Safety"
type: concept
tags: [concept, security, C++, safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
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
