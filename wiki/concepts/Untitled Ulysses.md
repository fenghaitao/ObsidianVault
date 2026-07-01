---
title: "Untitled Ulysses"
type: concept
tags: [training, memory-optimization, context-parallelism, together-ai, attention]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Untitled Ulysses (U-Pipe) is a novel context parallelism technique developed by Together AI that extends DeepSpeed Ulysses by subdividing attention head computation into time-sequenced chunks. Rather than computing all assigned heads simultaneously, it processes groups of heads sequentially while reusing the same GPU buffers, further reducing activation memory with minimal throughput impact.

## Key Information
- **Origin**: Developed by [[Max Ryabinin]] and the Together AI research team as part of the "Road to 5M" project
- **Key insight**: Computing even one set of attention heads already saturates GPU computational capacity within one iteration — meaning multiple head groups can be scheduled sequentially without significant throughput loss
- **Mechanism**: Divides attention heads into chunks; computes attention for one chunk, stores the partial result, then processes the next chunk reusing the same allocated buffers
- **Memory advantage**: Instead of allocating a large buffer for all heads simultaneously, allocates a smaller buffer reused across sequential iterations
- **Throughput**: Minimal impact at small scales; the chunk size vs. throughput relationship is straightforward — larger chunks use more memory but run slightly faster
- **Results**: Matches the most memory-optimized transformer training implementations at 8B and 32B scales while enabling 5M token context; can be more performant at shorter context lengths
- **Utility beyond 5M**: Can free up additional memory to reinvest elsewhere (e.g., more stages) even when not targeting extreme context lengths
- **Paper**: Publicly available with an upcoming detailed thread illustrating the method

## Related
- [[DeepSpeed Ulysses]] — parent technique that U-Pipe extends
- [[Context Parallelism]] — broader technique category
- [[Max Ryabinin]] — lead researcher
- [[Together AI]] — research organization
- [[Long Context Training]] — application domain
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
