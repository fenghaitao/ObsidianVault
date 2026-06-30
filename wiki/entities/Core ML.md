---
title: "Core ML"
type: entity
tags: [framework, apple, neural-engine, inference, on-device-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Core ML is Apple's framework for running machine learning models on the Neural Engine (a dedicated AI accelerator in Apple Silicon). Unlike MLX which uses the GPU, Core ML is required to leverage the Neural Engine, but currently suffers from poor developer experience due to private API limitations.

## Key Information
- Apple's framework for Neural Engine inference on Apple Silicon
- MLX uses GPU, not Neural Engine; Core ML is needed to access Neural Engine
- Current state: poor developer experience, not easy to use
- Private API issues are a major limitation — developers hope WWDC will address this
- Prince Canuma's team has internal projects for hybrid inference (GPU + Neural Engine) once APIs improve
- Apple may be changing Neural Engine architecture, potentially merging some components into GPU (M5 series hints at this)
- Future direction is uncertain but exciting — waiting for WWDC announcements

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[Apple]] — creator
- [[MLX]] — GPU-based alternative framework
- [[Hybrid Inference]] — combining GPU and Neural Engine
- [[OnDeviceAI]] — core concept
