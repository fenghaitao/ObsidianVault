---
title: "summary-20260609 - RAG is dead, right — Kuba Rogut, Turbopuffer"
type: source
tags: [source, transcript, rag, semantic-search, agentic-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260609 - RAG is dead, right — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Core Summary

Kuba Rogut from Turbopuffer argues RAG isn't dead — it's evolving into hybrid tool-rich retrieval. Semantic search acts as "cached compute": upfront indexing cost amortized across sessions. Cursor sees 24% accuracy improvement from semantic search. Claude Code's agentic grep approach works but misses what semantic search provides.

## Key Points

- RAG search volume on Google hit new inflection point mid-2025 — opposite of "RAG is dead" narrative.
- RAG = retrieval (vector, full-text BM25, grep, glob, regex, filters) + augmented generation (LLM).
- Agentic search = giving agents tools to progressively find and reason over context, not just file system grep.
- Cursor: Merkle tree-based codebase indexing, semantic search yields 12-13% accuracy improvement across models, 24% for Composer.
- Embeddings as "cached compute": upfront cost, but saves tokens and time across all sessions.
- Claude Code uses agentic grep, not semantic search — Boris said early versions tried vector DB but it "didn't work out."

## Related

- [[KubaRogut]] — speaker, Turbopuffer
- [[Turbopuffer]] — vector + full-text search database
- [[RAG]] — retrieval augmented generation
- [[SemanticCodeRetrieval]] — semantic search for code
- [[Cursor]] — code editor using semantic search
- [[ClaudeCode]] — agentic grep approach
