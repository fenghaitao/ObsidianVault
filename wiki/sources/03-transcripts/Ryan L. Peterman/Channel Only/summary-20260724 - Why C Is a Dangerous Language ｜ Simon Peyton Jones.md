---
title: "summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md"]
last_updated: 2026-09-23
---
## Core Summary
Simon Peyton Jones argues that C is a dangerous ("unsafe") language because any function can mutate any memory at any time through unconstrained raw pointers, with no array-bounds checks — which makes buffer overruns and flawed pointer manipulation the root cause of most security exploits on the internet. Writing the world's software infrastructure and operating systems in memory-safe languages such as Haskell, OCaml, or ML would eliminate roughly 99% of these exploits "by construction," and modern lower-level languages like Rust are "much, much better" than C.

## Key Points
- C is unsafe because any function can mutate any variable or memory at any time: programmers pass pointers around freely and functions mutate the memory they point to, "anywhere," with no array-bounds checks — "super unsafe."
- The internet is insecure primarily because software infrastructure and operating systems are written in unsafe languages such as C.
- If internet software and operating systems had been written in Haskell, OCaml, or ML, ~99% of these exploits would be "removed by construction."
- Analogy: relying on C for secure infrastructure is "like building a boat out of paperclips" and being surprised it leaks, then spending enormous human effort and money patching the holes.
- Most exploits trace to buffer overruns or pointer manipulation gone wrong; without buffer overruns, those exploits "just wouldn't exist."
- Microsoft's MSRC (Microsoft Security Response Center) discovers such exploits "in huge numbers," illustrating the daily toll of memory-unsafety.
- On modern lower-level languages: Rust is "much, much better"; SPJ is unsure whether Rust's array-bounds checks are on by default, but compiling with them enabled puts you in a "way better situation."
- SPJ clarifies this is about more than functional programming — it is his reason for calling C an insecure, unsafe language.

## Related
- [[Simon Peyton Jones]] — guest and speaker
- [[C (Programming Language)]] — the unsafe language he critiques
- [[Rust]] — the safer modern lower-level alternative
- [[Memory Safety]] — the core concept
- [[Buffer Overflow]] — the exploit class he highlights
- [[Programming Language Design]] — safe vs unsafe language design
- [[Functional Programming]] — the paradigm he qualifies the point against
- [[Haskell]] — a language that would remove exploits "by construction"
- [[OCaml]] — another safe alternative he names
- [[ML (Programming Language)]] — another safe alternative he names
- [[Microsoft]] — MSRC's exploits
