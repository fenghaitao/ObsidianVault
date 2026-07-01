---
title: "Overlapping Speech"
type: concept
tags: [speech-processing, voice-ai, diarization, stt, multi-speaker, conversation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
Overlapping speech occurs when two or more speakers talk simultaneously in a conversation. It is one of the most challenging phenomena for [[Speaker Diarization]] and speech-to-text systems, which are typically designed for and trained on single-speaker audio. Overlap can indicate interruptions, [[Back Channeling]] (e.g., "mhm," "okay"), or competitive turn-taking.

## Key Information
- Types of overlap:
  - **Interruptions**: one speaker cuts off another mid-utterance
  - **Back channeling**: short acknowledgments ("mhm," "yeah") during another speaker's turn
  - **Competitive overlap**: both speakers vying for the floor
- Most STT models (including [[Whisper]] and [[NVIDIA Parakeet]]) are trained on single-speaker data and fail to transcribe overlapping speech correctly
- Diarization systems must detect overlap to avoid misattributing speech or missing speakers entirely
- [[Exclusive Diarization]] is one technique for handling overlap — selecting the most likely speaker for STT during overlapping regions
- Missing overlap can cause loss of critical conversational information (agreement signals, emotional reactions, turn-taking dynamics)
- Overlap is culturally variable — e.g., Japanese conversations can have up to 20% overlap due to frequent [[Back Channeling]]
- Overlap detection is a key capability for understanding conversational dynamics beyond simple transcription

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Diarization]] — must detect and handle overlap
- [[Exclusive Diarization]] — technique for handling overlap
- [[Reconciliation (STT and Diarization)]] — overlap complicates reconciliation
- [[Back Channeling]] — common form of overlap
- [[Voice Activity Detection]] — overlap complicates VAD
- [[Diarization Error Rate]] — misdetection during overlap contributes to DER
- [[AMI Dataset]] — benchmark with significant overlapping speech
- [[Full Duplex]] — architecture that can handle overlap naturally
- [[Half Duplex]] — breaks on overlap
