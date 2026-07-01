---
title: "Lyria"
type: entity
tags: [model, google, deepmind, music-generation, genmedia, audio]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Lyria is Google DeepMind's music generation model, part of the GenMedia suite. It generates songs from natural language prompts with full control over duration, instruments, BPM, scale, structure, lyrics, and language — all specified in the prompt without separate parameters.

## Key Information
- Music generation model from Google DeepMind, shipped 2 weeks before May 2026
- Two variants: Clip model (30-second songs, ~$0.04/song) and Full Song model (up to 3 minutes, ~$0.08/song)
- Prompt-only control: no API parameters for musical attributes — everything specified in natural language
- Supports intro/verse/chorus/bridge/outro structure specification
- Can generate lyrics or accept user-provided lyrics
- Output includes timed lyrics metadata (word-level timestamps) for karaoke-style applications
- Supports multi-language generation and language switching mid-song
- Can generate speech-like output with minimal or no background music (audiobook style)
- Uses streaming: lyrics delivered first via generate_content_stream, music follows
- Training data includes Gemini-written prompts, making Gemini effective at generating Lyria prompts
- Can generate music from images (e.g., a photo of ingredients inspiring a cooking song)
- Pricing: approximately $0.04 for 30s clip, $0.08 for full song

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GoogleDeepMind]] — creator
- [[GenMedia]] — product suite
- [[Lyria RealTime]] — real-time predictive variant
- [[Gemini]] — used for prompt generation
- [[Media Prompt Generation]] — pattern for generating prompts
