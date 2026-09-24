---
title: "GPU"
type: entity
tags: [hardware, parallelism, simd]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

A GPU (graphics processing unit) is a massively parallel, SIMD-style processor that Michael Stonebraker discusses for accelerating databases, with caveats around indexing and bandwidth.

## Key Information

- GPUs are SIMD (single instruction, multiple data), which Stonebraker calls "the anathema of indexing."
- Whenever indexing is the right answer for a database workload, GPUs are "probably not a good idea."
- When a GPU is an add-on to the CPU, the bus connecting the GPU to the CPU is often the bottleneck; storage bandwidth also must not become the bottleneck.

## Related

- [[summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations]] — source summary
- [[Michael Stonebraker]] — discusses their fit for databases
- [[SIMD]] — the execution model behind the caveat
- [[Indexing]] — the technique GPUs are bad at
- [[Nvidia]] — a GPU maker
- [[Databases]] — the workload being accelerated
