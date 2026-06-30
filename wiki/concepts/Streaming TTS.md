---
title: "Streaming TTS"
type: concept
tags: [voice-ai, tts, streaming, latency, speech]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-29
---

## Definition
Streaming TTS (text-to-speech) is a low-latency speech synthesis approach where audio is generated and played back as text is being produced, rather than waiting for the full text to be generated first. This reduces the perceived latency in voice AI systems by overlapping text generation with speech output.

## Key Information
- Part of Gradium AI's cascaded system implementation alongside streaming STT
- Reduces perceived latency by beginning speech output before full text is complete
- Gradium's streaming TTS latency is ~200ms for TTS alone
- Human conversation requires the entire stack (understand → produce → pronounce) to be ~200ms
- TTS latency of 200ms+ means cascaded systems inherently exceed human conversation latency targets
- Combined with voice cloning for personalized streaming output
- Competing with the reality that tool call latency (500ms-4s) is now the bigger bottleneck
- Coqui 3 TTS originally did not stream — generated full output before delivering any audio
- Adding streaming to Coqui 3 was the first of three optimizations (alongside static KV cache and CUDA graph capture) that took it from 0.8x to 5.8x real-time factor

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
- [[Coqui]] — TTS model that gained streaming capability
- [[Real-Time Factor]] — metric improved by streaming
- [[CUDA Graph Capture]] — companion optimization
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
- [[Coqui]] — TTS model that gained streaming capability
- [[Real-Time Factor]] — metric improved by streaming
- [[CUDA Graph Capture]] — companion optimization
- [[Cascaded Systems (Voice)]] — architecture using streaming TTS
- [[Latency]] — key metric being optimized
- [[Gradium AI]] — implements streaming TTS
- [[Voice AI]] — parent domain
- [[Voice Cloning]] — combined with streaming TTS
