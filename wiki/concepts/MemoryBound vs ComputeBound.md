---
title: "Memory-Bound vs Compute-Bound"
type: concept
tags: [inference, performance, hardware, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
The distinction between memory-bound and compute-bound operations in AI inference: training is primarily compute-bound (limited by FLOPs), while inference — especially the decode phase at low batch sizes — is primarily memory-bound (limited by memory bandwidth and capacity).

## Key Information
- Training is compute-bound: what matters is FLOPs per dollar and energy per FLOP
- Inference is memory-bound: most operations are limited by how fast model weights and KV caches can be loaded from memory
- The prefill phase is compute-bound (loading context, generating KV caches) but matters less for local single-user workloads
- The decode phase is memory-bound (auto-regressive token generation) and dominates user experience
- Single-user local inference operates at batch size 1, which is always memory-bound (unlike cloud where batching enables compute saturation)
- Three critical metrics for memory-bound inference: memory capacity (does it fit?), memory bandwidth (how fast?), and energy per byte (how much power?)
- This distinction is why heterogeneous hardware strategies work: use high-compute hardware for prefill, high-memory-bandwidth hardware for decode

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Memory Bandwidth]] — the key bottleneck
- [[PrefillDecode Disaggregation]] — architectural pattern leveraging this distinction
- [[Heterogeneous Computing]] — hardware strategy based on this distinction
- [[Batching]] — cloud technique that changes the compute/memory balance
