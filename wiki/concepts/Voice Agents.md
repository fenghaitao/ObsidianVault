---
title: "Voice Agents"
type: concept
tags: [voice, agents, multimodal, conversational-ai, speech]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
Voice Agents are AI agents that interact with users through spoken conversation rather than text. They upgrade text-based chat agents by adding speech-to-text, text-to-speech, and turn-taking capabilities, enabling more natural, faster, and accessible interaction. Voice agents unlock omni-channel paradigms including phone lines, video calls, and web widgets.

## Key Information
- Built on top of chat agents by adding a voice layer (speech-to-text, text-to-speech, turn taking)
- Voice is a more natural medium — faster, more interactive, and more accessible for people with dyslexia or keyboard difficulties
- Once voice is added, agents can participate in phone calls, Zoom meetings, and other communication channels
- Existing chat agent tool calling and RAG infrastructure carries over — the voice layer wraps around the agent
- ElevenLabs Voice Engine provides a server SDK + client SDK approach to convert chat agents to voice agents
- Turn taking must be emotion-context-aware to handle pauses and semantic boundaries naturally
- 2025 was the year of chat agents; the prediction is that chat agents will either die or add voice
- Voice is the primary interaction paradigm for robots — no one will type on a keyboard to interact with a humanoid
- Reachy Mini uses a speech-to-speech pipeline: VAD → Parakeet STT (150ms transcription) → LLM with tool calling → Coqui TTS
- Robot-side apps handle microphone, echo cancellation, tool dispatching (movements, emotions), and camera with face tracking
- Four hard problems must all be solved simultaneously: latency (<500ms), intelligence (tool calling, complex workflows), naturalness (accent, emotion, pronunciation), and reliability at scale
- The pipeline architecture (STT → LLM → TTS) is the dominant production approach; speech-to-speech models are emerging but lack tool calling reliability

## Related
- [[Chat Agents]] — the baseline paradigm that voice agents upgrade
- [[VoiceEngine]] — ElevenLabs product for building voice agents
- [[Turn Taking]] — critical capability for natural voice interaction
- [[Omni-Channel Voice]] — interaction paradigms unlocked by voice
- [[Agent Wrapper Pattern]] — pattern for adding voice to existing agents
- [[Voice-to-Function Calling]] — related on-device voice capability
- [[ElevenLabs]] — company building voice agent infrastructure
- [[Revolut]] — company using voice agents for customer support
- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — source
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Reachy Mini]] — robot using voice agents as primary interface
- [[Speech-to-Speech Pipeline]] — pipeline powering Reachy Mini conversations
- [[Coqui]] — TTS model in the voice pipeline
- [[Parakeet]] — STT model in the voice pipeline
- [[Voice Agent Pipeline Architecture]] — the dominant production architecture
- [[Word Error Rate]] — STT quality metric
- [[Turn Detection]] — STT capability
- [[Streaming ASR]] — architectural evolution for STT
- [[Co-location (Voice AI)]] — latency optimization strategy
- [[Auto Scaling for Voice Agents]] — scaling infrastructure
- [[Thinker-Talker Pattern]] — guardrail management pattern
