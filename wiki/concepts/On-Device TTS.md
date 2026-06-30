---
title: "On-Device TTS"
type: concept
tags: [voice-ai, tts, on-device, cpu, privacy, edge-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Definition
On-device TTS (text-to-speech) refers to speech synthesis models that run locally on the user's device — specifically on a smartphone CPU, not requiring a GPU or cloud connection. This approach eliminates API costs, reduces latency, and ensures privacy by keeping all voice data on the device.

## Key Information
- "On-device" means different things to different people — for Gradium, it means smartphone CPU (not gamer GPU)
- Key benefits: zero API cost, total privacy, no cloud servers, no waiting
- Enables consumer voice apps to scale usage without burning fundraising on TTS bills
- Gradium Phonon: <100M parameters, runs on smartphone CPU, includes voice cloning
- Better than existing on-device models like Kokoro (which lacks voice cloning)
- Addresses the cost problem: TTS is the dominant cost in voice AI, far exceeding LLM costs
- Also addresses privacy concerns: users want always-on voice assistants but fear cloud data breaches
- Open to private beta from Gradium AI

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[Gradium Phonon]] — implementation example
- [[Voice AI Cost]] — problem it solves
- [[Voice Cloning]] — capability included
- [[Kokoro]] — competitor without voice cloning
- [[Edge AI]] — broader category
- [[Privacy]] — key benefit
- [[Voice AI]] — parent domain
