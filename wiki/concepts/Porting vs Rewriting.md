---
title: "Porting vs Rewriting"
type: concept
tags: [concept, compilers, software-engineering, backwards-compatibility]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

Porting vs rewriting is the engineering decision between mechanically translating an existing codebase into a new language while preserving its semantics, versus rewriting from scratch for cleanliness at the cost of backwards compatibility.

## Key Information

- Hejlsberg's first decision for the TypeScript 7 native port was "we're not going to rewrite. We're going to port" — only porting preserves the compiler's semantics, algorithms, and exact behavior that everyone depends on for backwards compatibility.
- Rewrites are "toxic often for ecosystems" because they sacrifice compatibility: you never get back to exactly what you had, and users suffer through every change made "in the name of making it better or prettier."
- A rewrite can effectively produce a "different language" — different errors or behavior at points where the implementation must choose between multiple possibilities.
- Porting constrains the target language choice: the TypeScript codebase already assumed garbage collection and first-class functions, so the new language had to provide both.
- Mechanically, the team wrote a tool that syntactically translated TypeScript into Go (syntactically valid but not compiling), then refactored data structures — a deterministic translation is preferred over stochastic AI because it produces the same transformation every run.
- Hejlsberg reports no benefits left on the table by porting instead of rewriting.

## Related

- [[TypeScript]] — the compiler that was ported
- [[Go (Programming Language)]] — the port target
- [[Anders Hejlsberg]] — who led the decision
- [[Garbage Collection]] — a constraint on the target language
- [[Concurrency]] — the performance motivation
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
