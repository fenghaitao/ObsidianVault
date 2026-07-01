---
title: "Max Ryabinin"
type: entity
tags: [person, researcher, together-ai, long-context, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Max Ryabinin is the VP of Research and Development at Together AI. He leads research on long-context model training, including the "Road to 5M" project that achieved 5 million token context length on a single 8×H100 GPU node.

## Key Information
- VP of R&D at [[Together AI]]
- Led the "Road to 5M" research project breaking memory barriers in context parallelism
- Primary author of [[Untitled Ulysses]] (U-Pipe), a novel technique that subdivides attention head computation into time-sequenced chunks to further reduce activation memory
- Presented a systematic walkthrough of long-context training optimizations: FSDP → DeepSpeed Ulysses → activation checkpointing → CPU offloading → sequence parallelism → U-Pipe
- Emphasizes using PyTorch profiler to identify unexpected memory bottlenecks during training

## Related
- [[Together AI]] — employer
- [[Untitled Ulysses]] — novel research contribution (U-Pipe)
- [[Context Parallelism]] — core research area
- [[Long Context Training]] — primary research domain
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
