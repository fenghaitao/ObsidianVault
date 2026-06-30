---
title: "EXO"
type: entity
tags: [tool, app, local-inference, distributed-computing, mesh-network]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
EXO is a macOS app developed by EXO Labs that runs in the background on each device and automatically discovers other EXO instances over a mesh network, distributing model inference across heterogeneous hardware.

## Key Information
- Auto-discovers other devices via mesh networking (Thunderbolt, Wi-Fi, Ethernet)
- Uses event sourcing architecture for distributed consistency — each machine writes an append-only log, merged across the cluster
- Maintains a live view of physical topology to determine optimal model distribution
- Supports tensor parallelism with RDMA for low-latency inter-device communication (single-digit microseconds)
- Exposes HTTP API endpoints on each device; compatible with Tailscale for secure remote access
- Supports heterogeneous prefill-decode disaggregation (e.g., prefill on GPU, decode on Mac)
- Demonstrated running GLM 5.1 across 4 Mac Studios; Qwen 3.5 across 2 machines at 77 tokens/sec
- Users can spin up multiple model instances simultaneously on the same cluster
- Handles dynamic topology — devices can join, leave, sleep, or disconnect at any time
- Plans to add support for importing models from other apps (llama.cpp, MLX)

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[EXO Labs]] — developer
- [[Alex Cheema]] — co-founder
- [[Tensor Parallelism]] — distribution technique
- [[Event Sourcing]] — architectural pattern
- [[RDMA]] — low-latency communication protocol
- [[Tailscale]] — secure remote access
- [[Heterogeneous Computing]] — key use case
- [[Thunderbolt]] — connectivity standard
