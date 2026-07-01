---
title: "summary-20260616 - You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia"
type: source
tags: [source, transcript, diffusion, optimization, quantization, nvidia]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260616 - You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia.md"]
last_updated: 2026-06-30
---

## Core Summary

Ziv Ilan from Nvidia presents optimization techniques for diffusion models: quantization, caching, and distillation. Borrowing concepts from the LLM ecosystem, these reduce diffusion steps from 20-50 to fewer, enabling real-time image/video generation. Work with Black Forest Labs on Flux 2 shows dynamic quantization impact.

## Key Points

- Three optimization techniques: (1) Quantization (post-training or quantization-aware, dynamic preferred for diffusion). (2) Caching (KV cache concepts adapted for diffusion's non-autoregressive nature). (3) Distillation (teacher-student to reduce steps).
- Diffusion models are attention-heavy — quantization impact is less than for LLMs but still valuable.
- Dynamic quantization: ranges computed on-the-fly to match data distribution. Pre-quantized checkpoints available on HuggingFace.
- Real-time image/video is the holy grail: enables robotics world models, gaming, content generation.
- TRT LLM visual gen repository: open-source quantization tools for the community.
- Ecosystem less mature than LLM/VLM — borrowing concepts from autoregressive world.

## Related

- [[ZivIlan]] — speaker, Nvidia AI Labs
- [[Nvidia]] — company
- [[DiffusionModels]] — generative models
- [[ModelQuantization]] — optimization technique
- [[KV Cache]] — caching for diffusion
- [[ModelDistillation]] — step reduction
