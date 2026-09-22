---
title: "Pre-training"
type: concept
tags: [ML, training, LLM]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Pre-training is the initial, largest-scale training phase of an LLM; as Google DeepMind's pre-training area lead, Vlad Feinberg explains its core question as predicting final test loss from scaling laws.
## Key Information
- Every pre-training run commits more flops than any previous run — a one-shot, high-stakes version of the classical ML test-error problem.
- Standalone pre-training and post-training teams exist inside Google DeepMind, focused on "creating... models," while remaining responsible for delivering models that train stably (being "SREs of sorts" for the run).
- Vlad's team's deliverables: Flash and Flash-Lite models (AI Overviews, AI mode, ads, YouTube, 1P models) and technical POC work for the Google-Apple partnership, plus research for the Pro series.
- Three research verticals: distillation, inference co-design, and quantization.
- Recipes are functions from desired flops to a training routine, paired with a prediction rule for accuracy.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — area lead
- [[Google DeepMind]] — his org
- [[Gemini]] — models he trains
- [[Gemini Flash]] — models he trains
- [[Scaling Laws]] — core question
- [[Knowledge Distillation]] — vertical
- [[Inference Co-Design]] — vertical
- [[Model Quantization]] — vertical
- [[Mixture of Experts]] — architecture choice
