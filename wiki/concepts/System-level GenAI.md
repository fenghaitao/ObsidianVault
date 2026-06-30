---
title: "System-level GenAI"
type: concept
tags: [deployment, on-device, os-integration, models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
System-level GenAI is the trend of building larger AI models (2-5 billion parameters) directly into the mobile operating system, providing a central foundation model pre-loaded on premium devices with APIs available to all apps. It contrasts with in-app GenAI where smaller models are loaded per-app.

## Key Information
- Models in the 2-5 billion parameter range, built into the OS
- Available on premium devices only
- Customized via prompting or skills (not fine-tuning)
- Android implementation: AI Core with summarization APIs, prompt API, expanding capabilities
- Apple implementation: Apple Intelligence
- Both major mobile OS vendors making similar architectural choices
- Gemma 4 E2B and E4B are on the AI Core roadmap
- Contrast with in-app GenAI: smaller models (100-500M) loaded per-app, fine-tuned for specific tasks, wider device reach

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[In-app GenAI]] — contrasting approach
- [[AI Core]] — Android implementation
- [[AppleIntelligence]] — Apple implementation
- [[Gemma4]] — models on the roadmap
- [[Android]] — platform
- [[iOS]] — platform
