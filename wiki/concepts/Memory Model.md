---
title: "Memory Model"
type: concept
tags: [concurrency, programming-languages, memory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

A memory model is the set of guarantees a programming language gives programmers about the ordering and visibility of concurrent reads and writes to shared memory, needed once a language exposes shared-memory concurrency.

## Key Information

- Shared-memory concurrency (threads communicate by modifying shared memory) is a model Xavier Leroy never liked; he prefers message passing (as in Erlang), but it requires copying data and partly lost out to shared memory's cheap sharing.
- Once a language exposes shared memory, races must be defined: C/C++ often say "undefined behavior," while sequential consistency (some interleaving of reads/writes) is too strict for modern CPUs that reorder memory accesses.
- Java went through roughly five memory-model iterations (some too strict, some too lax, some inconsistent, with "the past depends on the future"); C/C++11 did better but remains extremely complex.
- Adding multicore to OCaml (2022) required both rewriting the GC/allocator and agreeing on a memory model; OCaml's is easier to understand than Java's but still complicated.
- In type-safe languages (Java, OCaml) the memory model must also guarantee data stays well-typed — e.g., not exposing an object to another thread before it is fully initialized — which is hard and requires compiler precautions.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[OCaml]] — the language whose memory model was settled for multicore
- [[Concurrency]] — the broader subject
- [[C (Programming Language)]] — whose undefined-behavior races complicate the model
- [[Type System]] — type safety under concurrency is the hard part
