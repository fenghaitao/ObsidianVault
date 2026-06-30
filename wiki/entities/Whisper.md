---
title: "Whisper"
type: entity
tags: [model, speech-to-text, openai, stt, audio, transcription]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-30
---

## Definition
Whisper is OpenAI's canonical speech-to-text model, released in 2022. It was trained on 30-second audio clips as a batch model, making it the reference point for STT architecture from which the industry is now evolving toward streaming-native models for voice agent use cases.

## Key Information
- Released by [[OpenAI]] in 2022
- Trained on 30-second audio clips — a batch architecture, not streaming-native
- 30-second latency is too high for voice agents, requiring complex workarounds: chunking audio, padding with silences, making multiple calls, and stitching transcripts together
- Served as the canonical STT model for several years
- Now being superseded by streaming-native architectures (e.g., Nvidia's recent model with look-ahead time and cached encoder activations)
- Used as the base for dictation tools like [[WhisperFlow]] and [[Super Whisper]]

## Related
- [[OpenAI]] — creator
- [[Streaming ASR]] — the architectural evolution beyond Whisper
- [[WhisperFlow]] — dictation tool built on Whisper
- [[Super Whisper]] — another dictation tool
- [[Word Error Rate]] — quality metric
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
