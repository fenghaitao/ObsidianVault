---
title: "Zero Overhead Abstraction"
type: concept
tags: [concept, performance, abstraction, C++]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Zero-overhead abstraction is the C++ principle that abstractions should impose no runtime cost beyond what hand-written code would, and can even enable "negative overhead" when the compiler uses the extra information to optimize better.

## Key Information
- C++'s guiding principle; Bjarne now argues "zero overhead" understates what modern C++ compilers do — they can achieve "negative overhead abstraction," where using abstraction is faster than hand-written lower-level code.
- More abstraction need not cost performance: abstractions are "compiled away."
- C is not necessarily closer to the machine or faster: C and C++ share the same machine model (C borrowed C++ 11's memory model), and C++ compilers can do more at compile time, so C++ runs as fast or faster than C in most cases.
- Bjarne's "don't be clever" / "don't be too clever" guidance (from his finance-industry talk): clever 1990s-style micro-optimizations often pessimize today because hardware and compilers have changed.
- His practice: give the optimizer more information with clean, high-level code, and time before optimizing.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language built on this principle
- [[Bjarne Stroustrup]] — its chief advocate
- [[Abstraction]] — the underlying concept
- [[Premature Optimization]] — the error this principle avoids
