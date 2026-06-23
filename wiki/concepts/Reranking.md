---
title: "Reranking"
type: concept
tags: [concept, rag, retrieval, cross-encoder, relevance]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
last_updated: 2026-06-20
---

## Definition

Reranking is a two-step [[RetrievalAugmentedGeneration]] strategy: first pull a *large* set of candidate chunks from the vector database, then use a specialized reranker model (often a cross-encoder) to score and return only the *most relevant* few. [[ColeMedin]] calls it "the first strategy I use for almost every RAG implementation."

## Key Information

- **Two stages**: (1) cheap, broad retrieval pulls many candidates; (2) a reranker model scores each candidate against the query and keeps the top few.
- **Why it helps**: handing an LLM 20-50+ chunks overwhelms it ([[ContextRot]]). Reranking lets you *consider* a broad candidate set but *deliver* only the most relevant chunks — more knowledge considered, less noise passed on.
- **Cross-encoder rerankers** evaluate the query and each chunk together (vs. bi-encoders that embed them separately), giving more accurate relevance scores at higher per-comparison cost.
- **Cost**: a second model in the pipeline adds latency and expense, but Cole considers it modest and worth it for the accuracy gain.
- One of [[ContextualRetrieval]]'s stacking partners — Anthropic's research shows reranking + contextual embedding + [[HybridSearch]] dropping RAG failure rate from ~10% to under 3%.
- **Cole's starter combo**: reranking + agentic RAG + context-aware chunking. Reranking is his most consistently-used RAG strategy.

## Related

- [[RetrievalAugmentedGeneration]] — parent concept
- [[ContextualRetrieval]] — frequently stacked with reranking
- [[HybridSearch]] — complementary (hybrid retrieves broadly, reranking reorders)
- [[ContextRot]] — what reranking avoids (don't dump 50 chunks on the LLM)
- [[ColeMedin]] — advocate
- [[summary-20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff)]] — primary source
