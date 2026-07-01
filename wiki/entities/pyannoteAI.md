---
title: "pyannoteAI"
type: entity
tags: [company, voice-ai, speaker-diarization, speech-processing, open-source, startup]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
pyannoteAI is a company focused on conversation understanding, building on top of transcription with speaker diarization, speaker-attributed transcription, and enriched conversation analysis. It offers both open-source models (Community One) and premium cloud API models (Precision-2), as well as an STT orchestration service that reconciles diarization outputs with speech-to-text timestamps.

## Key Information
- Co-founded by [[Hervé Bredin]] (Chief Science Officer), a former academic researcher
- Mission: go beyond transcription to understand conversations — who said what, when, how, and to whom
- Built on the [[PyAnnote]] open-source toolkit (~10K GitHub stars)
- Offers two tiers of diarization models:
  - **Community One**: open-source, free-to-use speaker diarization model
  - **Precision-2**: premium cloud API model with lower error rates
- Provides an STT orchestration API that reconciles diarization and transcription timestamps
- The reconciliation approach is proprietary but works with any STT model (including fine-tuned private models)
- Key technique: [[Exclusive Diarization]] — during overlapping speech, selects the most likely speaker for STT transcription
- Ecosystem includes: PyAnnote Metrics (evaluation), i-pyanno (interactive visualization), SDK for premium models
- Tutorials and demos available on GitHub

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Hervé Bredin]] — co-founder and Chief Science Officer
- [[PyAnnote]] — open-source speaker diarization toolkit
- [[Speaker Diarization]] — core technology
- [[Speaker Attributed Transcription]] — key product capability
- [[Exclusive Diarization]] — proprietary technique for overlap handling
- [[Reconciliation (STT and Diarization)]] — STT orchestration service
- [[Diarization Error Rate]] — evaluation metric
- [[HuggingFace]] — model distribution platform
