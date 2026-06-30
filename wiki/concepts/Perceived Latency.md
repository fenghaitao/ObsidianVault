---
title: "Perceived Latency"
type: concept
tags: [latency, ux, streaming, tts, real-time, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral.md"]
last_updated: 2026-06-29
---

## Definition
Perceived Latency is the user's subjective experience of system responsiveness, as distinct from actual end-to-end computation time. In TTS and conversational AI, perceived latency can be dramatically reduced by starting audio playback as soon as the first audio packet is available, even while the full utterance is still being generated.

## Key Information
- **First-packet playback**: By generating audio in patches and emitting the first packet immediately, the user hears audio begin within milliseconds. The full computation may take 60+ seconds, but the user experiences near-instant response
- **Streaming LLM integration**: In voice agents, the ideal pipeline streams text tokens from the LLM to the TTS, which starts voicing from the very first token. This means the user hears speech begin before the LLM has finished generating the complete response
- **Speech-to-text symmetry**: On the input side, real-time STT produces the transcript by the time end-of-turn is detected, eliminating transcription latency from the user's perspective
- **End-to-end agent example**: The demo showed a voice agent where: STT captured speech → small fast LLM generated response → TTS voiced it. Despite full audio not being computed upfront, the conversation felt responsive because audio packets arrived early
- **Impact on UX**: Lower perceived latency is critical for natural conversational flow. Long pauses between user speech and agent response break the illusion of natural dialogue
- **Long-form content**: Perceived latency becomes even more important for long utterances (e.g., reading a full page of text). Without streaming, the user would wait for the entire text to be generated before hearing anything

## Related
- [[summary-20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral]] — source
- [[Streaming Audio Generation]] — the technique that reduces perceived latency
- [[Text-to-Speech Architecture]] — the architecture enabling low-latency streaming
- [[Time to First Token]] — analogous metric for LLM text streaming
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — conversational agent latency considerations
