---
title: "Diarization Error Rate"
type: concept
tags: [metrics, evaluation, speaker-diarization, speech-processing, voice-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Diarization Error Rate (DER) is the standard evaluation metric for [[Speaker Diarization]] systems. It measures the percentage of time where the diarization output differs from the ground truth reference, computed as the sum of three error types (confusion, false alarm, and misdetection) divided by the total speech duration.

## Key Information
- Formula: DER = (confusion + false alarm + misdetection) / total speech duration
- Three error components:
  - **Confusion**: a speech segment is assigned to the wrong speaker
  - **False alarm**: speech is detected where there is none in the ground truth
  - **Misdetection**: speech in the ground truth is missed by the system
- Speaker labels are anonymous — swapping "Speaker A" and "Speaker B" produces the same DER (labels are permutable)
- Performance varies dramatically by use case:
  - ~8% DER: clean two-person telephone conversations (near state-of-the-art)
  - ~41% DER: noisy multi-speaker restaurant scenarios (far from solved)
- [[PyAnnote]] Metrics library provides DER computation
- DER does not account for speaker identity (who is "John" vs "Hervé") — it only evaluates anonymous diarization accuracy

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Diarization]] — task evaluated by DER
- [[PyAnnote]] — provides DER computation via PyAnnote Metrics
- [[AMI Dataset]] — benchmark dataset used for DER evaluation
- [[Word Error Rate]] — analogous metric for STT
- [[Open ASR Leaderboard]] — benchmark platform
