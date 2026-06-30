---
title: "EmbeddingLayer"
type: concept
tags: [architecture, llm, tokenization, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
The embedding layer is a lookup table of size vocab_size × embedding_dim that converts token IDs (integers) into dense vector representations (embeddings) that the transformer can process. In Angelos Perivolaropoulos's workshop, the embedding table was 65 × 384 = ~25K parameters — tiny compared to GPT-2's 50K × 384 = 19M parameter embedding table.

## Key Information
- Converts integer token IDs into dense vectors of size embedding_dim
- Size = vocab_size × embedding_dim; for the workshop: 65 × 384 = ~25K parameters
- For GPT-2's 50K token vocabulary, the embedding table alone would be 19M parameters — more than 3× the entire workshop model
- LLMs don't see text; they work with embeddings (vectors), so the embedding layer is the bridge between tokens and the model
- The embedding dimension (384 in the workshop) determines how much information each token can carry
- Larger embedding dimensions carry more information per token but increase parameter count
- The embedding layer is trained along with the rest of the model; embeddings are learned representations
- Combined with positional embeddings before being fed into the transformer blocks

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[PositionalEmbeddings]] — combined with token embeddings
- [[Tokenization]] — produces the token IDs fed to the embedding layer
- [[TransformerArchitecture]] — overall architecture
- [[EmbeddingLayerEfficiency]] — related concept
