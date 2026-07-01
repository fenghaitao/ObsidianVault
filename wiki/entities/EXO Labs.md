---
title: "EXO Labs"
type: entity
tags: [company, lab, local-inference, distributed-computing, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
EXO Labs is a research lab focused on running frontier AI systems on local consumer hardware, working across the full stack including models, software kernels, orchestration, and hardware optimization.

## Key Information
- Name derived from "exocortex" — the idea of AI as an extension of human cognition
- Mission is to drive down the cost of running frontier AI systems locally
- Develops EXO, a mesh-network app for distributed local inference
- Works across the full stack: kernel-level optimizations (kernel fusion for 30% performance gains), orchestration (tensor parallelism with RDMA), model support (GLM 5.1, Qwen, Gemma), and hardware (Mac, Nvidia, heterogeneous setups)
- Achieved single-digit microsecond latency for inter-device communication via RDMA over Thunderbolt 5
- Plans to publish open benchmarks showing performance across hardware, models, quantizations, and pruning configurations
- Building a Pareto frontier tool for users to select hardware budgets and see optimal local inference configurations
- Website: exolabs.net

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Alex Cheema]] — co-founder
- [[EXO]] — the distributed inference app
- [[Exocortex]] — the concept behind the name
- [[FullStack CoDesign]] — core methodology
- [[Heterogeneous Computing]] — key architectural approach
- [[Tensor Parallelism]] — distribution technique used
- [[GLM 5.1]] — frontier model demonstrated
