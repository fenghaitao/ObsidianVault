---
title: "Mixture of Experts"
type: concept
tags: [architecture, ML, LLM]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Mixture of Experts (MoE) is a model architecture that routes tokens to a subset of "expert" parameters, increasing capacity — the architecture behind Gemini 2.0 that the Flash 2.0 team had to make latency-viable.
## Key Information
- MoE models use far more parameters overall, which consumes more HBM, so they must be sharded across multiple chips.
- Sharding experts across chips means a token may route from one TPU to another on many layers, inducing a lot of inter-chip communication and inflating latency as N grows.
- Flash models had been dense (for low latency) until pipeline prefill moved layers instead of experts across machines, breaking the HBM constraint and making MoE latency attractive.
- The Gemini 2.0 report's MoE series was made possible, in part, by this serving-time innovation.
- MoE ties closely to Transformer architectures and to distributed training/serving choices.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Gemini Flash]] — Flash 2.0 architecture
- [[Pipeline Parallelism]] — what made MoE viable
- [[Transformer]] — architecture family
- [[Tensor Processing Unit (TPU)]] — chips being sharded
- [[Pre-training]] — training phase
