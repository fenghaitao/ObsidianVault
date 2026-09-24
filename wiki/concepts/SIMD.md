---
title: "SIMD"
type: concept
tags: [parallelism, hardware, computer-architecture]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

SIMD (single instruction, multiple data) is a parallel execution model where one instruction operates on many data elements at once; Michael Stonebraker cites it as the reason GPUs are a poor fit for indexing.

## Key Information

- GPUs are SIMD, which Stonebraker calls "the anathema of indexing."
- A B-tree lookup does not parallelize: it is a serial chain of pointer-following memory accesses repeated three or four times.
- Stonebraker's conclusion: "whenever indexing is the right answer, [GPUs are] probably not a good idea."

## Related

- [[summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations]] — source summary
- [[Michael Stonebraker]] — the source of the claim
- [[GPU]] — SIMD hardware
- [[Indexing]] — the technique that does not map to SIMD
- [[Databases]] — the workload under discussion
