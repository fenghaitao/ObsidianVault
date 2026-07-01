---
title: "Code-switching"
type: concept
tags: [speech-processing, multilingual, stt, linguistics, voice-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Code-switching is the practice of alternating between two or more languages within a single conversation or sentence. In speech processing, it poses a significant challenge for speech-to-text models, which are typically trained on monolingual data and may fail when speakers switch languages mid-utterance.

## Key Information
- Common in multilingual communities and conversations between bilingual speakers
- Most STT models are trained on monolingual data and degrade when encountering code-switched speech
- Mentioned by [[Hervé Bredin]] as one of the factors that causes STT models to fail on multi-speaker, real-world recordings
- Contributes to the gap between benchmark STT performance and real-world performance
- Related challenges: mixed-language diarization (identifying which language each speaker is using), multilingual speaker attribution
- Particularly relevant for global applications like meeting transcription in international teams or multilingual podcast analysis

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Attributed Transcription]] — affected by code-switching
- [[Reconciliation (STT and Diarization)]] — code-switching complicates STT accuracy
- [[Whisper]] — multilingual STT model, but still challenged by code-switching
- [[Word Error Rate]] — degrades with code-switching
- [[Voice AI]] — parent domain
