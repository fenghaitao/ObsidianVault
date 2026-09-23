---
title: "Programming Language Design"
type: concept
tags: [programming-languages, design, computing]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

Programming language design is the craft of defining a language's syntax, semantics, and performance trade-offs. Through the examples of Julia and R, John Myles White frames languages as products competing in a zero-sum ecosystem.

## Key Information

- White: programming languages are products in zero-sum ecosystem competition; claiming otherwise "is clearly false and just makes everyone worse."
- Julia's design pitch rejects the "we can't be fast, and fast isn't important" attitude in parts of the Python/R community: write high-level code that runs at C speed.
- R's design costs: pervasive dynamic checks (even the block-delimiting brace can be overridden) and lazy evaluation (arguments passed as "promise" objects) impose runtime overhead.
- Jan Vitek's group paper on R found ~70–90% of those lazy promises did not need to be lazy.
- Motivating gap: R's distance-matrix routine is C for-loops underneath; a naive R translation runs 1,000–10,000x slower.

- Bjarne Stroustrup: language design should start with the problem, not the features — "what you need is a problem that needs a solution." Most who want a "better language" can do it with existing ones; domain-specific languages are fine when they fit.
- For a general-purpose language you are building for others, so "don't think you're the only user."
- Start from what exists: analyze and use help, books, and frameworks like LLVM that "most of the modern languages use to generate decent code"; identify the problem first.
- "Focus on the problem" was also his reply to the common "what pieces do I need to build a language?" question — which he considers the wrong question.
- David J. Malan (2026): C's design strikes a pedagogical balance — "English-like syntax and abstractions on top of lower-level primitives" — and its small language plus small standard library mean students must build most things themselves, making it a deliberate teaching choice rather than a production convenience.
- Simon Peyton Jones frames language design as a safety choice: memory-safe languages (Haskell, OCaml, ML) remove ~99% of exploits "by construction," while unsafe lower-level languages like C leave buffer overruns and raw pointer mutation everywhere.
- Xavier Leroy: exposing shared-memory concurrency forces the designer to settle a memory model — Java went through ~5 iterations and C/C++11's is extremely complex, so OCaml's 2022 multicore support was delayed by both the runtime GC/allocator rewrite and memory-model design.
- Type inference is itself a design trade-off: either full inference with a more restrictive type system, or a richer type system with less powerful inference (subtyping is hard to combine with inference).
- Industry now leads programming-language innovation (Java's GC and bytecode verification, Swift's algebraic data types/pattern matching, Rust's fusion of safe low-level research with C/C++); in the 1990s people wrongly assumed "it will be C++ forever."
- An open problem: programming massively parallel hardware (GPUs) — MLIR and Halide help, but "theorem proving on a GPU" remains out of reach.

- Leonardo de Moura: Lean chose dependent type theory over higher-order logic — despite being "way harder" to implement — because the target community (mathematicians) required it; "listening to your users is important" in language design.
- Lean is a dependently typed language close to Haskell, with tactic mode as a domain-specific language for writing proofs.

- Martin Odersky: languages are drifting to a standard feature set — pattern matching, strong type systems, generics/polymorphism, and closures — features that mostly originated in functional programming.
- Scala's origin is a fusion of three design lineages: Java (platform and objects), OCaml/Standard ML (modules and components), and Haskell (much of the standard library).
- Odersky's design regret: going "full hog" into functional features from the start invited over-abstraction and a culture clash, whereas Go's restraint (adding generics late) let a disciplined style form first.
- AI-era shift: "easy to write" no longer matters as much as high-level ways to constrain and specify what a program should and should not do; prompts should become first-class program values so changes stay incremental.

### Anders Hejlsberg on language design
- Building a language requires mastering both the mechanics (parsers, scanners, lexers, code generators) and the "art of making it feel right."
- "Every new language is actually only 10% new and 90% the same drudgery that every other language has to go do" — be prepared for a lot of uninteresting work.
- The most common mistake: overindexing on one cool idea and underindexing on mundane machinery, so the language does that one thing better but everything else worse.
- It's a long game: every language project he has worked on took at least 10 years, and it's never until version three that a language "truly starts to get okay."
- "You stand on the shoulders of giants" — learn existing languages and styles (procedural, object-oriented, functional) before designing one.
- For choosing an implementation language, he runs a structured evaluation: first decide port vs rewrite, then score candidates on high-order constraints (garbage collection, first-class functions, native codegen, shared-memory concurrency) and pick the one that checks the most boxes for the specific workload.

## Related

- [[summary-20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White]] — source summary
- [[Julia (Programming Language)]] — the fast-by-design language
- [[R (Programming Language)]] — the design-overhead example
- [[Python]] — another dynamic-language comparison
- [[MATLAB]] — Julia's original replacement target
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Bjarne Stroustrup]] — problem-first design philosophy
- [[C++]] — the language he designed this way
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[C (Programming Language)]] — pedagogical balance example
- [[summary-20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan]] — source summary
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[Xavier Leroy]] — guest and language designer
- [[Memory Model]] — a concurrency design challenge
- [[Type Inference]] — a type-system design trade-off
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Dependent Type Theory]] — the design choice for Lean
- [[Lean]] — the language designed this way
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
- [[Martin Odersky]] — Scala's creator and language critic
- [[Scala]] — the fusion language he designed
- [[Type Classes]] — a design choice he regrets skipping
- [[Capability-Based Security]] — the AI-era design direction
- [[Inlining]] — the Scala/Zig/C++ comparison
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[Anders Hejlsberg]] — 10% new / 90% drudgery, long-game view
- [[TypeScript]] — a language he designed
- [[C#]] — a language he designed
- [[Turbo Pascal]] — his first language product
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
