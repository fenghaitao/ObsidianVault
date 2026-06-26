---
title: "NVFB4"
type: concept
tags: [quantization, nvidia, fp4, inference, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md"]
last_updated: 2026-06-26
---

## Definition
NVFB4 is Nvidia's 4-bit floating-point quantization format that dramatically improves LLM inference throughput and time-to-first-token on Blackwell architecture hardware. It effectively increases "intelligence per byte," allowing larger models to feel as responsive as much smaller ones.

## Key Information
- On the DGX Spark, a 14B NVFB4-quantized model achieves 20.19 tokens/sec vs. 8.40 tokens/sec for the unquantized 14B base model
- Delivers 3.4x faster time-to-first-token compared to the unquantized 14B base model
- The choice of quantization format is as important as the hardware itself on Blackwell architecture
- Bridges the gap between research work and production prototyping on local hardware
- Increases intelligence per byte, making larger models practical on local workstations
- Works in conjunction with Nvidia's unified memory architecture to maximize throughput

## Related
- [[Quantization]] — broader concept of precision reduction
- [[DGX Spark]] — hardware where NVFB4 was benchmarked
- [[Nvidia]] — creator of NVFB4
- [[vLLM]] — inference framework used with NVFB4 models
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
