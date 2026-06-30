---
title: "Voice Chat (Nvidia)"
type: entity
tags: [model, speech-to-speech, nvidia, voice-ai, full-duplex]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Voice Chat is a speech-to-speech model recently launched by Nvidia. Like OpenAI's real-time API, it uses a single model behind the scenes to handle speech input and output directly, though it still struggles with instruction following and tool calling — common limitations of speech-to-speech models in production.

## Key Information
- Speech-to-speech model from [[Nvidia]]
- Single model architecture (no separate STT/LLM/TTS components)
- Similar approach to OpenAI's real-time API
- Current limitations: instruction following and tool calling not yet production-ready
- Like other speech-to-speech models, most teams eventually move to pipeline architecture for production
- Represents the emerging direction of pure speech-to-speech models

## Related
- [[Nvidia]] — creator
- [[Speech-to-Speech Models]] — model category
- [[Voice Agent Pipeline Architecture]] — production alternative
- [[OpenAI]] — real-time API competitor
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
