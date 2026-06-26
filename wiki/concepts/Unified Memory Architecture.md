---
title: "Unified Memory Architecture"
type: concept
tags: [hardware, memory, gpu, cpu, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md"]
last_updated: 2026-06-26
---

## Definition
Unified Memory Architecture is a hardware design where CPU and GPU share a single pool of memory, eliminating data transfer overhead between separate memory banks. On the DGX Spark, this provides 128 GB of unified memory, enabling models up to approximately 200 billion parameters to run locally.

## Key Information
- Combines CPU and GPU memory into a single shared pool, removing the need to copy data between separate memory spaces
- The DGX Spark's 128 GB unified memory supports models up to ~200B parameters
- Memory capacity (fitting the model) is distinct from memory bandwidth (how fast data moves), and both govern inference throughput
- Unified memory is a key enabler for local LLM inference on workstation-class hardware
- Part of the GB10 Grace Blackwell superchip architecture

## Related
- [[DGX Spark]] — hardware system featuring unified memory
- [[Nvidia]] — company behind the Grace Blackwell architecture
- [[Local LLM Inference]] — workflow enabled by unified memory
- [[NVFB4]] — quantization format that maximizes throughput within unified memory constraints
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
