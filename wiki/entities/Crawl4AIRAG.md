---
title: "Crawl4AIRAG"
type: entity
tags: [tool, mcp-server, rag, open-source, cole-medin]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"
last_updated: 2026-06-19
---

## Definition

Crawl4AI-RAG is [[ColeMedin]]'s open-source [[ModelContextProtocol]] server that crawls websites, builds a private RAG knowledge base, and exposes RAG queries as MCP tools. He recommends it as one of the "3 must-have MCP servers" for AI coding — specifically, the documentation-RAG slot.

> The "Crawl4AI" in the name refers to the underlying Python library Cole uses for the actual crawling step, not a separate tool.

## Key Information

### What it does

1. **Crawl**: takes a starting URL (typically a docs site like [[PydanticAI]]'s or [[Supabase]]'s) and walks the site, extracting clean markdown.
2. **Chunk + embed**: splits each page into chunks, applies [[ContextualRetrieval]] (per-chunk LLM-generated context), embeds with OpenAI's `text-embedding-3-small`.
3. **Store**: persists vectors to a self-hosted [[Supabase]] (`pgvector`) instance.
4. **Expose**: registers a `perform_rag_query` MCP tool that any MCP client can call.

The result: any MCP-aware AI IDE ([[Cursor]], [[Windsurf]], Cline) can query Cole's curated knowledge bases for framework docs while generating code, without hallucinating APIs.

### Why Cole built it

Existing options Cole considered insufficient:
- **Built-in IDE doc retrieval** (Windsurf's `@PydanticAI`, Cursor's `@docs`): generic chunking, shallow integration, frequently misses what the model actually needs.
- **Context7**: solid, has thousands of pre-ingested libraries, but you don't control what's in it or how it's chunked.

Crawl4AI-RAG is the "build my own knowledge base" answer: you decide what to crawl, you control the chunking strategy, you own the data, and the RAG pipeline includes [[ContextualRetrieval]] for accuracy.

### Connection to [[Archon]]

Cole has stated [[Archon]] (his AI-agent-builder) will integrate Crawl4AI-RAG as its underlying knowledge layer. Archon's existing RAG over PydanticAI docs is moving toward this server. Once that lands, Archon's coder agent benefits from Crawl4AI-RAG's contextual-retrieval-enhanced lookups.

### Role in Cole's "3 MCP" stack

In [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]], Cole's recommended MCP server triad:

| Slot | Cole's pick |
|---|---|
| Documentation RAG | **Crawl4AI-RAG** (this) |
| Database management | [[Supabase]] MCP |
| Web search | Brave MCP |

The pairing of Crawl4AI-RAG (curated, deep) + Brave (web, broad) is Cole's standard pattern: query private docs first, fall back to web search for examples and edge cases.

### Reference implementation for [[ContextualRetrieval]]

`utils.py` in this repo contains `generate_contextual_embeddings()` — the canonical Python implementation Cole points to as the example others can copy. Worth reading as a concrete companion to the abstract description in [[ContextualRetrieval]].

## Related

- [[ColeMedin]] — author
- [[ModelContextProtocol]] — protocol Crawl4AI-RAG implements
- [[ContextualRetrieval]] — RAG enhancement built into the server
- [[RetrievalAugmentedGeneration]] — base pattern
- [[Supabase]] — vector store
- [[Archon]] — planned integration
- [[Cursor]], [[Windsurf]] — primary client surfaces
- [[summary-20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)]] — feature deep-dive
- [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]] — recommendation context
