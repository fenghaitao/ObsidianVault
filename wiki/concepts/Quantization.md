---
title: "Quantization"
type: concept
tags: [ai, inference, optimization, llm, performance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-26
---

## Definition
Quantization is a technique for reducing the precision of model weights (e.g., from FP16 to INT4 or INT6) to accelerate inference and reduce memory usage. MAX achieves 5x faster inference than llama.cpp on cloud CPUs using INT4/INT6 quantization powered by advanced compiler technology.

## Key Information
- INT4 and INT6 are lower-precision integer formats used for quantizing LLM weights to dramatically reduce memory bandwidth requirements and accelerate inference
- MAX's quantization approach is powered by "really crazy compiler and technology" underneath, combined with high-performance kernels
- The 5x speedup over [[LlamaCpp]] demonstrates that quantization performance depends heavily on the underlying implementation, not just the bit-width reduction
- MAX's quantization approach is generalizable — not specific to one model, though benchmarks are demonstrated on popular models people are familiar with
- Quantization is particularly impactful for CPU-based inference where memory bandwidth is the primary bottleneck
- Lower precision directly translates to lower cost in production deployments by enabling more inference per compute dollar
- For on-device iPhone deployment, 4-bit is the practical minimum for acceptable quality; below 4-bit significantly degrades output
- 8-bit quantization is recommended for very small models on mobile devices
- MLX community on Hugging Face provides models quantized in 4-bit, 5-bit, 6-bit, 8-bit, BF16, and MXFP4 formats

## Related
- [[MAX]] — framework achieving 5x speedup via INT4/INT6 quantization
- [[NVFB4]] — Nvidia's 4-bit floating-point quantization format for Blackwell architecture
- [[LlamaCpp]] — CPU inference framework MAX outperforms on quantization benchmarks
- [[DGX Spark]] — hardware where NVFB4 quantization benchmarks were conducted
- [[Local LLM Inference]] — workflow enabled by quantization on local hardware
- [[MLX]] — Apple framework using quantized models on iPhone
- [[OnDeviceAI]] — concept enabled by quantization on mobile
- [[summary-20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner]] — source
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
