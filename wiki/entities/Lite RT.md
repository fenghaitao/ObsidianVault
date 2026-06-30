---
title: "Lite RT"
type: entity
tags: [framework, google, on-device, inference, edge, tensorflow, pytorch, jax]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Lite RT is Google's on-device ML inference framework, built on TensorFlow Lite, rebranded to emphasize multi-framework support (TensorFlow, PyTorch, JAX). It powers on-device AI across 100,000+ apps with billions of active users.

## Key Information
- Built on the TensorFlow Lite foundation, using the TFLite file format
- Rebranded from TensorFlow Lite to emphasize support beyond TensorFlow models (PyTorch, JAX)
- 100,000+ apps, billions of active users, high daily interpreter invocations
- Cross-platform: Android, iOS, macOS, Linux, Windows, web, IoT devices
- Conversion path: PyTorch/JAX models → convert to TFLite format → quantize → deploy
- Provides CPU and GPU acceleration libraries
- NPU acceleration integrated with Qualcomm and MediaTek; additional partners in progress
- Supports ahead-of-time (AOT) and just-in-time (JIT) compilation
- Lite RT LLM path for large language models; standard Lite RT path for other models
- CLI tool with Python bindings available for easier deployment
- Performance: up to 35x faster than Llama on mobile, 3x faster on IoT, at par on desktop
- Powers on-device face unlock on Google Pixel devices
- Model Explorer tool for graph visualization and mixed-precision quantization planning
- AI Edge Portal for cloud-based benchmarking across Android device fleets

## Related
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source
- [[TensorFlow Lite]] — predecessor framework
- [[Google AI Edge]] — parent division
- [[GoogleDeepMind]] — organization
- [[Chintan Parikh]] — product manager
- [[PyTorch]] — supported framework
- [[JAX]] — supported framework
- [[Qualcomm]] — NPU integration partner
- [[MediaTek]] — NPU integration partner
- [[Gemma4]] — models running on Lite RT
- [[Raspberry Pi]] — deployment target
- [[OnDeviceAI]] — core use case
- [[NPU Acceleration]] — hardware acceleration
- [[Model Explorer (tool)]] — graph visualization tool
- [[AI Edge Portal]] — benchmarking service
- [[Ahead-of-Time Compilation]] — compilation strategy
