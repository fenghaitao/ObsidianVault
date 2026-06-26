---
title: "MAX"
type: entity
tags: [framework, ai, inference, pytorch, genai, compiler]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner.md"]
last_updated: 2026-06-26
---

## Definition
MAX is Modular's AI framework designed as the best way to deploy PyTorch and run generative AI inference. It replaces vendor-specific libraries (CUDA, Intel MKL) with a single consistent compiler stack for unified CPU and GPU deployment.

## Key Information
- Two components: a free AI framework and paid managed services
- Focused primarily on inference, particularly for LLMs and GenAI workloads
- Works with PyTorch out of the box; also supports ONNX, TorchScript, and torch.compile
- Provides native APIs for advanced techniques like KV-caches and paged-attention for pushing state-of-the-art LLM techniques
- Replaces CUDA, Intel MKL, and other vendor libraries with a single consistent stack built from the ground up
- Achieves 5x faster inference than [[LlamaCpp]] on cloud CPUs using INT4/INT6 quantization
- GPU performance: matches or beats cuBLAS and CUTLASS on matrix multiplication benchmarks
- GPU support officially launched September 2024 (early access available via Discord before that)
- Supports production deployment on Kubernetes and SageMaker
- Underlying technology includes advanced compilers, high-performance kernels, and the [[Mojo]] programming language

## Related
- [[Modular]] — company behind MAX
- [[Mojo]] — programming language used to build MAX
- [[ChrisLattner]] — co-founder of Modular
- [[LlamaCpp]] — competing CPU inference framework MAX outperforms
- [[UnifiedAIStack]] — architectural concept MAX embodies
- [[summary-20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner]] — source
