---
title: "KV Cache Compression"
type: concept
tags: [quantization, context-length, optimization, on-device-ai, mlx, memory]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
KV Cache Compression is the technique of reducing the memory footprint of the key-value (KV) cache in transformer models through quantization, enabling longer context windows on memory-constrained devices. Turbo Quant achieves 4x reduction while maintaining exact match quality.

## Key Information
- KV cache stores attention keys and values for all previous tokens; grows linearly with context length
- Without compression, KV cache can consume ~1GB for full models, limiting context on-device
- Turbo Quant reduces KV cache by 4x (e.g., ~1GB → ~250MB) with exact match quality
- At 300K tokens of context, throughput nearly doubles vs unquantized KV cache
- Enables serving up to 1 million tokens of context on-device (hardware-dependent)
- Implemented by Prince Canuma within 30 minutes of paper release (March 2025)
- Critical enabler for long-context on-device AI applications (document analysis, long conversations)
- Works alongside weight quantization (4-bit, 8-bit) for comprehensive memory optimization

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[Turbo Quant]] — specific implementation technique
- [[Quantization]] — broader technique family
- [[MLX]] — framework where it's implemented
- [[OnDeviceAI]] — core concept
- [[Context Compression]] — related concept
