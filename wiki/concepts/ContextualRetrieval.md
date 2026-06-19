---
title: "ContextualRetrieval"
type: concept
tags: [concept, rag, retrieval, anthropic, embedding]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
last_updated: 2026-06-19
---

## Definition

Contextual retrieval (a.k.a. contextual embedding) is a [[RetrievalAugmentedGeneration]] enhancement introduced by [[Anthropic]] that prepends each chunk with LLM-generated context describing the chunk's place within its source document. The LLM consuming retrieved chunks then "knows where it's reading from" without having to back out and fetch the surrounding context.

## Key Information

### The pattern

For each chunk produced by your chunker:

1. Run a small/cheap LLM call with: the **whole document** + **this specific chunk** + a 1-2 sentence prompt asking for context positioning the chunk.
2. Prepend the LLM's response to the chunk (separated by a delimiter like `---`).
3. Embed the augmented chunk and store as usual.

The exact prompt from Anthropic's article (used verbatim by [[ColeMedin]]):

> Here is the chunk we want to situate within the whole document:
> `<chunk>`
> Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.

At retrieval time, no change — just embed the user's query and find nearest chunks. The augmented chunks include their own context, so retrieved chunks are immediately useful to the answering LLM.

### Why it works

A bare chunk like *"Progress is 72% complete against the 85% target"* tells the answering LLM nothing about *what* is 72% complete. With contextual retrieval, that chunk is prefixed with *"This chunk details the development status of the neural adaptation engine in the Q1 2024 quarterly report"* — and the answer becomes obvious. Retrieval was already finding the right chunk; the augmentation makes the chunk *useful once retrieved*.

### Anthropic's evaluation results

| Configuration | Failure rate (chunks not retrieved) |
|---|---|
| Basic RAG | 9.9% |
| + Contextual embedding | ~6.5% (-35%) |
| + All techniques combined | <3% |

A ~35% reduction in failures from contextual embedding alone, before adding [[HybridSearch]] or [[Reranking]].

### Cost concerns and [[PromptCaching]]

**The naïve concern**: contextual retrieval runs N extra LLM calls (one per chunk), each containing the entire document. For a 10K-chunk corpus that sounds expensive.

**The mitigation**: prompt caching. The document is repeated across every chunk's prompt, so providers cache it. Cole's data:
- OpenAI: 50% cheaper for cached input tokens (automatic, on by default).
- Anthropic & Gemini: ~90% cheaper for cached input tokens (toggle in API request).

Combined with using a cheap model for this step (GPT-4o-mini, GPT-4.1-nano), the per-document cost is small.

### Implementation references

- **[[N8N]]** — Cole's published workflow uses a JavaScript chunker + a per-chunk LLM node + Postgres (`pgvector`) storage on [[Neon]] or [[Supabase]].
- **Python** — `generate_contextual_embeddings` in Cole's [[Crawl4AIRAG]] MCP server (`utils.py`).

### Related techniques (compound effect)

These appear in Anthropic's article and combine multiplicatively with contextual retrieval:
- **[[HybridSearch]]** — vector similarity + BM25 keyword search; helps with rare terminology and exact-match cases that pure semantic search misses.
- **[[Reranking]]** — fetch top-K with cheap retrieval, then re-rank with a stronger model; trades a small per-query cost for better relevance ordering.
- **Query decomposition** — split a complex query into sub-queries, retrieve for each, merge.

## Related

- [[RetrievalAugmentedGeneration]] — base pattern this enhances
- [[Anthropic]] — original article author
- [[PromptCaching]] — required for cost-effective implementation
- [[HybridSearch]] / [[Reranking]] — complementary techniques
- [[Crawl4AIRAG]] — Cole's reference Python implementation
- [[N8N]] — visual implementation surface
- [[ColeMedin]] — implementer/teacher
- [[summary-easiest-strategy-for-accurate-rag]] — primary source
