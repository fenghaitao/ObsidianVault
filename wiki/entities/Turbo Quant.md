---
title: "Turbo Quant"
type: entity
tags: [technique, quantization, kv-cache, mlx, on-device-ai, context-length]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Turbo Quant is a KV cache quantization technique that reduces the memory footprint of the key-value cache by 4x while maintaining response quality (exact match with full model). It enables serving up to 1 million tokens of context on-device on Apple Silicon via MLX.

## Key Information
- Implemented by Prince Canuma within 30 minutes of the paper's release (March 25)
- Reduces KV cache memory usage by 4x (e.g., ~1GB → ~250MB)
- Maintains exact match quality with full-precision model responses
- At 300,000 tokens of context, throughput nearly doubles compared to unquantized KV cache
- Enables serving 1 million tokens of context on-device (hardware-dependent)
- Implementation tweet went viral with ~700,000 views
- Key enabler for running long-context models entirely on consumer Apple hardware
- Part of the broader MLX on-device optimization ecosystem

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[Prince Canuma]] — implementer
- [[MLX]] — target framework
- [[KV Cache Compression]] — broader concept
- [[Quantization]] — related technique
- [[OnDeviceAI]] — core concept enabled by this technique
