---
title: "Garbage Collection"
type: concept
tags: [concept, memory-management, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
Garbage collection is automatic reclamation of unreachable memory; C++ supports it optionally but does not require it.

## Key Information
- Early high-level languages often required garbage collection, which is poor for device drivers (or for building collectors) — so Bjarne avoided requiring it in C++.
- In 1995 the standards committee (led by Hans Boehm, who has a conservative collector) wanted a standard interface; one was added to C++ 11 so GC use could be standardized.
- Over the next ~10 years usage declined as RAII became better understood; today only a few use GC, and it's no longer part of the standard.
- Mechanically it wraps the allocation/deallocation primitives (`new`, `delete`, `operator new`, `malloc`).
- OCaml's low-latency allocator/GC avoids long pauses, which matters for network programming; Cornell's Ensemble project even ran the GC while network packets were in flight.
- GC has runtime overhead (~10–30% in some applications) because it scans memory at run time, but it enables cheap, safe sharing of data structures — manual memory management is not always faster.
- Heap allocation is cheap for short-lived objects (they die before the next collection); that is why stack allocation wins less than expected for them.

### Anders Hejlsberg on GC and the Go choice
- For the TypeScript compiler port, GC was a deciding constraint: the existing codebase already assumed garbage collection, so the target language had to provide it "engineered into the language."
- External GC libraries come with restrictions and lack the safety guarantees of language-integrated GC; Rust's borrow checker/ref counting leaves "that little bit of unsafe" where manual memory management must be worked around.
- Garbage collection engineered into a language is "a separate concern" — the programmer does nothing special except avoid holding data no longer needed.

### Martin Odersky on GC vs embedded
- Scala is garbage-collected, which means small pauses and needing a big chunk of memory to run fast; Rust runs in much smaller memory, which is better for embedded systems.
- "If you have the memory for a garbage collector, you should absolutely use one because it makes a lot of things simpler" — hence his view that Rust is overused above the embedded/OS level.
- Modern collectors "have become quite capable... brilliant," with very small pauses, but it remains a fact that a GC language needs "a big chunk of memory" to run fast.
- You cannot turn off Scala's GC in production; research would allow custom allocators with static reference tracking (à la Zig), but it isn't shipped yet.
- The JVM has very good, high-performance garbage collectors — one reason to target bytecode.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — supports it optionally
- [[Resource Acquisition Is Initialization (RAII)]] — the preferred discipline
- [[Hans Boehm]] — its main advocate in standardization
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[OCaml]] — low-latency GC user
- [[Manual Memory Management]] — the contrasting model
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Go (Programming Language)]] — chosen partly for its GC
- [[TypeScript]] — the compiler that was ported
- [[Anders Hejlsberg]] — on GC vs Rust's borrow checker
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[Martin Odersky]] — "use a GC when you have the memory"
- [[Scala]] — the GC language compared with Rust
- [[Rust]] — runs in far smaller memory
- [[JVM]] — ships high-performance collectors
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
