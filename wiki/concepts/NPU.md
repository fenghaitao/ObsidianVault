---
title: "NPU"
type: concept
tags: [hardware, acceleration, on-device, inference, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
NPU (Neural Processing Unit) is a specialized hardware accelerator for AI inference on edge devices. Unlike CPU and GPU which use JIT compilation from a single model file, NPU deployment requires Ahead-of-Time (AOT) compilation producing a device-specific artifact via a vendor compiler plugin.

## Key Information
- Specialized hardware accelerator for AI inference on edge devices
- Requires AOT (Ahead-of-Time) compilation, not JIT like CPU/GPU
- Produces a device-specific file via vendor compiler plugin
- Runtime dispatches work to the NPU device driver through a specific API
- Despite different build workflow, app development API is consistent across NPU, CPU, and GPU
- Cormac Brick led NPU architecture at Intel before joining Google
- Google AI Edge partners: Qualcomm, Intel, MediaTek
- Broader NPU support expected as more smaller models become available
- Provides significantly better performance than CPU/GPU for on-device inference

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[AOT Compilation]] — required compilation approach
- [[LiteRT-LM]] — runtime with NPU support
- [[Intel]] — NPU architecture (Cormac Brick's prior work)
- [[Qualcomm]] — NPU hardware partner
- [[MediaTek]] — NPU hardware partner
- [[Cormac Brick]] — led Intel NPU architecture
- [[Cross-platform deployment]] — JIT approach for CPU/GPU
