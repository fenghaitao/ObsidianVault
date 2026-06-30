---
title: "Word Error Rate"
type: concept
tags: [speech-to-text, stt, quality, metrics, evaluation, voice-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Word Error Rate (WER) is the primary quality metric for speech-to-text systems, measuring the percentage of words in a transcription that contain errors when compared to a reference transcript. State-of-the-art models achieve approximately 6% WER on open benchmarks.

## Key Information
- WER = (substitutions + insertions + deletions) / total words in reference × 100%
- State-of-the-art models: ~6% WER on open benchmarks
- Errors in STT compound through the entire voice agent pipeline — the LLM and TTS will both carry forward mistakes
- Getting keywords right (names, drug names, product names) is especially critical; there is no way to fix errors downstream
- WER requirements vary by use case — medical transcription demands much lower WER than casual conversation
- Benchmark WER may not reflect domain-specific performance

## Related
- [[Voice Agent Pipeline Architecture]] — STT is the first stage
- [[Streaming ASR]] — architectural approach to reduce latency while maintaining quality
- [[Turn Detection]] — another STT quality capability
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
