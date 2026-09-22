---
title: "Inference Co-Design"
type: concept
tags: [ML, hardware, systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Inference co-design is Vlad Feinberg's term for designing neural architectures that run inference efficiently — jointly choosing network topology, matrix shapes, attention shape, and head count to saturate serving hardware while preserving quality.
## Key Information
- Hardware has different rates for matmul flops, vector flops (activations), memory bandwidth, and inter-chip communication; a given computation rarely matches the peak rate of all units.
- The goal is to choose neural-net shapes that fully saturate every hardware unit for high MFU during inference.
- It is more than an algebra problem because those shape choices change the quality you get when training the model.
- So inference co-design is a joint optimization: architectures that scale predictably (high quality) while maximizing inference MFU.
- It is "evergreen" because hardware's relative constants (flops / memory bandwidth / communication bandwidth) keep changing, shifting what the optimal shape is.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Gemini]] — application
- [[Gemini Flash]] — application
- [[Transformer]] — shapes and head counts
- [[Model Quantization]] — related pillar
- [[Model FLOPS Utilization]] — the metric
- [[Knowledge Distillation]] — related pillar
- [[Pre-training]] — pillar of his area
