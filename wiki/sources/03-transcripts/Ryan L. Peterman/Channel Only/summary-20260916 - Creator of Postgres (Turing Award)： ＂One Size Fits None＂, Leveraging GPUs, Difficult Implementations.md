---
title: "summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Core Summary

Michael Stonebraker reiterates his "one size fits none" thesis: a general-purpose database gives up an order of magnitude versus an engine architected for a specific workload, so Postgres is only the right default at the low end. He walks through the 2004 paper — StreamBase's stream engine, Vertica's column store, and row stores — and argues ClickHouse and Pinecone still prove the point today, while Postgres's lack of a column store and multi-node support leaves it uncompetitive on sizable data warehouses. On GPUs, he explains they are SIMD, "the anathema of indexing," because a B-tree lookup is a serial chain of memory accesses that does not parallelize, and warns that a GPU bolted onto a CPU often bottlenecks on the connecting bus. He recalls writing the original Ingres from scratch and names the query optimizer the hardest, most algorithmically difficult part.

## Key Points

- One size fits none: stream processing, column stores, and row stores are "wildly different implementations" with no resemblance to each other, each an order of magnitude faster for its own workload.
- The exception is the low end, where Postgres is the right default — free, huge community, easy talent — until you need roughly a million transactions a second or a petabyte-scale warehouse.
- Postgres does not implement a column store and lacks multi-node support, so it is not competitive on sizable data warehouses.
- The thesis still holds: ClickHouse is a column store, and Pinecone beats user-defined types on text-based vector processing; a common parser can sit on top of multiple implementations.
- GPUs are SIMD (single instruction, multiple data), which is "the anathema of indexing"; walking a B-tree is a chain of three or four memory accesses that does not parallelize well.
- When a GPU is an add-on to the CPU, the bus between GPU and CPU is often the bottleneck; storage bandwidth must also not become the bottleneck.
- The original Ingres was written entirely from scratch (there was no existing B-tree library), and the hardest part was the query optimizer — "algorithmically difficult."

## Related

- [[Michael Stonebraker]] — guest
- [[Ryan L. Peterman]] — host
- [[PostgreSQL]] — his open-source database
- [[One Size Does Not Fit All]] — his core thesis
- [[Databases]] — the field
- [[Query Optimizer]] — the hardest part to implement
- [[Ingres]] — written from scratch
- [[StreamBase]] — stream-engine example
- [[Vertica]] — column-store example
- [[ClickHouse]] — modern column store
- [[Pinecone]] — modern vector database
- [[GPU]] — SIMD hardware
- [[SIMD]] — why GPUs struggle with indexing
- [[Indexing]] — the technique GPUs are bad at
- [[Column Store]] — the specialized storage layout
