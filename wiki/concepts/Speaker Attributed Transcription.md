---
title: "Speaker Attributed Transcription"
type: concept
tags: [speech-processing, voice-ai, diarization, transcription, stt, multi-speaker]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Speaker attributed transcription is the result of combining [[Speaker Diarization]] (who speaks when) with speech-to-text (what was said) to produce a transcript where each word is labeled with the speaker who uttered it. It answers the question "who said what" and is essential for applications like meeting note-taking, video dubbing, and podcast intelligence.

## Key Information
- Combines two separate model outputs: diarization (speaker labels with timestamps) and STT (words with timestamps)
- The reconciliation between the two is non-trivial due to:
  - STT models degrading on multi-speaker audio (trained primarily on single-speaker data)
  - Timestamp disagreements between STT and diarization outputs
  - Overlapping speech: STT transcribes one speaker while diarization detects two
  - Detection mismatches: diarization may detect speech that STT doesn't transcribe, and vice versa
- Applications: meeting note-takers (assigning action items to people), automatic video dubbing (consistent voice assignment), podcast intelligence (tracking guests across episodes)
- [[pyannoteAI]] provides an STT orchestration API that handles the reconciliation automatically, supporting any STT model including fine-tuned private models
- Knowing "who said what" is often as important as knowing what was said

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Diarization]] — provides speaker labels
- [[Reconciliation (STT and Diarization)]] — the alignment problem
- [[Exclusive Diarization]] — technique for overlap handling
- [[pyannoteAI]] — provides reconciliation API
- [[PyAnnote]] — open-source diarization toolkit
- [[Whisper]] — commonly paired STT model
- [[NVIDIA Parakeet]] — STT model with per-word timestamps
- [[Overlapping Speech]] — key challenge
- [[Diarization Error Rate]] — diarization quality metric
- [[Word Error Rate]] — STT quality metric
- [[Voice AI]] — parent domain
