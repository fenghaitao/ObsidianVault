---
title: "AudioTokenizer"
type: concept
tags: [audio, speech, preprocessing, multimodal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
An Audio Tokenizer processes raw audio into soft tokens by running audio through a mel spectrogram, splitting into mel chunks, and downsampling through convolutional layers to produce audio embeddings for downstream processing.

## Key Information
- Used in Gemma 4's E2B and E4B models for audio input processing
- Pipeline: raw audio → mel spectrogram (feature extraction) → N mel chunks → two convolutional layers (downsampling) → N/4 soft tokens
- Output audio embeddings are passed to the conformer for further processing
- Enables speech recognition and translation capabilities on-device

## Related
- [[Gemma4]] — uses audio tokenizer in E2B/E4B
- [[Conformer]] — downstream audio processor
- [[MultimodalModels]] — broader context
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
