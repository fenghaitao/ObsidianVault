---
title: "Voice AI Cost"
type: concept
tags: [voice-ai, cost, tts, economics, on-device, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Definition
Voice AI Cost refers to the economic challenge of running voice AI at consumer scale. TTS (text-to-speech) is the dominant cost driver, far exceeding LLM costs, speech-to-text costs, and diarization. This has led startups to burn their fundraising on TTS API bills, making voice AI economically unviable for consumer applications without on-device processing.

## Key Information
- Cost breakdown for consumer voice apps: LLM is almost nothing, STT is very cheap, diarization is affordable, TTS consumes most of the budget
- Hyperscaler voice modes (OpenAI, etc.) run at a loss — it's a marketing initiative using "gigantic multimodal models"
- Startups have burned their fundraising on TTS bills without getting user growth
- On-device TTS (running on smartphone CPU) is the proposed solution: zero API cost
- Gradium Phonon enables consumer voice apps to scale without per-query API fees
- The always-on nature of future voice assistants (several hours/day) makes cost even more critical
- Voice is not a commodity — the cost problem requires science and engineering to solve

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[OnDevice TTS]] — proposed solution
- [[Gradium Phonon]] — implementation of on-device TTS
- [[Voice AI]] — parent domain
- [[TTS]] — the dominant cost driver
- [[OpenAI]] — runs voice mode at a loss
