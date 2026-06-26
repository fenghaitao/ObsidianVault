---
title: "summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA"
type: source
tags: [source, transcript]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md"]
last_updated: 2026-06-26
---
## Core Summary
Mozhgan Kabiri Chimeh presents data-backed benchmarks of running LLMs locally on the Nvidia DGX Spark, a desktop system powered by the GB10 Grace Blackwell superchip with 128 GB of unified memory. Using vLLM and an automated benchmarking harness with Docker isolation, she demonstrates that the 14B parameter model with NVFB4 4-bit floating-point quantization achieves 20.19 tokens per second — faster than human reading speed — while the unquantized 14B base model drops to 8.40 tokens/sec. The key insight is that quantization format choice is as important as hardware itself, and the DGX Spark enables developers to prototype locally with the same Nvidia AI software stack used in production data centers, then scale to cloud when ready.

## Key Points
- DGX Spark is powered by the GB10 Grace Blackwell superchip with 128 GB unified memory, supporting models up to ~200B parameters locally
- The automated benchmarking harness uses Docker for environment isolation, three mandatory warm-up runs, and 1-second GPU metrics logging
- 1.5B instruct model achieves 61.73 tokens/sec; 14B NVFB4 model achieves 20.19 tokens/sec; 14B base model drops to 8.40 tokens/sec
- NVFB4 quantization on the 14B model delivers 3.4x faster time-to-first-token compared to the unquantized 14B base model
- Memory capacity (128 GB) is not the same as memory bandwidth — throughput is governed by how efficiently data moves
- NVFB4 effectively increases "intelligence per byte," making a 14B model feel as responsive as a much smaller one
- The DGX Spark runs the same Nvidia AI software stack used in data centers, enabling desktop-to-cloud workflow portability
- Ideal use cases: steady-state workloads, privacy-sensitive data, and rapid prototyping

## Related
- [[Mozhgan Kabiri Chimeh]] — presenter, Nvidia developer relations manager
- [[Nvidia]] — company behind DGX Spark and NVFB4
- [[DGX Spark]] — the local AI development hardware system benchmarked
- [[vLLM]] — inference serving framework used in benchmarks
- [[NVFB4]] — Nvidia's 4-bit floating-point quantization format
- [[Time to First Token]] — user-perceived latency metric
- [[Local LLM Inference]] — running LLMs on local hardware vs cloud
- [[Unified Memory Architecture]] — 128 GB unified memory on DGX Spark
- [[Quantization]] — precision reduction technique; NVFB4 as key enabler
