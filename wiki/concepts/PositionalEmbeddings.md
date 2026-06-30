---
title: "PositionalEmbeddings"
type: concept
tags: [architecture, transformer, llm, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Positional embeddings encode the position of each token in the sequence, allowing the transformer — which has no inherent notion of order — to understand token positions. In Angelos Perivolaropoulos's workshop, the positional embedding table was 256 × 384 = ~98K parameters, matching the model's context window of 256 tokens.

## Key Information
- Transformers have no inherent notion of sequence order; positional embeddings provide this
- Size = block_size × embedding_dim; for the workshop: 256 × 384 = ~98K parameters
- Added to token embeddings before being fed into the transformer blocks
- The block_size (256 in the workshop) is the maximum sequence length the model can process
- Without positional embeddings, the model would treat "The sky is blue" and "blue is sky The" identically
- Modern models use more sophisticated positional encoding schemes like RoPE (Rotary Position Embeddings)
- For the workshop's small model, learned positional embeddings are sufficient

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[EmbeddingLayer]] — combined with token embeddings
- [[TransformerArchitecture]] — overall architecture
- [[RoPE]] — modern alternative for positional encoding
