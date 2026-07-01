---
title: "Real-Time Factor"
type: concept
tags: [tts, performance, latency, optimization, benchmarking, voice-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Real-Time Factor (RTF) is a performance metric for speech synthesis that measures the ratio of audio generation time to audio duration. An RTF of 1.0 means the system generates audio at exactly real time; below 1.0 means it is slower than real time; above 1.0 means it is faster than real time.

## Key Information
- RTF = audio duration / generation time (higher is better for speed)
- RTF 0.8: generates 1 second of audio in 1.2 seconds (sub-real-time, unusable for interactive voice)
- RTF 5.8: generates 1 second of audio in ~200ms (usable for voice agents)
- Original Coqui 3 TTS had RTF 0.8 — too slow for voice agents
- Optimized Faster Coqui 3 TTS achieved RTF 5.8 via streaming, static KV cache, and CUDA graph capture
- For voice agents, RTF must be high enough that the entire pipeline (understand → produce → pronounce) fits within human conversation latency (~200ms)
- RTF is distinct from Time to First Audio — RTF measures sustained throughput, TFA measures startup latency
- Must be less than 1 to avoid buffering in voice agent pipelines

## Related
- [[Time to First Audio]] — complementary latency metric
- [[CUDA Graph Capture]] — optimization technique that improved RTF
- [[KV Cache]] — static KV cache contributed to RTF improvement
- [[Coqui]] — TTS model optimized for RTF
- [[Streaming TTS]] — streaming is key to achieving usable RTF
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Voice Agent Pipeline Architecture]] — the pipeline where RTF is a key metric
