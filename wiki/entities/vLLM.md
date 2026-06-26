---
title: "vLLM"
type: entity
tags: [software, inference, llm, serving, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
vLLM is an open-source LLM inference serving framework used to serve quantized models across different sizes and precision formats. It supports streaming responses and runs inside Nvidia-optimized containers for environment consistency between local development and data center deployment.

## Key Information
- Used by Mozhgan Kabiri Chimeh to serve models on the DGX Spark for benchmarking
- Supports quantized models across different sizes and precision formats
- Runs inside Nvidia-optimized Docker containers, ensuring identical environments between desktop and data center
- Provides streaming response APIs that enable precise time-to-first-token measurement
- Used in an automated benchmarking harness with environment isolation, warm-up runs, and GPU metrics logging

## Related
- [[DGX Spark]] — hardware vLLM was benchmarked on
- [[Nvidia]] — provides optimized containers for vLLM
- [[NVFB4]] — quantization format used with vLLM-served models
- [[Time to First Token]] — metric measured via vLLM streaming responses
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
