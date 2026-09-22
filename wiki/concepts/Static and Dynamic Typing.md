---
title: "Static and Dynamic Typing"
type: concept
tags: [concept, type-systems, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Static typing checks types at compile time; dynamic typing checks them at runtime. The trade-off is early error detection and performance versus flexibility.

## Key Information
- Bjarne chose static typing for C++ because of the problems he attacked: a telephone switch can't drop into a debugger on a runtime error, and you want performance and small programs for memory-constrained embedded systems (99% of computers).
- Runtime resolution requires carrying extra data, which conflicts with fitting into 100k–1MB memories (still relevant for cameras, phones, and battery life).
- Dynamic languages (Python, JavaScript) are easier to start in and popular, but errors the type system would catch appear later at runtime; large systems need far more unit testing because the compiler doesn't check for you.
- Raw Python runs ~70x slower than raw C++; its viability comes from key libraries written in C/C++ — the same "two languages" split Bjarne designed C++ to avoid.
- Guarantees that critical systems (telephone switch, car, plane) must not crash are harder in a flexible dynamic type system.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — a statically typed language
- [[Python]] — a dynamically typed language
