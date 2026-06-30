---
title: "Streaming ASR"
type: concept
tags: [speech-to-text, streaming, architecture, voice-agents, model-evolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Streaming ASR (Automatic Speech Recognition) refers to speech-to-text models designed to transcribe audio incrementally as it arrives, rather than waiting for complete audio clips. This architectural evolution moves from batch models like Whisper (trained on 30-second clips) to streaming-native models that can produce partial transcripts with minimal latency.

## Key Information
- Traditional batch models like [[Whisper]] were trained on 30-second audio clips — too long for voice agent use cases
- Workarounds for batch models: chunking audio, padding with silences, making multiple calls, stitching transcripts together
- Streaming-native models have two key characteristics:
  - Trained with different amounts of look-ahead time (80ms to ~1 second, not 30 seconds)
  - Able to cache encoder activations so that small steps in audio frames only require light computation
- Nvidia recently published a streaming-native STT model with these characteristics
- Enables much lower transcription latency for real-time voice conversations
- P90 transcription completion times can reach ~100ms with streaming-native models

## Related
- [[Word Error Rate]] — quality metric that streaming models must maintain
- [[Turn Detection]] — capability enabled by fast streaming transcription
- [[Voice Agent Pipeline Architecture]] — STT is the first stage
- [[Whisper]] — canonical batch model being superseded
- [[Nvidia]] — published a streaming-native STT model
- [[Together AI]] — runs streaming STT models at P90 ~100ms
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
