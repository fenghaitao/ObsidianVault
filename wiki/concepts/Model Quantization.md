---
title: "Model Quantization"
type: concept
tags: [ML, optimization, hardware]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Model quantization compresses the numerical precision of a neural network's weights (and activations) — e.g., from FP32 toward 4-bit integers — to make models run more cheaply and with lower latency.
## Key Information
- Weights are normally stored as FP32 (32-bit floats, ~7 digits of precision); simple methods can reduce storage to 4-bit ints (range roughly -8 to 7) while mostly preserving quality.
- Applying quantization to runtime activations shrinks the matmul operands, so the actual compute — and its electricity — drops significantly.
- ~99% of AI-hardware operating cost is the power to run the chips, so quantization directly cuts cost and improves serving capacity and latency.
- It is one of Vlad's three pre-training verticals; he has worked on it "ever since" joining Google, and says it changes what is feasible for distillation and inference co-design.
- The "name of the game" is pushing precision below the four-bit frontier.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Pre-training]] — pillar of his area
- [[Inference Co-Design]] — related pillar
- [[Knowledge Distillation]] — related pillar
- [[Model FLOPS Utilization]] — related metric
- [[Transformer]] — weights being compressed
