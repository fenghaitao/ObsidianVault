---
title: "EdgeModels"
type: concept
tags: [models, deployment, on-device, small-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Edge models are AI models designed for on-device deployment on memory-constrained hardware such as phones, cars, and other embedded devices. They are characterized by being memory-bound, task-specific, and latency-sensitive, with low knowledge capacity compared to large models.

## Key Information
- **Three defining characteristics**: memory-bound (hardware constraints), task-specific (not general-purpose chatbots), latency-sensitive (need fast throughput)
- **Deployment targets**: phones, cars, and other devices without reliable internet connectivity
- **Use cases**: in-car deployment (no internet), latency-sensitive workloads, privacy-regulated environments (finance, healthcare)
- **Not scaled-down large models**: Require specialized architectures, training recipes, and post-training techniques
- **Knowledge capacity limitation**: Compensated by agentic tool use (web search, Python) rather than relying on memorized knowledge
- **Long context limitation**: Compensated by recursive LM environments and Python shortcuts
- Liquid AI's models range from 350M to 24B parameters

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[LiquidAI]] — company focused on edge models
- [[LFM]] — Liquid Foundation Models
- [[OnDeviceProfiling]] — architecture optimization methodology
- [[AgenticReinforcementLearning]] — compensating for knowledge limits
- [[DoomLoop]] — particularly severe in small reasoning models
