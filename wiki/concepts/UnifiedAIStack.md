---
title: "UnifiedAIStack"
type: concept
tags: [ai, architecture, compiler, inference, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner.md"]
last_updated: 2026-06-26
---

## Definition
A Unified AI Stack is an architectural approach to AI infrastructure that replaces multiple vendor-specific libraries (CUDA, Intel MKL, cuBLAS) with a single consistent compiler and runtime stack, enabling unified deployment across CPUs and GPUs without the "big fork at the top" pattern of two completely different technology stacks.

## Key Information
- Traditional approaches use a "big fork": one technology stack built on top of Intel MKL for CPUs and a completely different one on top of CUDA for GPUs, so nothing actually works the same across targets
- A unified stack replaces the entire layer of technology: matrix multiplications, fused attention layers, graph optimizations, and all the supporting components
- Benefits include predictable behavior across hardware targets, easier maintenance, and the ability to "program a GPU as easily as a CPU in Python"
- [[Modular]] rebuilt the world's first AI stack from the bottom up specifically for generative AI, going deeper than existing solutions by building [[Mojo]], a new programming language
- The unified approach enables GPU utilization improvements: typical GPU utilization is 30-50%, meaning users pay for 2-3x more GPU than necessary
- A unified stack provides both ease of use (for normal developers) and full power (for advanced developers writing custom kernels) without forcing a tradeoff
- The approach is analogous to how modern phones don't run 15-year-old Blackberry software — it's time to rethink the technology stack

## Related
- [[MAX]] — Modular's implementation of a unified AI stack
- [[AIInferenceFragmentation]] — the problem a unified stack solves
- [[Modular]] — company that rebuilt the AI stack from bottom up
- [[Mojo]] — programming language built to enable the unified stack
- [[summary-20240725 - Unlocking Developer Productivity across CPU and GPU with MAX： Chris Lattner]] — source
