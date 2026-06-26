---
title: "FPTraining"
type: concept
tags: [training, precision, hardware, optimization, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Low-precision floating-point training (FP8, float4) reduces the numerical precision of model weights and activations during training and inference to achieve dramatic speed improvements (2-3x per precision halving) by using fewer transistors per operation.

## Key Information
- **FP8 vs FP16**: FP8 is approximately 2-3x faster than FP16 because it uses roughly half the transistors, not exactly 4x because of overhead from data movement and other transistor uses
- **Float4**: Nvidia's B100 GPUs natively support float4 (1 sign + exponent + fraction bits), approximately 2x faster than FP8; considered the likely final precision limit
- **1.58-bit vs float4**: Daniel Han argues against 1.58-bit approaches — float4 achieves similar transistor count without the complexity of straight-through estimators and manipulation overhead required by 1.58-bit
- **Mixed precision**: Modern training often uses float6 for gradients and float4 for activations simultaneously
- **Diminishing returns**: Going below float4 (float3, float2) yields diminishing speed returns; float4 may be the practical minimum
- **TF32 marketing**: Nvidia markets "TF32" (Tensor Float 32) but it's actually 19-bit precision, not true 32-bit — a marketing simplification
- **Sign bit necessity**: The sign bit is needed for negative directions in representation, though models could theoretically be trained without one
- **Mobile deployment**: 2-bit precision can run models on phones (e.g., Mixtral 8x7B at ~20 TPS on Snapdragon X) using flash storage as memory; combining 2-bit MLP with 4-bit attention optimizes quality vs. memory

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[Nvidia]] — B100 GPU hardware supporting float4
- [[LLMImplementationAnalysis]] — precision issues as a source of implementation bugs
