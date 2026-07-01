---
title: "NVIDIA Parakeet"
type: entity
tags: [model, speech-to-text, stt, nvidia, transcription, audio]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
NVIDIA Parakeet is a speech-to-text (STT) model from [[NVIDIA]] that provides word-level timestamps along with transcriptions. It was used by [[Hervé Bredin]] in demos to illustrate the reconciliation challenge between diarization and STT outputs. While it performs well on single-speaker audio, its accuracy degrades significantly on multi-speaker recordings with distant microphones.

## Key Information
- STT model from [[NVIDIA]]
- Reported 11.4% [[Word Error Rate]] on the [[Open ASR Leaderboard]] (headset microphone, single-speaker conditions)
- Degrades to ~26% WER on the same [[AMI Dataset]] when using distant (table) microphones with multi-speaker audio
- Provides per-word timestamps — essential for [[Speaker Attributed Transcription]]
- The degradation illustrates a key challenge: most STT models are trained on single-speaker data and fail on multi-speaker recordings with overlap, speaker changes, and distant mics
- Used in combination with [[PyAnnote]] diarization models via [[pyannoteAI]]'s STT orchestration API to produce speaker-attributed transcription

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[NVIDIA]] — creator
- [[Whisper]] — alternative STT model
- [[Word Error Rate]] — quality metric
- [[Open ASR Leaderboard]] — benchmark platform
- [[AMI Dataset]] — benchmark dataset
- [[PyAnnote]] — diarization toolkit commonly paired with STT models
- [[Speaker Attributed Transcription]] — application combining STT with diarization
- [[Reconciliation (STT and Diarization)]] — challenge of aligning STT and diarization outputs
