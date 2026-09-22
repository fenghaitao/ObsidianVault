---
title: "Generic Programming"
type: concept
tags: [concept, programming-paradigm, C++, templates]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Generic programming is a paradigm where algorithms and data structures are written in terms of types specified later, using templates and type constraints.

## Key Information
- C++'s merge of Simula classes with C, plus a more regular type system, "gets us to generic programming eventually many years later."
- Overloading is "essential for generic programming": to write e.g. a `vector<T>` you must call the same operations on many types sharing an interface.
- `auto` was the beginning of concepts — the simplest constraint (it must be a type) — and formal concepts add constraints to generic code.
- The STL (Alex Stepanov) is generic programming's landmark C++ embodiment.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language supporting it
- [[Standard Template Library (STL)]] — its landmark standard library
- [[Alex Stepanov]] — its pioneer
