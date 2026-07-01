---
title: "LiteRT"
type: entity
tags: [framework, google, inference, on-device, edge, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
LiteRT is Google's general inference framework for edge devices, formerly known as TensorFlow Lite. It serves as the foundation for LiteRT-LM and supports both LLM and non-LLM models across a wide range of platforms.

## Key Information
- General inference framework for edge devices, formerly TensorFlow Lite
- Foundation for LiteRT-LM (LLM runtime)
- Single file deploys on CPU and GPU across Android, iOS, macOS, Linux, Windows, web, and IoT devices
- NPU requires special AOT compilation producing a device-specific file
- Underlying optimization libraries: XNNPACK (CPU) and ML Drift (GPU)
- Supports non-LLM models (voice activity detection, denoising, etc.) for building complete apps
- Ships in Android as part of system services
- Used in Google products: Photos, YouTube Shorts, Pixel live voice translation
- LiteRT Torch: Python package for exporting PyTorch models with quantization built in
- LiteRT Torch Generative API: for building custom models from scratch

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[LiteRTLM]] — LLM runtime built on LiteRT
- [[Google AI Edge]] — parent division
- [[MediaPipe]] — ML pipeline framework also in the stack
- [[CrossPlatform deployment]] — key capability
- [[NPU]] — hardware acceleration via AOT compilation
- [[AOT Compilation]] — required for NPU deployment
