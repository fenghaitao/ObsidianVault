---
title: "Samuel Humeau"
type: entity
tags: [person, ai-scientist, speech, tts, mistral]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral.md"]
last_updated: 2026-06-29
---

## Definition
Samuel Humeau is an AI scientist at Mistral AI working on speech generation and text-to-speech. He previously worked at Facebook FAIR (when it was still called Facebook). He presented Mistral's first open-source TTS model at the aiDotEngineer conference.

## Key Information
- AI scientist at Mistral AI, focused on speech generation and text-to-speech
- Previously worked at Facebook FAIR (Facebook AI Research)
- Presented Mistral's first open-source TTS model, which uses a 4-billion-parameter transformer backbone with flow matching for frame-level token generation
- Advocates for voice identity as a branding concept — companies defining how they sound, analogous to visual brand identity
- The Mistral TTS model achieves 17ms latency from text input to first playable audio (single GPU, excluding network)
- Voice cloning encoder is kept proprietary to prevent misuse, while model weights and inference code are open source

## Related
- [[Mistral AI]] — his employer
- [[summary-20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral]] — source
- [[TextToSpeech Architecture]] — the architecture pattern he described
- [[Voice Cloning]] — capability of the model he presented
- [[Flow Matching]] — technique used in Mistral's TTS model
- [[Audio Codec]] — neural audio compression approach used in the architecture
- [[Streaming Audio Generation]] — streaming approach for low-latency TTS
