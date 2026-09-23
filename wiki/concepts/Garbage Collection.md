---
title: "Garbage Collection"
type: concept
tags: [concept, memory-management, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---
## Definition
Garbage collection is automatic reclamation of unreachable memory; C++ supports it optionally but does not require it.

## Key Information
- Early high-level languages often required garbage collection, which is poor for device drivers (or for building collectors) — so Bjarne avoided requiring it in C++.
- In 1995 the standards committee (led by Hans Boehm, who has a conservative collector) wanted a standard interface; one was added to C++ 11 so GC use could be standardized.
- Over the next ~10 years usage declined as RAII became better understood; today only a few use GC, and it's no longer part of the standard.
- Mechanically it wraps the allocation/deallocation primitives (`new`, `delete`, `operator new`, `malloc`).
- OCaml's low-latency allocator/GC avoids long pauses, which matters for network programming; Cornell's Ensemble project even ran the GC while network packets were in flight.
- GC has runtime overhead (~10–30% in some applications) because it scans memory at run time, but it enables cheap, safe sharing of data structures — manual memory management is not always faster.
- Heap allocation is cheap for short-lived objects (they die before the next collection); that is why stack allocation wins less than expected for them.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — supports it optionally
- [[Resource Acquisition Is Initialization (RAII)]] — the preferred discipline
- [[Hans Boehm]] — its main advocate in standardization
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[OCaml]] — low-latency GC user
- [[Manual Memory Management]] — the contrasting model
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
