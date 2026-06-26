---
title: "Time to First Token"
type: concept
tags: [llm, inference, latency, performance, user-experience]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA.md"]
last_updated: 2026-06-26
---

## Definition
Time to First Token (TTFT) is the latency metric that defines user-perceived performance in AI applications. It measures the time from when a request is sent until the first token of the streaming response is received. If the first token arrives instantly, the application feels responsive.

## Key Information
- The metric that determines whether an AI application feels instant or broken to the user
- More parameters mean more computation before the first token is generated, so TTFT increases with model size
- On the DGX Spark, the 14B NVFB4 model achieved 3.4x faster TTFT than the unquantized 14B base model
- Measured by timestamping the very first chunk of a streaming response from vLLM
- Distinct from throughput (tokens/sec) — TTFT is about perceived responsiveness, throughput is about raw processing speed
- Quantization dramatically improves TTFT by reducing the computational load before the first token

## Related
- [[NVFB4]] — quantization format that dramatically improves TTFT
- [[vLLM]] — inference framework whose streaming API enables TTFT measurement
- [[DGX Spark]] — hardware where TTFT benchmarks were conducted
- [[Local LLM Inference]] — context where TTFT matters for developer experience
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — source
