---
title: "ResidualConnections"
type: concept
tags: [architecture, training, stability, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Residual connections are a mechanism in transformer architectures where each layer's output is added to its input (X = X + layer_output) rather than replacing it entirely. This prevents each layer from having to "reinvent" the activations from scratch, keeping training stable across many layers.

## Key Information
- Instead of X = attention(X), the pattern is X = X + attention(X) — the layer adds a delta rather than replacing
- Prevents each transformer layer from completely restarting the activations from scratch
- Each layer makes a small adjustment to the previous representation rather than a wholesale change
- Makes training more stable across many layers by preventing drastic changes to activations
- Part of the standard transformer block: layer norm → attention → residual add → layer norm → MLP → residual add
- Works in conjunction with layer normalization to keep activations in a stable range
- Without residuals, deep networks suffer from vanishing/exploding gradients and training instability

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LayerNorm]] — paired normalization technique
- [[TransformerArchitecture]] — overall architecture
- [[LLMTrainingFromScratch]] — workshop context
