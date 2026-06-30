---
title: "Streaming Audio Generation"
type: concept
tags: [tts, audio, streaming, latency, real-time, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral.md"]
last_updated: 2026-06-29
---

## Definition
Streaming Audio Generation is a TTS technique where audio is produced incrementally — frame by frame or packet by packet — rather than generating the entire audio clip before playback begins. This dramatically reduces perceived latency, which is critical for conversational AI agents where users expect natural turn-taking.

## Key Information
- **Frame-by-frame generation**: Audio is generated in patches (~80ms frames) sequentially. As soon as the first audio packet is available, playback can begin, even though full computation of the complete utterance may finish seconds later
- **Perceived latency reduction**: The user hears audio start almost immediately, creating the impression of a responsive system. In the demo, audio began playing within milliseconds while the full 60-second computation continued in the background
- **Streaming text input challenge**: For real-time conversational agents, the ideal is to start voicing text as soon as the LLM produces the first token (streaming text-to-speech). This requires architectures that can handle incremental text input
- **Architectural approaches for streaming text input**:
  - **Interleaved**: Text tokens are inserted into the same layer as audio tokens as they arrive
  - **Dual-stream**: Separate streams for audio and text, blended during inference
  - **Delayed sequence modeling**: Another proposed approach
  - No clear winner yet among these patterns
- **Current limitation**: Mistral's released model uses full-context conditioning (all text upfront), but future iterations aim for streaming text input support
- **Agent pipeline integration**: In a voice agent, the ideal flow is: speech-to-text (real-time, transcript ready at end-of-turn) → LLM (streaming text tokens) → streaming TTS (voicing from first token). This minimizes end-to-end latency

## Related
- [[summary-20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral]] — source
- [[Text-to-Speech Architecture]] — the architecture enabling streaming generation
- [[Audio Codec]] — frame-based tokenization that enables patch-level streaming
- [[Perceived Latency]] — the UX benefit of streaming
- [[Voice Cloning]] — can be combined with streaming for real-time cloned speech
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — conversational agent architecture
