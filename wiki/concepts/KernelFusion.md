---
title: "KernelFusion"
type: concept
tags: [gpu, compiler, optimization, performance, inference]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner.md"]
last_updated: 2026-06-26
---

## Definition
Kernel Fusion is a compiler optimization technique that automatically combines multiple GPU operations into a single kernel, eliminating redundant memory reads and writes. MAX provides an auto-fusing compiler that achieves good GPU performance without requiring developers to write hand-fused kernels.

## Key Information
- Traditional GPU optimization requires developers to manually fuse operations into custom CUDA kernels — a labor-intensive and expertise-heavy process
- MAX's auto-fusing compiler performs kernel fusion automatically, giving good performance "for the normal cases" without hand-written fused kernels
- Manual kernel fusion via CUDA or Triton remains available for advanced developers who need the absolute best performance
- Auto-fusion represents a major usability improvement by separating the "how to get good performance" from the "what computation to perform"
- Kernel fusion is part of the broader compiler technology stack in MAX that includes graph optimization, high-performance kernel libraries, and runtime optimizations
- The combination of auto-fusion for common cases and direct kernel programming for experts embodies MAX's "it just works" philosophy inspired by Chris Lattner's experience at Apple

## Related
- [[GPUKernelProgramming]] — the manual alternative to auto-fusion
- [[MAX]] — framework providing the auto-fusing compiler
- [[UnifiedAIStack]] — broader architectural concept encompassing kernel fusion
- [[Mojo]] — language used for hand-written kernels when auto-fusion isn't enough
- [[summary-20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner]] — source
