---
title: "Alex Cheema"
type: entity
tags: [person, founder, local-inference, distributed-computing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Alex Cheema is the co-founder and lead of EXO Labs, a research lab focused on running frontier AI systems on local consumer hardware through full-stack co-design.

## Key Information
- Works on EXO, an app for distributed local inference across heterogeneous devices
- Advocates for full-stack optimization across kernels, orchestration, models, and hardware
- Argues that inference is primarily memory-bound, not compute-bound like training
- Believes a 100x improvement in price-to-performance for local inference is achievable through co-design
- Predicts viable consumer inference boxes ($5,000 range) within 18-24 months
- Identified 50% performance gap in Qwen 3.5 on Apple Silicon due to inefficient kernel launches, achieved 30% improvement through kernel fusion
- Presented live demo of GLM 5.1 running across 4 clustered Mac Studios with RDMA over Thunderbolt 5
- Demonstrates heterogeneous prefill-decode disaggregation using Nvidia Spark + MacBook for ~2x speedup on large prompts
- Uses event sourcing architecture in EXO for distributed consistency guarantees

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[EXO Labs]] — his lab
- [[EXO]] — the distributed inference app
- [[AndrejKarpathy]] — referenced "not your weights, not your brain"
- [[Exocortex]] — the concept behind EXO's name
- [[FullStack CoDesign]] — his core methodology
- [[Heterogeneous Computing]] — key architectural approach
