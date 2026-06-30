---
title: "Text-to-Speech Architecture"
type: concept
tags: [tts, speech, audio, llm-architecture, autoregressive, transformer, streaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral.md"]
last_updated: 2026-06-29
---

## Definition
Text-to-Speech (TTS) Architecture refers to the emerging dominant pattern for generating speech from text, which has converged toward an LLM-inspired design: an autoregressive decoder backbone processes audio tokens produced by a neural audio codec, generating audio frame-by-frame (patches) rather than sample-by-sample or all at once.

## Key Information
- **Convergence pattern**: Most modern TTS systems use an autoregressive decoder backbone (like LLMs), an encoder that transforms audio frames (~80ms) into tokens, and a decoder that converts tokens back to audio
- **Audio codec**: Raw audio is compressed into token sequences by a neural codec trained with a bottleneck, reconstruction losses, adversarial losses, and semantic losses. Each frame (80ms) becomes multiple tokens (e.g., 37 tokens), reducing the problem to ~500 tokens/sec
- **Frame-level generation**: Rather than generating one sample at a time (too slow) or the entire audio at once (no streaming), systems generate one frame (patch) at a time. A smaller model (often a diffusion transformer) handles per-frame token generation
- **Mistral's variation**: Instead of autoregressive per-token generation within a frame, Mistral generates all tokens of a frame simultaneously using a diffusion model with flow matching
- **Conditioning**: Two categories — full-context upfront (all text provided before generation starts) and streaming text input (text arrives incrementally). Streaming approaches include interleaved audio/text layers and dual-stream architectures; no clear winner yet
- **Scale**: Backbone transformers can be large (4 billion parameters in Mistral's case), but frame-level processing keeps computation manageable
- **Historical progression**: Word stitching (prehistoric) → sample-by-sample generation → whole-audio generation → patch-based autoregressive generation (current dominant pattern)

## Related
- [[summary-20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral]] — source
- [[Audio Codec]] — the tokenization layer
- [[Autoregressive Decoder Backbone]] — the LLM-like core component
- [[Streaming Audio Generation]] — the latency optimization enabled by this architecture
- [[Flow Matching]] — generative technique used in Mistral's variant
- [[DiffusionModels]] — related generative approach for per-frame token generation
- [[Voice Cloning]] — downstream capability enabled by TTS architectures
- [[Perceived Latency]] — UX benefit of patch-based generation
- [[TransformerArchitecture]] — the underlying neural architecture
