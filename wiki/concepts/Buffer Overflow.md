---
title: "Buffer Overflow"
type: concept
tags: [concept, security, memory-safety, vulnerability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md"]
last_updated: 2026-09-23
---
## Definition
A buffer overflow (also called a "buffer overrun") is a memory-safety vulnerability in which a program writes past the bounds of a buffer or array — possible in languages like C that perform no automatic array-bounds checks and allow raw pointer manipulation.

## Key Information
- Simon Peyton Jones identifies buffer overruns, alongside pointer manipulation "gone wrong," as the dominant class of real-world security exploits.
- In C, functions can freely mutate the memory pointed to by raw pointers "anywhere," with no bounds checks, so buffer overruns are possible by construction.
- Most exploits are based on buffer overruns; if buffer overruns were impossible, those exploits "just wouldn't exist."
- Memory-safe languages (Haskell, OCaml, ML) remove this class of bug by construction; modern lower-level languages with array-bounds checking (e.g., Rust with checks enabled) are "much, much better."

## Related
- [[Memory Safety]] — the umbrella property
- [[C (Programming Language)]] — the language prone to buffer overruns
- [[Simon Peyton Jones]] — the speaker making this argument
- [[Rust]] — a lower-level language with bounds checking
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
