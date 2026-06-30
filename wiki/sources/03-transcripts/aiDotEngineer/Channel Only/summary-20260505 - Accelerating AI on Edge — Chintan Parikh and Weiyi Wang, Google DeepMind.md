---
title: "summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind"
type: source
tags: [source, transcript, ai, edge, on-device, gemma-4, lite-rt, google-deepmind, tensorflow-lite, npu, quantization, agent-skills]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Core Summary
Chintan Parikh, product manager for Lite RT at Google AI Edge, presents the Gemma 4 Edge models (E2B and E4B), the Lite RT on-device inference framework, and the Google AI Edge gallery app. The talk covers new on-device agent capabilities (function calling, structured JSON output, chain-of-thought thinking mode), cross-platform deployment (Android, iOS, macOS, Linux, Windows, web, IoT, Raspberry Pi), and performance benchmarks showing significant speedups over alternatives. A live Raspberry Pi robot demo illustrates on-device inferencing in action.

## Key Points
- Gemma 4 E2B uses 1-2 GB RAM after quantization; E4B is heavier-duty for laptops and IoT devices
- New Gemma 4 Edge capabilities: built-in function calling (tool calling to local APIs), native structured JSON output (architectural, not prompt-engineered), chain-of-thought thinking mode, hardware-native optimization
- All Gemma models are Apache 2.0 licensed and available on Hugging Face
- Gallery app showcases on-device agent skills: Wikipedia querying, mood/sleep journaling with trend analysis, photo-to-music generation, animal sound generation — all running locally
- Users can create custom skills directly in the gallery app; community shares skills on GitHub
- Lite RT is Google's on-device ML framework, built on TensorFlow Lite, rebranded to emphasize multi-framework support (TensorFlow, PyTorch, JAX)
- Lite RT has 100,000+ apps, billions of active users, and high daily interpreter invocations
- TFLite file format is cross-platform: Android, iOS, macOS, Linux, Windows, web, IoT
- Conversion path: PyTorch/JAX models → convert to TFLite format → quantize → deploy via Lite RT
- AI Edge Portal: cloud-based benchmarking service for testing model performance across Android device fleets
- Model Explorer tool: visualize model graphs to decide which parts to quantize for mixed precision
- NPU acceleration integrated with Qualcomm and MediaTek; delivers 3-10x performance improvement for real-time AR/VR/camera applications
- Gemma models tested on Android, iOS, Linux, and Raspberry Pi
- Live demo: Raspberry Pi robot running Lite RT LLM on CPU, performing inference to respond to visual signs
- CLI tool available with Python bindings for easier deployment
- Performance: up to 13x boost on NPU accelerators, ~56 tokens/sec on iOS, 35x faster than Llama on mobile, 3x faster on IoT
- Face unlock on phones (iPhone/Pixel) already runs on-device using Lite RT (Google) or Core ML (Apple)
- Supports open-weight models beyond Gemma — any model convertible to TFLite format
- Orchestration patterns emerging: speaker/thinking agent architectures for distributing local vs cloud inference

## Related
- [[Chintan Parikh]] — speaker, product manager for Lite RT
- [[Weiyi Wang]] — speaker, Google DeepMind
- [[Lite RT]] — Google's on-device ML framework
- [[Google AI Edge]] — division at Google
- [[TensorFlow Lite]] — predecessor framework
- [[Gemma4]] — E2B and E4B Edge models
- [[GoogleDeepMind]] — creator of Gemma models
- [[HuggingFace]] — model hosting platform
- [[Raspberry Pi]] — IoT deployment target
- [[Qualcomm]] — NPU integration partner
- [[MediaTek]] — NPU integration partner
- [[PyTorch]] — supported model framework
- [[JAX]] — supported model framework
- [[OnDeviceAI]] — core concept
- [[EdgeModels]] — core concept
- [[OnDeviceAgentic]] — agentic capabilities on-device
- [[Function Calling]] — built-in capability in Gemma 4 Edge
- [[Structured Outputs]] — native JSON output in Gemma 4 Edge
- [[ChainOfThought]] — thinking mode in Gemma 4 Edge
- [[Quantization]] — model optimization for on-device
- [[Apache2License]] — license for Gemma models
- [[NPU Acceleration]] — hardware acceleration for on-device AI
- [[AI Edge Portal]] — cloud benchmarking service
- [[Model Explorer (tool)]] — graph visualization and quantization planning
- [[Ahead-of-Time Compilation]] — compilation strategy for deployment
- [[On-Device Agent Skills]] — user-created skills running locally
- [[aiDotEngineer]] — event host
