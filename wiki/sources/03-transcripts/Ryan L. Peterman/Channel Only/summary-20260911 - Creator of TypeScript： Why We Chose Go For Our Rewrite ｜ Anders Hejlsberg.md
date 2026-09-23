---
title: "summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Core Summary

Anders Hejlsberg explains why the TypeScript compiler's native port from JavaScript was motivated purely by performance and scalability: JavaScript carries a 2–3x performance penalty and, as a single-threaded language, offers no shared-memory concurrency, leaving modern multi-core CPUs underutilized. The team deliberately chose to port rather than rewrite so they could preserve the compiler's semantics and backwards compatibility, then selected Go because it checked the most boxes — mature native codegen, garbage collection, and shared-memory concurrency — while Rust's lack of GC and its borrow checker's inability to express the compiler's circular data structures would have forced a rewrite for the same payoff.

## Key Points

- The problem was "real simple: performance and scalability" — JavaScript was never optimized for compute-intensive workloads like compilers (built for browser UI, originally maybe ~100 lines).
- JavaScript costs a 2–3x performance penalty versus native code and is engineered to be single-threaded — that's why it has callbacks and async — so it can't spin up threads.
- Concurrency with mutable data is hard (races, deadlocks); functional languages make it easier because all the data is immutable.
- JavaScript's only concurrency is web workers, which can't share data — workers must remoting/serialize it (JSON) — so there is no shared-memory concurrency, which is what multi-core CPUs demand ("Moore's law gives us more CPUs, not faster CPUs").
- The first decision was "we're not going to rewrite. We're going to port" — only porting preserves the semantics, algorithms, and exact behavior everyone depends on for backwards compatibility.
- The code already assumed garbage collection and first-class functions (closures); Go checked the most boxes: robust, mature native codegen on all major platforms, GC, and shared-memory concurrency.
- Why not Rust: it lacks GC (manual, or via the borrow checker), and the borrow checker can't express circular data structures (trees with parent pointers, recursive types) that the compiler is "chock full of"; choosing Rust would have meant solving new problems, not just porting — "Rust is no better" on generated-code quality or concurrency gains.
- "Go is type safe and memory safe": GC engineered into the language is a separate concern with safety guarantees, versus Rust's ref-counting strategies that always carry "a little bit of unsafe."

## Related

- [[Anders Hejlsberg]] — guest
- [[TypeScript]] — the compiler being ported
- [[JavaScript]] — the source language and its limits
- [[Go (Programming Language)]] — the chosen target
- [[Rust]] — the rejected alternative
- [[Porting vs Rewriting]] — the core methodology
- [[Garbage Collection]] — a deciding constraint
- [[Functional Programming]] — why immutable data eases concurrency
- [[Concurrency]] — shared-memory concurrency as the goal
- [[Programming Language Design]] — the structured language selection
- [[Memory Safety]] — Go vs Rust safety
- [[Ryan L. Peterman]] — host
