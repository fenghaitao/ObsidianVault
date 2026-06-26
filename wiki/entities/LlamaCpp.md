---
title: "LlamaCpp"
type: entity
tags: [framework, inference, llm, cpu, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
llama.cpp is a widely-used open-source CPU-based LLM inference framework that MAX benchmarks against, achieving 5x faster performance on INT4/INT6 quantized models on cloud CPUs.

## Key Information
- Popular CPU-based inference framework for running LLMs
- MAX achieves 5x speedup over llama.cpp on cloud CPUs using INT4/INT6 quantization
- Benchmark comparison demonstrates MAX's compiler-driven performance advantage for CPU inference workloads
- Represents the existing open-source inference tooling that [[MAX]] aims to improve upon
- Supported as an inference engine in LM Studio alongside MLX, allowing comparison between engines
- Used for on-device Gemma 4 demos: 10 parallel instances generating SVGs on laptop at 100 tokens/sec; also used for Android Studio offline agent mode
- Supports per-layer embeddings override via `--override-tensor` flag, moving PLE to CPU or disk for on-device efficiency
- Community has put llama.cpp on Nintendo Switch to run Gemma models
- Collaborates with Google DeepMind on Gemma 4 support at launch

## Related
- [[MAX]] — Modular's AI framework that outperforms llama.cpp by 5x
- [[Gemma4]] — model family running on llama.cpp
- [[Quantization]] — INT4/INT6 quantization techniques used in the benchmark
- [[LM Studio]] — desktop app supporting Llama CPP as an inference engine
- [[MLX]] — alternative inference engine also supported in LM Studio
- [[PerLayerEmbeddings]] — supported via override-tensor flag
- [[summary-20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
