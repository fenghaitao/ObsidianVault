---
title: "Template Metaprogramming"
type: concept
tags: [concept, C++, templates, compile-time]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Template metaprogramming is computation performed by the C++ compiler through template instantiation, before the program runs.

## Key Information
- Templates turned out to be Turing complete; early examples computed prime numbers and factorials at compile time (reporting results via error messages).
- Bjarne saw this as "useful" rather than banning it, but considered factorial-style template tricks "awful," expensive, and memory-hungry.
- With Gabriel Dos Reis, he built `constexpr` to do compile-time calculation in ordinary, familiar code — simpler and faster to compile — along with `consteval` to guarantee compile-time evaluation.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Turing Completeness]] — the property templates exhibited
- [[C++]] — the language involved
