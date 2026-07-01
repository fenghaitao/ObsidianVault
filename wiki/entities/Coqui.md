---
title: "Coqui"
type: entity
tags: [company, tts, text-to-speech, voice-ai, open-source, voice-cloning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Coqui is a company that produces text-to-speech (TTS) models, notably Coqui 3 TTS and Coqui 3.5 27B. Their open-source TTS models are used in the Reachy Mini voice pipeline and were a breakthrough for open-source voice AI quality.

## Key Information
- Coqui 3 TTS released 2–3 months before May 2026 — a breakthrough in open-source TTS quality
- Original open-source implementation had good quality but sub-real-time speed (0.8x RTF)
- Coqui's commercial API was fast, but the open-source model was slow — likely a strategy to push users toward the paid API
- Coqui 3.5 27B is used as the LLM in Reachy Mini's conversation pipeline
- Andres Marafioti optimized Coqui 3 TTS to 5.8x real-time factor via streaming, static KV cache, and CUDA graph capture
- The optimized version ("Faster Coqui 3 TTS") is open source on Hugging Face
- Supports voice cloning — can clone voices from short audio samples
- Model is autoregressive, requiring 500 steps per audio packet before optimization

## Related
- [[Andres Marafioti]] — optimized Coqui 3 for real-time
- [[Reachy Mini]] — uses Coqui TTS in voice pipeline
- [[HuggingFace]] — platform hosting the models
- [[CUDA Graph Capture]] — optimization technique applied
- [[KV Cache]] — static KV cache optimization
- [[RealTime Factor]] — performance metric improved
- [[Time to First Audio]] — latency metric
- [[Voice Cloning]] — supported capability
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
