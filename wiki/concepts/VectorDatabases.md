---
title: "VectorDatabases"
type: concept
tags: [embeddings, storage, rag, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-25
---

## Definition
Vector databases are storage systems that index and retrieve documents based on their embedding vectors (numerical representations produced by LLMs). They are the backbone of RAG systems in production, with many competing implementations offering different cost-performance trade-offs.

## Key Information
- Major implementations include: Chroma, Pinecone, Weaviate, TurboPuffer
- Andrej Karpathy characterized embeddings as "the file system of LLMs" in his OS-for-LLMs diagram
- Store documents as high-dimensional vectors that represent semantic meaning
- Embeddings appear random and unreadable to humans, but can be inverted to recover original text (up to 90% accuracy)
- Standard embeddings are not domain-adaptive — all documents share one universal semantic space
- Contextual embeddings (feeding surrounding documents into the embedding model) improve retrieval on niche data
- Jack Morris argues vector databases/embeddings are "the file system of today, not the future"
- Fundamental limitation: some relationships cannot be captured in fixed-dimensional vectors
- **Semantic Code Search**: Vector databases power semantic code retrieval in coding agents. Turbopuffer, a serverless vector DB on object storage, is used by Cursor for built-in semantic code search. Kuba Rogut benchmarked adding semantic search to Claude Code via TurboGrep + Turbopuffer, finding significant precision improvements. Cursor's A/B tests show 2.6% increase in code retention and 2.2% decrease in dissatisfied requests when semantic search is enabled.
- **Cached Compute**: Kuba Rogut (Turbopuffer) frames embeddings as "cached compute" — an upfront investment in indexing code that pays off by avoiding repeated grep-and-read cycles across sessions and agents

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[RAG]] — the paradigm they power
- [[EmbeddingInversion]] — security vulnerability
- [[ContextualEmbeddings]] — improvement technique
- [[Chroma]] — major implementation
- [[NeuralFileSystem]] — proposed successor paradigm
