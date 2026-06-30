---
title: "Speech-to-Speech Pipeline"
type: concept
tags: [voice-ai, pipeline, speech, hugging-face, open-source, stt, llm, tts, tool-calling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
The Speech-to-Speech Pipeline is an open-source Hugging Face project (maintained by Andres Marafioti for 2+ years) that chains together voice activity detection, speech-to-text, LLM reasoning with tool calling, and text-to-speech to create conversational voice agents. It is the backbone of the Reachy Mini robot's voice interaction system.

## Key Information
- Architecture: VAD → Parakeet STT (transcribing every 150ms) → LLM with tool calling → Coqui TTS
- Voice Activity Detection determines when the user is speaking
- Parakeet STT provides partial transcriptions every 150ms for early reaction
- LLM generates responses and can perform tool calling (movements, camera use)
- Coqui TTS converts text responses to speech
- Robot-side app layer handles microphone input, echo cancellation, tool dispatching, camera with face tracking
- Deployed on Hugging Face Inference Endpoints with dynamic load balancing
- LLM inference separated from conversation nodes for resource efficiency
- Open source: users can modify any component or replace the pipeline entirely
- All models (Parakeet, Coqui) are also open source

## Related
- [[Andres Marafioti]] — maintainer
- [[HuggingFace]] — organization hosting the project
- [[Reachy Mini]] — primary consumer of the pipeline
- [[Voice Agents]] — parent concept
- [[Cascaded Systems (Voice)]] — the architectural pattern used
- [[Coqui]] — TTS model in the pipeline
- [[Hugging Face Inference Endpoints]] — serving infrastructure
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
