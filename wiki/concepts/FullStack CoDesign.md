---
title: "Full-Stack Co-Design"
type: concept
tags: [methodology, optimization, hardware, software, models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Full-stack co-design is the methodology of optimizing AI systems by simultaneously considering models, software kernels, orchestration, harnesses, and hardware, rather than treating each layer independently. Gains compound across the stack, potentially achieving a 100x improvement in price-to-performance.

## Key Information
- Core methodology of EXO Labs for making local inference viable
- Argues that optimizations at each layer compound multiplicatively, not additively
- Layers include: model architecture, kernel implementations, orchestration/distribution, harness/agent layer, and hardware selection
- Harness layer is particularly undervalued — same model can get dramatically different performance with a better harness (e.g., OpenClaw vs Claude Code)
- Example: kernel fusion alone yielded 30% inference improvement on Qwen 3.5; combined with better orchestration, heterogeneous hardware, and model-level optimizations, the total gain compounds
- Already happening in data centers (Nvidia's Groq acquisition, Cerebras + Trainium pairings) but not yet common for local inference
- Requires opinionated choices about models and use cases to be effective

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[EXO Labs]] — primary practitioner
- [[Hardware Lottery]] — the problem full-stack co-design addresses
- [[Heterogeneous Computing]] — key hardware strategy within co-design
- [[Tensor Parallelism]] — distribution technique within co-design
