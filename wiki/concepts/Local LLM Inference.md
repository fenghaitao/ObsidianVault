---
title: "Local LLM Inference"
type: concept
tags: [llm, inference, local, deployment, developer-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md"]
last_updated: 2026-06-26
---

## Definition
Local LLM inference is the practice of running large language models on local hardware (workstations, desktop systems) rather than in the cloud or data center. It addresses challenges of cost predictability, data residency, deterministic latency, and iteration speed by bringing AI development closer to where development actually happens.

## Key Information
- Motivations include cost predictability, data residency/privacy, deterministic latency, and avoiding shared infrastructure scheduling delays
- Memory capacity and memory bandwidth are distinct constraints — fitting a model in memory does not guarantee usable throughput
- Quantization is a critical enabler, with NVFB4 making 14B models practical at 20+ tokens/sec on local hardware
- The DGX Spark with 128 GB unified memory can run models up to ~200B parameters locally
- Local inference is not about replacing the cloud but complementing it — prototype locally, scale to cloud when ready
- Running the same software stack (vLLM, Nvidia containers) locally and in data centers enables seamless workflow portability
- Ideal for steady-state workloads, privacy-sensitive data, and rapid prototyping
- On mobile devices, MLX enables 40 tokens/second on iPhone with 4-bit quantized models like Gemma 4
- LM Studio provides a desktop interface for running local models with multiple engines (MLX, Llama CPP) and serving via OpenAI/Anthropic-compatible APIs

## Related
- [[DGX Spark]] — local hardware system designed for this workflow
- [[NVFB4]] — quantization format enabling practical local inference
- [[Quantization]] — broader technique for reducing model precision
- [[Unified Memory Architecture]] — hardware feature enabling large local models
- [[Time to First Token]] — key user-experience metric for local inference
- [[OnDeviceAI]] — related concept for mobile/edge devices
- [[MLX]] — Apple framework for on-device local inference
- [[LM Studio]] — desktop app for local model management
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
