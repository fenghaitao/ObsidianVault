---
title: "Recall@50"
type: concept
tags: [evaluation, retrieval, embeddings, metrics, code-generation, multi-document]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou.md"]
last_updated: 2026-06-26
---

## Definition
Recall@50 is a multi-document retrieval evaluation metric that measures what fraction of ground-truth relevant documents appear in the top 50 items retrieved. Unlike single-document "needle in a haystack" benchmarks, Recall@50 captures the real-world requirement of retrieving multiple relevant context items simultaneously for tasks like code generation.

## Key Information
- **Formula**: Fraction of ground-truth relevant documents found within top 50 retrieved results
- **Motivation**: Traditional embedding benchmarks evaluate single-document retrieval (one "needle"), but real code generation requires multiple context sources simultaneously (design system components, style guides, similar files, documentation)
- **Codeium's Application**: Used to evaluate retrieval quality for AI code generation, where the query maps to a set of files relevant to a given change
- **Ground Truth Construction**: Codeium built datasets from real PR commit messages mapped to the files modified in those commits, creating a product-driven eval set
- **Advantage over Single-Document Metrics**: Tests whether the retrieval system can surface all necessary context, not just one relevant item
- **Contrast with Embedding Benchmarks**: Standard embedding benchmarks (like MTEB) have been plateauing with models approximating similar performance (±5%), partly because they don't measure multi-document retrieval capability

## Related
- [[summary-20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou]] — source
- [[Product-Driven Benchmarks]] — broader evaluation philosophy
- [[Embedding Ceiling]] — the performance plateau motivating better metrics
- [[BenchmarkSaturation]] — related concept of benchmarks hitting ceilings
- [[RAG]] — retrieval augmented generation
