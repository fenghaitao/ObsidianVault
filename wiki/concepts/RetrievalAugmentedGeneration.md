---
title: "RetrievalAugmentedGeneration"
type: concept
tags: [concept, rag, retrieval, vector-search, llm]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
last_updated: 2026-06-19
---

## Definition

Retrieval-Augmented Generation (RAG) is a pattern where an LLM's response is grounded by retrieved external documents, rather than relying purely on the model's training data. The standard pipeline: ingest documents → split into chunks → embed each chunk into a vector → store in a vector database → at query time, embed the user's question, fetch the nearest-neighbor chunks, and prepend them to the LLM prompt.

## Key Information

### Standard pipeline

```
Documents → Chunker → Embedder → Vector DB
                                    ↑
User query → Embedder → Vector DB ──┘
              → top-K chunks → prepended to LLM prompt → answer
```

### RAG in Archon (specific use)

[[Archon]] uses RAG to keep its [[PydanticAI]] (and, in v7+, [[LangGraph]]) code generation grounded in current framework docs:

- Documentation is crawled and chunked.
- Chunks are embedded and stored in [[Supabase]] with `pgvector`.
- The Coder agent, when generating code for a user request, retrieves the most relevant doc chunks and uses them to ground the generated code (avoids hallucinating API surfaces that don't exist).

This is the difference Cole highlights between [[Windsurf]]'s `@PydanticAI` doc retrieval (basic RAG with general-purpose embeddings) and Archon's curated RAG (deeper chunking, framework-specific configuration).

### Advanced techniques on Archon's roadmap (v12)

Cole calls out these as planned improvements:

| Technique | Purpose |
|---|---|
| **Hybrid search** | Combine vector similarity with keyword (BM25) search for better recall on rare terms |
| **Reranking** | Take top-K from initial retrieval, then re-rank with a stronger model |
| **Query decomposition** | Split a complex query into sub-queries, retrieve for each, merge |
| **Hierarchical chunking** | Multi-level chunks (sentence + paragraph + section) for context-appropriate retrieval |

### Cole's broader stance: RAG as data-engineering problem

A recurring theme across Cole's content (echoed in the Vectorize sponsor segment in video 1): the hard part of RAG isn't the LLM call — it's the **pipeline**. Getting documents from where they live (Drive, GitHub, Notion, etc.) into a usable vector store with proper chunking and metadata is where most projects fail or burn time.

### Vector DB choices Cole references

- **[[Supabase]]** — Archon's default. Postgres-friendly, free, self-hostable.
- **Qdrant** — faster than Supabase, also self-hostable.
- **Pinecone** — serverless, very fast, not open source.
- **Weaviate**, **Chroma** — also mentioned as popular options.

## Knowledge Conflicts

> **RAG vs. agent-side reading.** The Karpathy-style LLM-Wiki philosophy underpinning this knowledge base is *opposed* to vanilla RAG (it favors "compile knowledge once into structured wiki pages"). Cole's use of RAG inside Archon, however, is for ephemeral framework-doc grounding during code generation — a different use case. The two views are compatible: use RAG for ephemeral retrieval over high-volume reference material; use compiled wiki pages for distilled, reusable knowledge.

## Related

- [[Archon]] — uses RAG over PydanticAI docs
- [[Supabase]] — Archon's vector DB backend
- [[PydanticAI]] — the framework whose docs are RAG-indexed
- [[ColeMedin]] — frequent advocate of robust RAG pipelines
- [[ToolUse]] — agents can also expose RAG as a tool rather than building it into the prompt
