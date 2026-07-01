---
title: "Speech-to-Speech Models"
type: concept
tags: [voice-ai, model, speech, architecture, multimodal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
Speech-to-speech models are AI models that process speech audio directly as input and output speech audio, without intermediate text transcription. They replace the three-stage cascaded architecture (STT → LLM → TTS) with a single model, reducing latency but currently lacking the reliability, intelligence, and tool-calling capabilities of cascaded systems.

## Key Information
- Single model handles: audio input → understanding → response generation → audio output
- Reduces latency compared to cascaded systems by eliminating intermediate text stages
- Except Moshi, every speech-to-speech model (including OpenAI advanced voice mode and Sesame AI) is half duplex
- Half duplex means the model is either listening or speaking — cannot handle overlap, back-channeling, or interruptions
- Technically preserves paralinguistic information, but models trained on audio versions of instruct datasets never learn to exploit it
- Current limitation: "very stupid" compared to cascaded systems — no tool calling, poor observability, limited intelligence
- Neil Zeghidour: until speech-to-speech models match cascaded systems on reliability, intelligence, and personalization, they won't replace cascaded systems
- Moshi (from Kyutai) remains the only full-duplex speech-to-speech model as of May 2026
- Nvidia's PersonalPlex is based on Moshi's architecture
- OpenAI's real-time API and Nvidia Voice Chat are examples — both use a single model behind the scenes
- Key benefit: preserves paralinguistic information (tone, emotion, hesitation) lost in cascaded systems
- Enables full-duplex communication, better interruption handling, and back-channeling
- Most teams try speech-to-speech models but move to pipeline architecture in production due to tool calling limitations

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Cascaded Systems (Voice)]] — alternative architecture
- [[Voice Agent Pipeline Architecture]] — production pipeline architecture
- [[Full Duplex]] — key capability gap
- [[Half Duplex]] — current limitation
- [[Moshi]] — only full-duplex implementation
- [[PersonalPlex]] — Nvidia model based on Moshi
- [[Voice Chat (Nvidia)]] — Nvidia speech-to-speech model
- [[Voice AI]] — parent domain
- [[Paralinguistic Understanding]] — information preserved but unexploited
- [[Turn Detection]] — handled differently in speech-to-speech vs pipeline
