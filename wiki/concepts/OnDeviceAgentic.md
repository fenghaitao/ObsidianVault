---
title: "OnDeviceAgentic"
type: concept
tags: [on-device, agents, mobile, edge, gemma]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
On-device agentic AI refers to the capability of running autonomous agent workflows entirely on local hardware (phones, laptops) without cloud API calls, as demonstrated by Gemma 4 running agentic skills, coding, and SVG generation in airplane mode.

## Key Information
- Gemma 4 demos show full agentic setups running on Android phones: skill selection (e.g., piano playing), coding, all in airplane mode with no API calls
- 10 parallel Gemma instances generating SVGs on a laptop at 100 tokens/sec via llama.cpp
- Enabled by architectural innovations: per-layer embeddings (PLE) stored in CPU/disk rather than GPU, effective models with fewer operating parameters
- Smallest models (E2B, E4B) can run on Android, iOS, and Raspberry Pi
- Android Studio agent mode supports offline Gemma via llama.cpp/vLLM for AI-assisted Android development
- Represents a shift from cloud-dependent AI to local, private, always-available agentic capabilities
- Use cases: offline coding assistance, on-device control, Chrome extensions, subway/airplane AI usage

## Related
- [[OnDeviceAI]] — broader concept of local AI inference
- [[Gemma4]] — model family enabling on-device agentic
- [[PerLayerEmbeddings]] — key architectural enabler
- [[EffectiveModels]] — design approach for on-device
- [[AgenticWorkflows]] — agentic capabilities
- [[LlamaCpp]] — inference framework for on-device demos
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
