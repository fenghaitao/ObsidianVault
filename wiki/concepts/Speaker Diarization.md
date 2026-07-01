---
title: "Speaker Diarization"
type: concept
tags: [speech-processing, voice-ai, speaker-identification, diarization, multi-speaker, audio]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Speaker diarization is the task of answering "who speaks when" in an audio recording. Given an audio stream containing a conversation, it partitions the audio into speaker-labeled segments, outputting anonymous labels such as "Speaker A," "Speaker B," etc. It is a foundational building block for conversation understanding and speaker-attributed transcription.

## Key Information
- Core question: "who speaks when?"
- Pipeline components: [[Voice Activity Detection]] (is anyone speaking?) → Segmentation (finding speaker change points and overlap regions) → Speaker clustering (assigning anonymous identities to speech turns)
- Key challenges that make it a hard unsolved problem:
  - The number of speakers is unknown in advance
  - Speaker labels are anonymous (not "John" or "Hervé" but "Speaker A, B, C")
  - Overlapping speech must be detected and handled
  - Very short speech turns (e.g., [[Back Channeling]]) must not be missed
  - Speaker time imbalance (one dominant speaker, others barely speak) creates statistical challenges
  - Acoustic conditions (noise, distance, reverberation) degrade performance
- Among the most downloaded model categories on [[HuggingFace]], alongside STT models
- Performance varies dramatically by scenario: ~8% [[Diarization Error Rate|DER]] on clean two-person phone calls, ~41% DER in noisy multi-speaker restaurant settings
- Popularized as a complement to [[Whisper]], which provides transcription but not speaker labels
- [[PyAnnote]] is the leading open-source toolkit for speaker diarization

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Attributed Transcription]] — combining diarization with STT
- [[Voice Activity Detection]] — first stage of the diarization pipeline
- [[Diarization Error Rate]] — evaluation metric
- [[Overlapping Speech]] — key challenge
- [[Exclusive Diarization]] — technique for handling overlap
- [[Reconciliation (STT and Diarization)]] — aligning with transcription
- [[PyAnnote]] — leading open-source toolkit
- [[pyannoteAI]] — company commercializing diarization
- [[Hervé Bredin]] — creator of PyAnnote
- [[Whisper]] — commonly paired STT model
- [[HuggingFace]] — model distribution platform
- [[AMI Dataset]] — benchmark dataset
- [[Back Channeling]] — short speech turns that diarization must capture
- [[Voice AI]] — parent domain
