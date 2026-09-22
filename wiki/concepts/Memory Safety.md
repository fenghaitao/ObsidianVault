---
title: "Memory Safety"
type: concept
tags: [concept, security, C++, safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Memory safety is freedom from bugs like buffer overflows and use-after-free; a major, often-misunderstood topic in modern C++.

## Key Information
- Bjarne is "so tired" of C++'s unsafe reputation; he says he hasn't had those problems in years and that >90% of buffer-overflow vulnerabilities come from people writing C-style code with raw pointers.
- Modern C++ offers spans (fat pointers with element counts), vectors, and hardened libraries (Apple, Google, and Microsoft all ship them); a hardened mode became standard in C++ 26.
- His "profiles" work provides enforced guidelines as a way to guarantee you don't do "the stupid things" — applicable beyond memory safety, to learning and domain-specific work.
- Theoretically the problem "was solved many years ago"; the gap is practice, education, and enforcement.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language in question
- [[Resource Acquisition Is Initialization (RAII)]] — the lifetime discipline
- [[Herb Sutter]] — provided the vulnerability data
