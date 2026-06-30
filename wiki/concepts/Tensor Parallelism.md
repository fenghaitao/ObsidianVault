---
title: "Tensor Parallelism"
type: concept
tags: [distributed-computing, inference, parallelism, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Tensor parallelism is a technique for distributing model inference across multiple devices by splitting individual tensor operations (matrix multiplications) across machines, requiring synchronization at each layer. It enables running models larger than any single device's memory but demands low-latency interconnects.

## Key Information
- Splits tensor operations within each layer across multiple devices
- Requires two synchronizations per layer — for a 60-layer model like DeepSeek/Kimmy, that's 120 synchronizations per token
- Communication latency is critical: 300 microseconds per sync × 120 = 36ms overhead, making it slower than single-device inference
- EXO's RDMA implementation over Thunderbolt 5 reduces latency to single-digit microseconds, making the total communication overhead less than 1ms
- With low-latency RDMA, tensor parallelism can actually be faster than single-device inference by aggregating memory bandwidth
- Demonstrated running GLM 5.1 (trillion parameters, ~400GB at 4-bit) across 4 Mac Studios with all devices at 100% utilization
- Used in conjunction with event sourcing for consistency when devices can join/leave dynamically
- Complementary to other parallelism strategies like pipeline parallelism and data parallelism

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[EXO]] — app implementing tensor parallelism with RDMA
- [[RDMA]] — the low-latency protocol that makes it practical
- [[Thunderbolt]] — the physical interconnect
- [[Event Sourcing]] — consistency mechanism for dynamic topologies
- [[Heterogeneous Computing]] — broader distribution strategy
