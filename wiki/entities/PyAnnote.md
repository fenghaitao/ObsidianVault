---
title: "PyAnnote"
type: entity
tags: [toolkit, open-source, speaker-diarization, speech-processing, python, hugging-face]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI.md"]
last_updated: 2026-06-30
---

## Definition
PyAnnote is an open-source Python toolkit for speaker diarization — the task of answering "who speaks when" in audio recordings. Created by [[Hervé Bredin]] and developed over many years, it became widely popular as a complement to [[OpenAI]]'s [[Whisper]] speech-to-text model, which provides transcription but not speaker labels. The toolkit has approximately 10,000 GitHub stars.

## Key Information
- Created by [[Hervé Bredin]], now Chief Science Officer at [[pyannoteAI]]
- Open-source Python toolkit focused on [[Speaker Diarization]]
- ~10K GitHub stars as of June 2026
- Popularity surged after [[Whisper]] release — users combined PyAnnote (speaker labels) with Whisper (transcription)
- Core components: [[Voice Activity Detection]], speech turn segmentation, speaker clustering
- Community One model: free, open-source diarization pipeline available on [[HuggingFace]]
- Works with PyTorch; can run locally on Mac (MPS backend) or GPU
- Ecosystem includes: PyAnnote Metrics (for computing [[Diarization Error Rate|DER]]), i-pyanno (interactive visualization widget)
- Tutorials and demo notebooks available on GitHub

## Related
- [[summary-20260605 - Beyond Transcription： Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI]] — source
- [[Hervé Bredin]] — creator
- [[pyannoteAI]] — company built around the toolkit
- [[Speaker Diarization]] — core task
- [[Whisper]] — commonly paired STT model
- [[OpenAI]] — creator of Whisper
- [[HuggingFace]] — model distribution platform
- [[Diarization Error Rate]] — evaluation metric
- [[Voice Activity Detection]] — pipeline component
