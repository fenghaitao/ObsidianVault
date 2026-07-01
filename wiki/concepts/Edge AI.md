---
title: "Edge AI"
type: concept
tags: [deployment, on-device, inference, mobile, iot]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Edge AI is the practice of running AI models directly on edge devices (phones, laptops, IoT, embedded systems) rather than in the cloud. It offers four key benefits: latency/UX improvements, privacy (data stays on device), offline use, and cost savings.

## Key Information
- Four key benefits: latency/UX, privacy, offline use, cost savings
- Google AI Edge is Google's dedicated division for edge AI
- Stack: MediaPipe, LiteRT-LM, LiteRT
- Two deployment trends: system-level GenAI (2-5B models in OS) and in-app GenAI (100-500M models per app)
- Single model file deploys on CPU/GPU across platforms; NPU requires AOT compilation
- Used in Google products: Photos, YouTube Shorts, Pixel live voice translation
- Tiny LLMs (under 1B params) fine-tuned for specific tasks enable production-quality edge AI
- Agent skills now possible on edge devices with Gemma 4 models
- Growing interest in embedded/IoT use cases, especially with image input

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Google AI Edge]] — Google's edge AI division
- [[OnDeviceAI]] — closely related concept
- [[Tiny LLMs]] — model category for edge deployment
- [[SystemLevel GenAI]] — deployment trend
- [[InApp GenAI]] — deployment trend
- [[LiteRTLM]] — runtime for edge LLMs
- [[NPU]] — hardware acceleration
