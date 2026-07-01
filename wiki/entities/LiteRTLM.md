---
title: "LiteRT-LM"
type: entity
tags: [framework, google, llm, runtime, on-device, edge, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
LiteRT-LM is Google's open-source LLM runtime for mobile and edge devices, built on top of LiteRT. It provides the full autoregressive loop and exposes easy-to-use APIs for running LLMs on device across platforms.

## Key Information
- Open-source LLM runtime for mobile and edge devices
- Built on top of LiteRT (formerly TensorFlow Lite)
- Provides C++, Java, Swift (coming soon), and Python APIs (as of April 2026)
- Takes a LiteRT-LM file (LiteRT file with tokenizer and other components in one package)
- Single file works across CPU and GPU on Android, iOS, macOS, Linux, Windows, web, and IoT devices
- Supports hardware acceleration via NPU (requires AOT compilation)
- Powers the Google AI Gallery app
- Supports third-party models (Qwen, FastVLM from Apple, etc.)
- Includes constrained decoding for reliable tool calling on small models
- Underlying optimization libraries: XNNPACK (CPU) and ML Drift (GPU)
- Workflow: HuggingFace Transformers → LiteRT Torch (with quantization) → LiteRT-LM file → deploy

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[LiteRT]] — underlying inference framework
- [[Google AI Edge]] — parent division
- [[AI Edge Gallery]] — app powered by LiteRT-LM
- [[ConstrainedDecoding]] — technique used for tool calling reliability
- [[CrossPlatform deployment]] — key capability
- [[NPU]] — hardware acceleration support
- [[Quantization]] — built into the workflow
