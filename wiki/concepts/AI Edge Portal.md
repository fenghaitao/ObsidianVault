---
title: "AI Edge Portal"
type: concept
tags: [google, benchmarking, deployment, android, edge, on-device]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
AI Edge Portal is Google's cloud-based benchmarking service that helps developers test model performance across a broad fleet of Android devices, determining the right compilation strategy (ahead-of-time vs just-in-time) and quantization recipe for reliable deployment.

## Key Information
- Cloud-based benchmarking service for Android device fleets
- Helps developers determine optimal compilation strategy: ahead-of-time (AOT) vs just-in-time (JIT)
- Assists in finding the right quantization recipe for broad device compatibility
- Used by third-party app developers and internal Google teams
- Provides a "pulse check" on whether a model is deployable across diverse device hardware
- Part of the Google AI Edge toolchain alongside Model Explorer and Lite RT

## Related
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source
- [[Google AI Edge]] — parent division
- [[Lite RT]] — deployment framework
- [[Model Explorer (tool)]] — companion graph visualization tool
- [[Ahead-of-Time Compilation]] — compilation strategy evaluated
- [[Android]] — target platform
- [[OnDeviceAI]] — broader concept
