---
title: "HybridSearch"
type: concept
tags: [concept, rag, retrieval, bm25, semantic-search]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
last_updated: 2026-06-20
---

## Definition

Hybrid search is a [[RetrievalAugmentedGeneration]] strategy that combines **semantic (vector) search** with **keyword (BM25) search**. Vector search captures meaning; keyword search captures exact terms. Together they improve recall — especially for rare terminology, proper nouns, and exact-match cases that pure semantic similarity misses.

## Key Information

- **Vector search alone** struggles with rare or out-of-distribution terms (an obscure API name, a specific error code) because the embedding may not place them near the query.
- **BM25 keyword search** catches exact lexical matches that vector search overlooks.
- **Combined (hybrid)**, you get the semantic generalization *and* the lexical precision — fewer failed retrievals.
- Part of [[Anthropic]]'s [[ContextualRetrieval]] research: hybrid search is one of the techniques that, stacked with contextual embedding and [[Reranking]], drives RAG failure rate from ~10% to under 3%.
- One of the 11 strategies in Cole's RAG survey (see [[RetrievalAugmentedGeneration]]). Typically combined with 2-4 others; rarely used alone.

## Related

- [[RetrievalAugmentedGeneration]] — parent concept
- [[ContextualRetrieval]] — frequently stacked with hybrid search
- [[Reranking]] — complementary technique (hybrid retrieves, reranking reorders)
- [[ColeMedin]] — surveyed it
- [[summary-20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff)]] — primary source
