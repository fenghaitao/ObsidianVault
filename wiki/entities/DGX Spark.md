---
title: "DGX Spark"
type: entity
tags: [hardware, nvidia, ai, local-inference, workstation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md"]
last_updated: 2026-06-26
---

## Definition
The DGX Spark (also referred to as Jetson Spark in the transcript) is a desktop AI development system from Nvidia powered by the GB10 Grace Blackwell superchip, combining CPU and GPU with a unified memory architecture. It is designed to build and run AI locally as a standalone system.

## Key Information
- Powered by the GB10 Grace Blackwell superchip with unified CPU+GPU memory architecture
- 128 GB of unified memory, supporting models up to approximately 200 billion parameters
- NV4 support enables efficient quantization for larger models
- Runs the same Nvidia AI software stack used in production data centers, enabling desktop-to-cloud workflow portability
- Fits under or on top of a desk — a local workstation, not a data center machine
- Can be used as a standalone system for building and running AI
- Ideal for steady-state workloads, privacy-sensitive data, and rapid prototyping
- Visit build.nvidia.com/spark for playbooks and software stack

## Related
- [[Nvidia]] — manufacturer
- [[NVFB4]] — quantization format that maximizes performance on DGX Spark
- [[vLLM]] — inference framework used on DGX Spark
- [[Unified Memory Architecture]] — key architectural feature
- [[Mozhgan Kabiri Chimeh]] — benchmarked the system
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
