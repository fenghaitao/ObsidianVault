---
title: "Co-location (Voice AI)"
type: concept
tags: [voice-ai, latency, infrastructure, networking, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Co-location in voice AI refers to the practice of placing all models (STT, LLM, TTS) and the agent orchestrator in the same data center or in very close network proximity to minimize network latency between components of the voice agent pipeline.

## Key Information
- Engine latency (model processing time) is only part of the total latency — network latency between components adds significantly
- Example: 75ms network hop (e.g., US West to Europe) vs 5ms intra-datacenter = ~70ms savings
- In an optimized voice agent setup with 100-200ms engine latency per component, reducing network latency from 75ms to 5ms yields a ~30% total reduction
- Enables use of open-source models run locally rather than API calls to distant cloud providers
- Every 10ms matters in real-time voice systems
- Requires deep observability to identify and track latency sources across the pipeline
- Related to global deployments: models should be as close to end users as possible for both latency and data residency

## Related
- [[Voice Agent Pipeline Architecture]] — the architecture being co-located
- [[Auto Scaling for Voice Agents]] — related infrastructure concern
- [[Latency]] — the problem co-location solves
- [[Together AI]] — emphasizes co-location for voice AI
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
