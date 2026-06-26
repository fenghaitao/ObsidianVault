---
title: "ContextualEmbeddings"
type: concept
tags: [embeddings, rag, vector-databases, retrieval]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Contextual embeddings are a technique where embedding models dynamically adjust their vector representations based on surrounding documents in the database, rather than producing a single universal embedding. This improves retrieval quality, especially for niche or long-tail domains where standard embeddings cluster too tightly.

## Key Information
- Standard embeddings represent only one "universal" sense of semantics, causing related but distinct documents (e.g., Visa vs. MasterCard) to cluster together
- Contextual embeddings feed surrounding documents into the model so it can differentiate between closely related topics
- In the Visa/MasterCard example, contextual embeddings reduced cross-brand similarity from near-indistinguishable to 0.144
- Works as a "free lunch" — adds extra tokens but significantly improves retrieval on long-tail data
- Productionized at OpenAI and other companies for behind-the-scenes embedding improvements
- Less effective on broad/web-scale tasks (e.g., MS Marco) where global embeddings already work well
- Requires a two-stage model architecture and retrieval of surrounding document embeddings at embedding time

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[JackMorris]] — primary researcher
- [[EmbeddingInversion]] — related embedding research
- [[VectorDatabases]] — the storage system they improve
- [[RAG]] — the paradigm they enhance
