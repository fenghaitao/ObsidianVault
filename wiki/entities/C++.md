---
title: "C++"
type: entity
tags: [programming-language, systems-programming, C++]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260918 - Update on Quitting My Job at Meta.md"]
last_updated: 2026-09-23
---
## Definition
C++ is the general-purpose, statically typed programming language created by Bjarne Stroustrup at Bell Labs, combining Simula-style classes with C's low-level efficiency.

## Key Information
- Origin: a merge of Simula's class concept with C, driven by the need for high-level and low-level facilities in one language for distributed systems.
- Built by bootstrapping: started as a C pre-processor ("C with Classes"), then a compiler written in that subset, iterating version after version.
- C compatibility was both an implementation technique (compile to C, treat C as a portable "assembler") and a cultural/tooling decision.
- Not an object-oriented language, per Bjarne — it is type/class-oriented, supporting multiple paradigms including generic programming.
- Strong, static typing was chosen for reliability, performance, and small-memory (embedded) targets — roughly 99% of computers are embedded systems.
- Performance: same machine model as C (C borrowed C++ 11's memory model); its abstractions are "compiled away," enabling zero- and even negative-overhead abstraction.
- Memory safety: modern C++ (spans, vectors, hardened libraries) is safe; >90% of problems come from old C-style code. A hardened mode standardized in C++ 26; profiles are proposed for C++ 29.
- Standardization began in 1989/1990 under ISO after IBM, HP, and Sun/DEC insisted; the committee grew to 527 members working by consensus.
- Regrets in hindsight: implicit narrowing conversions (a legacy C flaw he couldn't remove), releasing before templates (later saved by Alex Stepanov's STL), and an over-large committee.
- Competing languages mostly use C++ infrastructure (e.g., LLVM); Java's "we'll kill C++" ads failed — he estimates 10–12x more C++ developers now.
- Roberto Ierusalimschy cites C++ as a good example of a language that is "really, really complex" on the simplicity spectrum (with JavaScript "even worse").
- Lua is typically combined with C or C++ as the host language in a dual-language architecture: Lua takes the dynamic parts while C/C++ handles the hard, resource-intensive parts.
- Martin Odersky's warning example for inlining: expanding a C++ template can produce "very complex type errors and very hard to debug" programs — the failure mode that Zig's comptime inlining and Scala's type-restricted `inline` avoid.
- Ryan L. Peterman named C++ as his first programming language and said he'd looked up to Bjarne Stroustrup ever since learning it; he interviewed Bjarne in his study against a wall of C++ books, shot with two iPhones.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Bjarne Stroustrup]] — creator
- [[Bell Labs]] — where it began
- [[C (Programming Language)]] — the low-level base
- [[Simula]] — source of the class concept
- [[Unix]] — target system environment
- [[LLVM]] — modern infrastructure competitors use
- [[Standard Template Library (STL)]] — standard library
- [[Alex Stepanov]] — STL creator
- [[Herb Sutter]] — memory-safety data
- [[Hans Boehm]] — GC interface advocate
- [[Vasa (Ship)]] — his cautionary tale for the committee
- [[AT&T]] — the owning employer
- [[Zero Overhead Abstraction]] — design principle
- [[Memory Safety]] — modern C++
- [[Object-Oriented Programming]] — what C++ is not
- [[Bootstrapping (Compilers)]] — how it was built
- [[Generic Programming]] — paradigm it supports
- [[Resource Acquisition Is Initialization (RAII)]] — lifetime discipline
- [[Garbage Collection]] — optional interface
- [[Premature Optimization]] — what he warns against
- [[Static and Dynamic Typing]] — why static typing
- [[Template Metaprogramming]] — compile-time computation
- [[Programming Language Design]] — his craft
- [[IBM]] — pushed standardization; PowerPC corner
- [[Intel]] — x86 corner of the dispute
- [[Sun Microsystems]] — Java marketing rival
- [[Java]] — the "C++ killer" that wasn't
- [[Python]] — dynamic-language contrast
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
- [[Zig]] — whose comptime inlining avoids C++ template type-error hell
- [[Inlining]] — the mechanism under comparison
- [[summary-20260918 - Update on Quitting My Job at Meta]] — source summary
- [[Ryan L. Peterman]] — whose first programming language was C++
