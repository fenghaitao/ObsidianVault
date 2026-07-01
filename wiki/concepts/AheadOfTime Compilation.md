---
title: "Ahead-of-Time Compilation"
type: concept
tags: [compilation, optimization, deployment, on-device, edge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Ahead-of-Time (AOT) Compilation is a model compilation strategy where ML models are compiled to optimized native code before deployment, as opposed to Just-in-Time (JIT) compilation which compiles at runtime. Lite RT supports both strategies, and the AI Edge Portal helps determine which is optimal for a given model and device fleet.

## Key Information
- Compiles models to optimized native code before deployment to devices
- Contrasts with Just-in-Time (JIT) compilation, which compiles at runtime
- Lite RT supports both AOT and JIT compilation strategies
- AI Edge Portal benchmarking service helps determine the right strategy for a given model
- Choice between AOT and JIT depends on model size, target device fleet, and performance requirements
- AOT can provide faster startup and more predictable performance; JIT offers more flexibility

## Related
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source
- [[Lite RT]] — framework supporting AOT
- [[AI Edge Portal]] — tool for determining compilation strategy
- [[Google AI Edge]] — parent division
- [[OnDeviceAI]] — broader concept
