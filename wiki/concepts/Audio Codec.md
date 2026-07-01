---
title: "Audio Codec"
type: concept
tags: [audio, speech, tokenization, compression, neural-codec, tts]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral.md"]
last_updated: 2026-06-29
---

## Definition
An Audio Codec in the context of neural TTS is a learned compression system that transforms raw audio waveforms into discrete token sequences suitable for autoregressive language modeling. It uses a bottleneck architecture trained with multiple losses to discard perceptually irrelevant information while preserving acoustic features like voice identity and prosody.

## Key Information
- **Frame-based processing**: Audio is cut into frames of ~80 milliseconds (12 frames per second). Each frame is decomposed into multiple tokens (e.g., 37 tokens per frame in Mistral's codec, yielding ~500 tokens/sec)
- **Training procedure**: The codec is trained to reconstruct a large corpus of audio through a bottleneck. Losses include reconstruction loss, adversarial loss (discriminator), and semantic loss (ensuring text content is recoverable from certain tokens)
- **Information compression**: Raw audio requires ~200,000 bits/sec (MP3 quality). The codec compresses this to a few thousand bits/sec. By comparison, text-only semantic content is only ~15 bits/sec
- **Guided information retention**: The training losses guide the codec to drop useless information while retaining: acoustic features (voice timbre, prosody), semantic content (what is being said), and paralinguistic cues (emotion, accent)
- **Role in TTS pipeline**: The codec serves as the bridge between continuous audio and discrete token sequences. An encoder converts audio to tokens; a decoder converts tokens back to audio. This enables the use of LLM-style autoregressive transformers for speech generation
- **Token vocabulary**: Each token carries limited information (~10 bits for a vocabulary of ~1000), necessitating multiple tokens per frame to capture the full richness of audio

## Related
- [[summary-20260509 - Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral]] — source
- [[TextToSpeech Architecture]] — the broader architecture using audio codecs
- [[AudioTokenizer]] — related concept for audio input processing (speech recognition)
- [[Tokenization]] — the general concept of converting data to tokens
- [[Streaming Audio Generation]] — enabled by frame-based tokenization
- [[Voice Cloning]] — relies on codec's ability to preserve voice identity
