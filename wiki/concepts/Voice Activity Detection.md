---
title: "Voice Activity Detection"
type: concept
tags: [speech-processing, voice-ai, audio, diarization, vad]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Voice Activity Detection (VAD) is the task of determining whether human speech is present in an audio signal at a given time. It is the first stage in [[Speaker Diarization]] pipelines and a critical component of voice agent architectures, where it determines when a user is speaking versus when there is silence or non-speech audio.

## Key Information
- Binary classification: speech vs. non-speech at each time frame
- First stage of the [[Speaker Diarization]] pipeline — before segmentation and speaker clustering
- In voice agents: used to detect when a user starts and stops speaking (related to but distinct from [[Turn Detection]], which is about conversational semantics)
- Variants include [[Semantic VAD]] (Gradium AI), which understands conversational intent beyond just audio presence
- Challenges: distinguishing speech from background noise, handling overlapping speech, low-energy speech (whispers, trailing ends of utterances)
- Serves as a gate: only audio segments classified as speech proceed to downstream processing (STT, diarization)
- Critical for efficiency — prevents processing silence and non-speech audio through expensive models

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Speaker Diarization]] — uses VAD as first stage
- [[Turn Detection]] — related but semantically-aware variant
- [[Semantic VAD]] — conversational-intent-aware VAD
- [[Voice Agent Pipeline Architecture]] — VAD is a component
- [[Overlapping Speech]] — complicates VAD
- [[PyAnnote]] — includes VAD in its pipeline
- [[Voice AI]] — parent domain
