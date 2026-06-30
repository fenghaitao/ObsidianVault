---
title: "Model Explorer (tool)"
type: concept
tags: [google, tool, quantization, model-optimization, graph, edge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Model Explorer is a Google tool that visualizes ML model computation graphs, allowing developers to inspect graph structure and decide which parts to quantize for mixed-precision optimization before deploying via Lite RT.

## Key Information
- Visualizes model computation graphs for inspection
- Enables developers to study the graph and decide which aspects to change
- Supports mixed-precision quantization: selectively quantize parts of the model rather than full conversion
- Part of the Google AI Edge toolchain alongside AI Edge Portal and Lite RT
- Helps optimize models for on-device deployment by identifying quantization opportunities

## Related
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source
- [[Lite RT]] — deployment framework
- [[Google AI Edge]] — parent division
- [[AI Edge Portal]] — companion benchmarking service
- [[Quantization]] — optimization technique
- [[OnDeviceAI]] — broader concept
