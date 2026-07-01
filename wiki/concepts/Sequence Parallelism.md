---
title: "Sequence Parallelism"
type: concept
tags: [training, memory-optimization, long-context, parallelism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Sequence parallelism (also referred to as Arctic sequence length training) is a memory optimization technique that tiles element-wise operations (loss computation, MLP layers) across the sequence length dimension to avoid creating large intermediate buffers whose dimensions scale with sequence length.

## Key Information
- **Mechanism**: Chunks element-wise computations along the sequence dimension so that buffers are smaller and reused across tiles
- **Problem addressed**: Element-wise operations like loss computation and MLPs would otherwise create buffers with dimension = sequence length (e.g., 3 million), consuming enormous memory
- **Position in optimization stack**: Applied after CPU offloading; the final technique needed to reach 3M tokens on a single 8×H100 node
- **Beyond 3M tokens**: Even with sequence parallelism, reaching 5M tokens requires [[Untitled Ulysses]] (U-Pipe)
- **Complementary to**: [[Context Parallelism]], which addresses the attention computation bottleneck rather than element-wise operations

## Related
- [[Context Parallelism]] — addresses attention computation (not element-wise ops)
- [[Untitled Ulysses]] — technique for pushing beyond 3M tokens
- [[Long Context Training]] — primary application
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
