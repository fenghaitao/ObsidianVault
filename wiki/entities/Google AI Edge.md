---
title: "Google AI Edge"
type: entity
tags: [google, edge-ai, on-device, framework, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Google AI Edge is Google's division focused on bringing AI models to edge devices, used both internally for Google products and made available as open-source products. Its stack includes MediaPipe, LiteRT-LM, and LiteRT.

## Key Information
- Google division focused on edge AI deployment
- Stack includes: MediaPipe (ML pipelines), LiteRT-LM (LLM runtime), LiteRT (general inference framework, formerly TensorFlow Lite)
- Used internally for Google products (Photos, YouTube Shorts, Pixel live voice translation)
- Also available as open-source products for third-party developers
- Works closely with the Gemma team at Google DeepMind
- Single LiteRT file deploys on CPU and GPU across Android, iOS, macOS, Linux, Windows, web, and IoT devices
- Ships in Android as part of system services
- Underlying optimization libraries: XNNPACK (CPU) and ML Drift (GPU)
- Tech lead: Cormac Brick

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Cormac Brick]] — tech lead
- [[LiteRT-LM]] — LLM runtime
- [[LiteRT]] — general inference framework
- [[MediaPipe]] — ML pipeline framework
- [[Google]] — parent company
- [[Google DeepMind]] — Gemma model partner
- [[Android]] — ships as system service
- [[Google Pixel]] — product using edge AI
