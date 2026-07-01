---
title: "Open ASR Leaderboard"
type: concept
tags: [benchmark, speech-to-text, stt, evaluation, hugging-face, leaderboard]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
The Open ASR Leaderboard is a public benchmark hosted on [[HuggingFace]] that ranks speech-to-text (STT) models by their [[Word Error Rate]] on standard datasets. However, benchmark scores can be misleading because they typically use headset microphone recordings (single-speaker conditions), while real-world performance on multi-speaker, distant-microphone audio is significantly worse.

## Key Information
- Hosted on [[HuggingFace]]
- Ranks STT models by [[Word Error Rate]]
- [[NVIDIA Parakeet]] reports 11.4% WER on the leaderboard (headset mic on [[AMI Dataset]])
- Real-world performance on the same dataset drops to ~26% WER when using distant table microphones
- The gap illustrates that leaderboard scores are based on idealized single-speaker conditions
- Does not account for multi-speaker challenges: overlapping speech, speaker changes, crosstalk, distant microphones, [[CodeSwitching]]
- Important to consider benchmark methodology when comparing models — headset vs. distant microphone makes a large difference

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[HuggingFace]] — platform hosting the leaderboard
- [[Word Error Rate]] — primary metric
- [[NVIDIA Parakeet]] — model benchmarked on the leaderboard
- [[AMI Dataset]] — benchmark dataset used
- [[Whisper]] — commonly benchmarked STT model
- [[Speaker Diarization]] — complementary task not covered by ASR leaderboards
