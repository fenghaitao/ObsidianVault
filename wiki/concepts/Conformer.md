---
title: "Conformer"
type: concept
tags: [architecture, audio, speech, transformer, convolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
A Conformer is an audio encoder architecture that combines transformer layers with convolutional layers, used in Gemma 4's E2B and E4B models for processing audio embeddings to support translation and speech recognition.

## Key Information
- 305 million parameter conformer used in Gemma 4's E2B and E4B
- Processes audio embeddings (not tokens) output from the audio tokenizer
- Architecture follows a similar pattern to dense models and MoE but adds convolutional layers
- Enables on-device audio capabilities including translation and speech recognition

## Related
- [[Gemma4]] — uses conformer in E2B/E4B
- [[AudioTokenizer]] — feeds embeddings into the conformer
- [[MultimodalModels]] — broader context
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
