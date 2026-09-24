---
title: "Inlining"
type: concept
tags: [concept, compilers, metaprogramming, optimization]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Inlining is a compile-time construct in which a function call is replaced by the function's body before code generation, revealing the implementation so the compiler can apply guaranteed optimizations and remove call overhead.

## Key Information

- In Scala, writing `inline` before a function makes the compiler, while operating on typed trees, replace each call with the body and then optimize (e.g., forwarding a known lambda's call directly to the target function).
- Unlike an optimizing compiler, which has discretion over whether to inline, a typer-based inliner "must inline," so programmers can rely on it.
- Odersky rates Zig's comptime inlining as nifty, clean, and powerful, versus Rust's macros as more clunky.
- Scala adds a restriction Zig reportedly lacks: no additional type errors may appear after inlining — the failure mode he cites is C++ templates, which can expand into very complex, hard-to-debug type errors.
- Odersky: inlining "reveals the implementation," letting the compiler forward calls (e.g., through a known lambda) and remove function-call overhead — a guaranteed, reliance-worthy compile-time transform rather than a discretionary optimization.

## Related

- [[Scala]]
- [[Zig]]
- [[Rust]]
- [[C++]]
- [[Zero Overhead Abstraction]]
- [[Template Metaprogramming]]
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
