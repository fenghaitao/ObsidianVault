---
title: "Tiny LLMs"
type: concept
tags: [models, on-device, edge, fine-tuning, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Tiny LLMs (TLMs) are language models under 1 billion parameters designed for in-app deployment on edge devices. They are typically fine-tuned for specific tasks and can achieve production-level reliability for narrow use cases like summarization, transcription, or function calling.

## Key Information
- Defined as models under 1 billion parameters for in-app GenAI deployment
- Below 500M parameters, fine-tuning is necessary for production-level reliability
- Above 500M parameters, some general-purpose tasks are possible without fine-tuning (e.g., FastVLM at 500M for scene description)
- Can achieve 85-90%+ reliability on narrow tasks when properly fine-tuned
- Workflow: larger cloud model generates synthetic data → fine-tune tiny base model → quantize → deploy
- Examples: Function Gemma (270M), Gemma 327M derivatives, FastVLM (500M, Apple)
- Deployed with the app or web page, not pre-loaded in the OS
- Target wider device reach (not just premium devices)
- Modularity pattern: separate tiny models for separate tasks, enabling reuse across features
- Contrast with system-level GenAI (2-5B parameter models built into the OS)

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[InApp GenAI]] — deployment pattern
- [[SystemLevel GenAI]] — contrasting approach
- [[Function Gemma]] — example tiny LLM
- [[FineTuning]] — required for production use
- [[Synthetic Data Generation]] — training data workflow
- [[Quantization]] — deployment optimization
- [[LiteRTLM]] — runtime for deployment
- [[AI Edge Eloquent]] — production app using tiny LLMs
