---
title: "NVIDIAH100"
type: entity
tags: [hardware, gpu, nvidia, ai-infrastructure, inference]
sources: []
last_updated: 2026-07-07
---

## Definition

The NVIDIA H100 is a high-performance GPU based on NVIDIA's Hopper architecture, designed for large-scale AI training and inference workloads. It is used to run computationally intensive model inference tasks that exceed the capacity of standard hardware.

## Key Information

- Used by [[CustomUniverse]] during the [[ClaudeOpus4.8]] Build Day hackathon (June 2026) to run the 3D reconstruction and scene rendering pipeline.
- [[Claude]] operated a remote NVIDIA H100 throughout the hackathon, managing the hardware end-to-end.
- The H100 is part of NVIDIA's data center GPU lineup, optimized for transformer-based model inference and training at scale.
- In the [[SyntheticData|synthetic data]] pipeline, the H100 handled the compute-heavy 3D reconstruction from phone-scanned objects captured with [[AppleRealityKit]].
- Users of open-source pipelines like CustomUniverse can run similar workloads on their own GPUs, lowering the barrier for robotics labs that lack specialized simulation engineers.

## Related

- [[CustomUniverse]] — hackathon project that operated a remote NVIDIA H100
- [[SyntheticData]] — use case requiring GPU compute for synthetic training data generation
- [[ClaudeOpus4.8]] — the model that operated the H100 during the hackathon
- [[Anthropic]] — hosted the hackathon where the H100 was used
- [[AppleRealityKit]] — object capture framework whose output the H100 processed
