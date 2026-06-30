---
title: "Hybrid Inference"
type: concept
tags: [inference, gpu, neural-engine, apple-silicon, optimization, on-device-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Hybrid Inference refers to combining Apple Silicon's GPU and Neural Engine for on-device AI inference, leveraging both compute units simultaneously for better performance. Currently not possible due to Core ML's private API limitations, but expected to become viable after WWDC improvements.

## Key Information
- MLX currently uses only the GPU for inference, not the Neural Engine
- Core ML is needed to access the Neural Engine, but suffers from poor developer experience
- Hybrid inference would split workloads between GPU and Neural Engine for better throughput
- Prince Canuma's team (Neywa Labs) has internal projects ready for when APIs improve
- Apple may be merging Neural Engine components into the GPU (hints in M5 series)
- WWDC is expected to potentially address private API issues blocking hybrid inference
- Key enabler for even more efficient on-device AI on Apple Silicon

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[MLX]] — GPU-based framework
- [[Core ML]] — Neural Engine framework
- [[Apple]] — hardware provider
- [[OnDeviceAI]] — core concept
