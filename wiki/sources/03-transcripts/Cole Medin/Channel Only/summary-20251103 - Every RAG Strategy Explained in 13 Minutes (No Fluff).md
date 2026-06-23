---
title: "summary-20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff)"
type: source
tags: [source, transcript, rag, retrieval, strategies, neon, postgres]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] surveys 11 [[RetrievalAugmentedGeneration]] strategies in 13 minutes — a deliberate "no fluff" format. Most production RAG systems combine 3-5 of them. Cole's tactical recommendation for getting started: **reranking + agentic RAG + context-aware chunking** (specifically hybrid chunking via Docling). Demonstrates each strategy with pseudocode against a Postgres+`pgvector` setup ([[Neon]] sponsor); links to a GitHub repo with full implementations.

## Key Points

The 11 strategies, each with one-line essence:

| # | Strategy | Essence | Cost |
|---|---|---|---|
| 1 | **Reranking** | Pull a large candidate set, rerank with a cross-encoder, return top few. | Slight extra latency + small model cost |
| 2 | **Agentic RAG** | Agent picks how to search (semantic, full-doc fetch, etc.) per query. | More LLM calls; less predictable |
| 3 | **Knowledge Graph RAG** | Store entities/relationships in a graph DB alongside vector search. Cole's library: **Graphiti**. | Slow + expensive ingest (LLM-driven extraction) |
| 4 | **[[ContextualRetrieval]]** | Per-chunk LLM-generated context prepended at ingest time. From [[Anthropic]]. | Per-chunk LLM call (mitigated by [[PromptCaching]]) |
| 5 | **Query Expansion** | Single LLM call rewrites the user's query before search. | One extra LLM per query |
| 6 | **Multi-Query RAG** | LLM generates N variants, search in parallel. | N retrievals + LLM call |
| 7 | **Context-Aware Chunking** | Split documents at natural boundaries (embedding model finds them). Cole's library: **Docling** (hybrid chunking). | Higher complexity vs fixed-size chunking |
| 8 | **Late Chunking** | Embed the whole document first, then chunk the token embeddings. Each chunk retains full-doc context. | Most complex; Cole hasn't used it yet |
| 9 | **Hierarchical RAG** | Parent-child chunk relationships in metadata; search small, return big. Variant of agentic RAG. | More metadata + agent decisions |
| 10 | **Self-Reflective RAG** | LLM grades retrieved chunks (1-5); if low, retry with refined query. | One extra LLM per search; sometimes more |
| 11 | **Fine-Tuned Embeddings** | Train a domain-specific embedding model. 5-10% accuracy gain. | Training data + ongoing infra |

- **Three-to-five-combination heuristic.** No single strategy dominates; production systems stack 3-5.
- **Cole's starter combo for new RAG agents**: reranking + agentic RAG + context-aware chunking (with Docling).
- **Docling + hybrid chunking** is Cole's current favorite chunker for production work.
- **Sentiment vs semantic embeddings** — Cole's example for fine-tuning: "my order was late" being similar to "shipping was fast" (semantic) vs. "items are always sold out" (sentiment-trained). Different training data, different similarity space.

## Related

- [[RetrievalAugmentedGeneration]] — base concept
- [[ContextualRetrieval]] — strategy #4, has its own page
- [[ColeMedin]] — author
- [[Neon]] — sponsored Postgres/pgvector backend used in demos
- [[Crawl4AIRAG]] — Cole's open-source MCP that implements several of these
