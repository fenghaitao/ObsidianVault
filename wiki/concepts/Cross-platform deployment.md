---
title: "Cross-platform deployment"
type: concept
tags: [deployment, on-device, mobile, framework, portability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Cross-platform deployment is the capability of Google's LiteRT and LiteRT-LM frameworks to produce a single model file that runs on CPU and GPU across Android, iOS, macOS, Linux, Windows, web, and IoT devices without modification. NPU deployment requires device-specific AOT compilation.

## Key Information
- Single LiteRT/LiteRT-LM file works across CPU and GPU on all major platforms
- Supported platforms: Android, iOS, macOS, Linux, Windows, web, IoT devices
- NPU requires special AOT (Ahead-of-Time) compilation producing a device-specific file
- Underlying optimization libraries: XNNPACK (CPU) and ML Drift (GPU)
- Consistent API across NPU, CPU, and GPU despite different build workflows
- Ships in Android as part of system services
- Same file can also be used by third-party apps

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[LiteRT-LM]] — LLM runtime with this capability
- [[LiteRT]] — general inference framework with this capability
- [[NPU]] — requires AOT compilation
- [[AOT Compilation]] — required for NPU deployment
- [[Google AI Edge]] — parent division
