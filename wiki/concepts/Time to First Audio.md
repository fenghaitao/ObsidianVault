---
title: "Time to First Audio"
type: concept
tags: [tts, latency, voice-ai, performance, streaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Time to First Audio (TFA) is the latency between when a text-to-speech system receives text input and when it begins producing the first audio output. It is the audio equivalent of Time to First Token (TTFT) for text generation and is critical for natural conversational voice agents.

## Key Information
- Original Coqui 3 TTS: TFA of several seconds (depending on output length)
- Optimized Faster Coqui 3 TTS: TFA reduced to a few milliseconds
- Client-perceived TFA includes infrastructure overhead (network, load balancing, etc.), not just model time
- Infrastructure time can be as significant as model time for fast models
- TFA is distinct from Real-Time Factor — TFA measures startup latency, RTF measures sustained throughput
- For voice agents, the full pipeline TFA (understand → produce → pronounce) must approach ~200ms for natural conversation
- TTFA is a key metric alongside Real-Time Factor for TTS model evaluation in voice agent pipelines

## Related
- [[RealTime Factor]] — complementary throughput metric
- [[Streaming TTS]] — streaming reduces perceived TFA
- [[CUDA Graph Capture]] — optimization that reduced TFA
- [[Coqui]] — TTS model with optimized TFA
- [[Time to First Token]] — text-generation equivalent concept
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Voice Agent Pipeline Architecture]] — the pipeline where TTFA is a key metric
