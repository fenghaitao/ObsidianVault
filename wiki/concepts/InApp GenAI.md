---
title: "In-app GenAI"
type: concept
tags: [deployment, on-device, models, fine-tuning, mobile]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
In-app GenAI is the deployment pattern where small AI models (typically 100-500 million parameters) are loaded with an individual app or web page, custom-tuned for specific tasks, and targeted at wide device reach beyond premium devices. It contrasts with system-level GenAI where larger models are built into the OS.

## Key Information
- Models typically 100-500 million parameters, loaded with the app
- Customized via fine-tuning for specific tasks (summarization, transcription, function calling)
- Works on all devices, not just premium — important for app developer reach
- Below 500M parameters, fine-tuning is necessary for production-level reliability
- Above 500M, some general-purpose tasks possible without fine-tuning
- Workflow: synthetic data generation with large cloud model → fine-tune tiny base model → quantize → deploy in app
- Modularity pattern: separate models for separate tasks, enabling reuse across features
- Contrast with system-level GenAI: 2-5B models built into the OS, customized via prompting/skills, premium devices only

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[SystemLevel GenAI]] — contrasting approach
- [[Tiny LLMs]] — model category
- [[FineTuning]] — customization method
- [[Synthetic Data Generation]] — training data workflow
- [[Quantization]] — deployment optimization
- [[AI Edge Eloquent]] — production example
- [[Function Gemma]] — example model
