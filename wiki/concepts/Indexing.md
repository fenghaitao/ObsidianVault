---
title: "Indexing"
type: concept
tags: [databases, algorithms, data-structures]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

Indexing is the database technique of using structures like B-trees for fast key lookups; Michael Stonebraker explains why it does not parallelize well and is thus a poor match for SIMD GPUs.

## Key Information

- B-tree example: to find a salary you start at the root, find the divider that brackets both sides, and follow the pointer — a memory access per level, repeated three or four times.
- "Indexing doesn't parallelize well," so SIMD (GPU) execution, which depends on data parallelism, is "the anathema of indexing."
- Consequently, "whenever indexing is the right answer, [GPUs are] probably not a good idea."

## Related

- [[summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations]] — source summary
- [[Michael Stonebraker]] — the source of the explanation
- [[GPU]] — the SIMD hardware that suits it poorly
- [[SIMD]] — why indexing does not parallelize
- [[Databases]] — where indexing is used
