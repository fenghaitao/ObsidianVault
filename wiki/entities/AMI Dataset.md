---
title: "AMI Dataset"
type: entity
tags: [dataset, benchmark, speech, meetings, multi-speaker, diarization, transcription]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
The AMI (Augmented Multi-party Interaction) Dataset is a meeting corpus containing recordings of meetings with 4-5 participants in meeting rooms. It includes both headset microphone recordings (single-speaker quality) and distant table microphone recordings (multi-speaker, noisy). It is widely used as a benchmark for [[Speaker Diarization]] and multi-speaker speech-to-text evaluation.

## Key Information
- Meeting corpus with 4-5 participants per session
- Contains both headset microphone and distant (table) microphone recordings
- Reveals the performance gap between single-speaker and multi-speaker STT: models like [[NVIDIA Parakeet]] go from 11.4% WER (headset) to 26% WER (distant mic)
- Used to benchmark diarization systems and speaker-attributed transcription pipelines
- Illustrates key challenges: distant microphones, overlapping speech, speaker changes, crosstalk, and interruptions
- Referenced on the [[Open ASR Leaderboard]] and in diarization research

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Diarization]] — primary task benchmarked
- [[NVIDIA Parakeet]] — STT model evaluated on AMI
- [[Open ASR Leaderboard]] — benchmark platform using AMI
- [[Diarization Error Rate]] — evaluation metric
- [[Word Error Rate]] — STT metric on AMI
- [[Overlapping Speech]] — key challenge in AMI recordings
