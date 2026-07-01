---
title: "CUDA Graph Capture"
type: concept
tags: [cuda, gpu, optimization, inference, performance, tts]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
CUDA Graph Capture is a GPU optimization technique that records a sequence of CUDA operations into a graph that can be replayed with minimal CPU-GPU coordination overhead. It is used to accelerate neural network inference by keeping all computation on the GPU and eliminating repeated CPU-GPU synchronization.

## Key Information
- Solves the problem of autoregressive models requiring CPU-GPU coordination for each of hundreds of generation steps
- In Coqui 3 TTS: 500 autoregressive steps per audio packet, each requiring CPU-GPU data transfer
- Without graph capture, CPU-GPU coordination overhead accumulates significantly across steps
- Prerequisite: requires a static KV cache (fixed size) because dynamic KV cache prevents graph pre-recording
- Applied to Coqui 3 TTS to achieve 5.8x real-time factor (up from 0.8x)
- Cannot be used when KV cache size varies with input length — must switch to static allocation first
- Trade-off: uses more GPU RAM from the start (static allocation) but achieves much faster inference

## Related
- [[KV Cache]] — must be static for CUDA graph capture to work
- [[RealTime Factor]] — metric improved by graph capture
- [[Coqui]] — TTS model optimized with this technique
- [[AheadOfTime Compilation]] — related optimization concept
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
