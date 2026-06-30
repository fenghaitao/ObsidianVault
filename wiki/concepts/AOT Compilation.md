---
title: "AOT Compilation"
type: concept
tags: [compilation, deployment, npu, on-device, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
AOT (Ahead-of-Time) Compilation is the workflow required for deploying AI models to NPU hardware accelerators. Unlike JIT (Just-in-Time) compilation used for CPU/GPU deployment from a single model file, AOT requires calling a vendor compiler plugin upfront to produce a device-specific artifact.

## Key Information
- Required for NPU deployment (not needed for CPU/GPU)
- Calls a vendor compiler plugin upfront to produce a device-specific artifact
- Contrasts with JIT workflow: single artifact works across CPU and GPU on all platforms
- Despite different build workflow, app development API is consistent across AOT and JIT paths
- Part of Google AI Edge's multi-hardware deployment strategy
- Best for distributing small models to lots of platforms (JIT), while AOT is best for hardware acceleration on device

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[NPU]] — hardware requiring AOT compilation
- [[Cross-platform deployment]] — JIT approach for CPU/GPU
- [[LiteRT-LM]] — runtime supporting both AOT and JIT
- [[LiteRT]] — framework supporting both paths
