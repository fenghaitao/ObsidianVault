---
title: "EmbeddingInversion"
type: concept
tags: [embeddings, security, vector-databases, privacy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Embedding inversion is the technique of recovering original text from vector embeddings stored in vector databases. Jack Morris's PhD research demonstrated that up to 90% of text can be recovered exactly from embeddings, eliminating any security benefits of storing only embeddings.

## Key Information
- Morris's research showed that embeddings are analogous to text — they can be read back with a properly constructed system
- The technique uses a multi-round correction process to iteratively reconstruct original text from embeddings
- At certain text lengths, 90% of original text can be recovered exactly
- This means vector databases provide no inherent security benefit over storing plain text
- Many vector database architectures (TurboPuffer, Pinecone) store only embeddings, creating a false sense of security
- Even a "slightly motivated person" can build a system to recover text from embeddings

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[JackMorris]] — primary researcher
- [[VectorDatabases]] — the target of this attack
- [[RAG]] — paradigm that relies on vector databases
