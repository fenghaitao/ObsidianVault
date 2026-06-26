---
title: "RoPE"
type: concept
tags: [architecture, positional-encoding, attention, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition
Rotary Position Embeddings (RoPE) encode positional information into transformer attention by applying rotation operations (cosine/sine transformations) to query and key vectors, enabling the model to learn the relative position of tokens within a sequence.

## Key Information
- Replaces older absolute position encodings where a position index (e.g., 0, 1, 2) was simply added to embeddings
- Applies rotation via trigonometric functions (cosine and sine) to Q and K vectors, encoding relative position information
- The RoPE paper showed improved accuracy compared to absolute position encodings
- RoPE is now standard practice across virtually all modern LLMs
- Extending context length with RoPE: multiplying the base frequency by a factor (e.g., 2x) can extend context length proportionally, though models only trained at shorter lengths (e.g., 4K) face degradation
- Methods like YaRN address the gap between training length and target context length (e.g., 1M tokens) when using RoPE
- RoPE embeddings are applied before the QK^T computation in the attention mechanism

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[SelfAttentionMechanism]] — attention mechanism using RoPE
- [[GroupedQueryAttention]] — attention variant also using RoPE

- **ModernBERT adaptation**: Uses different rotation speeds for local attention (faster rotation) and global attention (slower rotation) to avoid completing full cycles that would make distant tokens appear close
- **Continuous context window**: Unlike absolute positional encodings, RoPE's context window is continuous and only limited by geometry, not training size