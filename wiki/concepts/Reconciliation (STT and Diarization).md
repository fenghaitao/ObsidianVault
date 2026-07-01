---
title: "Reconciliation (STT and Diarization)"
type: concept
tags: [speech-processing, voice-ai, stt, diarization, multi-speaker, alignment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Reconciliation is the process of aligning the outputs of [[Speaker Diarization]] (speaker labels with timestamps) and speech-to-text (words with timestamps) to produce [[Speaker Attributed Transcription]]. Despite sounding straightforward, it is a difficult problem due to timestamp disagreements, overlapping speech, and detection mismatches between the two model outputs.

## Key Information
- Core challenge: STT and diarization produce timestamps that disagree — words often fall between speaker boundaries
- Three main failure modes:
  - STT models trained on single-speaker data degrade on multi-speaker recordings (distant mics, speaker changes, crosstalk, interruptions, [[CodeSwitching]])
  - Timestamp misalignment: STT word timestamps don't match diarization speaker boundary timestamps
  - Detection mismatch: diarization may detect speech that STT doesn't transcribe, and vice versa
- Overlapping speech is particularly problematic — STT typically transcribes only one speaker while diarization detects two
- [[pyannoteAI]]'s approach: proprietary STT orchestration API that handles reconciliation, designed to work with any STT model (including fine-tuned private models)
- Key technique: [[Exclusive Diarization]] — during overlap, select the most likely speaker for STT transcription to simplify the reconciliation
- The reconciliation API can interleave words from overlapping speakers when both are correctly detected

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Attributed Transcription]] — the output of reconciliation
- [[Speaker Diarization]] — provides speaker labels
- [[Exclusive Diarization]] — key technique for simplifying reconciliation
- [[Overlapping Speech]] — primary challenge
- [[pyannoteAI]] — provides reconciliation API
- [[PyAnnote]] — open-source diarization toolkit
- [[NVIDIA Parakeet]] — STT model used in reconciliation demos
- [[Whisper]] — commonly paired STT model
