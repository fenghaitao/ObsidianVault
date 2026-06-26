---
title: "SlidingWindowAttention"
type: concept
tags: [architecture, attention, efficiency, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition
Sliding Window Attention is an attention mechanism where each token attends only to a fixed number of immediately preceding tokens (the window), rather than all preceding tokens, providing significant efficiency improvements for local attention layers.

## Key Information
- Used in Gemma 4's local attention layers within the interleaved local/global pattern
- Window size: 512 tokens for smaller models (E2B, E4B), 1,024 tokens for larger models (31B, 26B)
- Provides significant efficiency and optimization improvements over full attention
- Information still passes through to subsequent layers despite limited local context
- Contrasts with global layers that attend to all preceding tokens

## Related
- [[Gemma4]] — uses sliding window in local layers
- [[InterleavedLocalGlobalAttention]] — broader attention pattern
- [[GroupedQueryAttention]] — complementary optimization
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source

- **ModernBERT local attention**: Uses 128-token sliding window (64 left + 64 right) in alternating attention pattern, capturing locally concentrated attack patterns like gibberish suffixes and short prompt injections