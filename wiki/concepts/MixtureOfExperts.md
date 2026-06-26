---
title: "MixtureOfExperts"
type: concept
tags: [architecture, llm, efficiency, moe]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Mixture of Experts (MoE) is a neural network architecture where multiple small feedforward neural networks (experts) are selectively activated by a router during each forward pass, enabling large total parameter counts with only a fraction active at inference time.

## Key Information
- Gemma 4's 26B model uses MoE with one shared router expert (3x size of regular experts) always active, plus 128 total experts with 8 activated per forward pass
- Only 3.9 billion active parameters during any forward pass despite larger total parameter count
- Replaces the standard feedforward neural network in the decoder block with an MoE layer
- Provides significant efficiency gains while maintaining high performance
- First MoE model in the Gemma family

## Related
- [[Gemma4]] — uses MoE in the 26B variant
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
