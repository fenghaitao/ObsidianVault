---
title: "MLX Audio"
type: entity
tags: [tool, mlx, audio, speech, on-device-ai, apple-silicon, tts, stt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
MLX Audio is an audio framework built on MLX for Apple Silicon, providing speech-to-text, text-to-speech (via Marvis), and speech-to-speech capabilities through a modular pipeline architecture — all running completely on-device.

## Key Information
- Built by Prince Canuma (Neywa Labs) on top of MLX
- Three core capabilities: speech-to-text (STT), text-to-speech (TTS via Marvis), speech-to-speech
- Marvis TTS generates audio in under 100 milliseconds
- Modular speech pipeline: chain independent ASR → LLM → TTS components
- Modular pipeline allows adjusting to hardware budget by selecting different models for each stage
- Supports both Python (faster iteration) and Swift (native experiences)
- Enables voice control of computers (Jarvis-like vision)
- Used in Locally AI app for voice capabilities (speaking back to users)
- Powers the Richie Mini robot with audio perception and voice cloning
- Can replace cloud-based dictation tools (WhisperFlow, Super Whisper) with on-device alternatives

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[MLX]] — underlying framework
- [[Prince Canuma]] — creator
- [[Neywa Labs]] — company behind it
- [[Marvis]] — TTS model used in MLX Audio
- [[MLX VLM]] — companion vision framework
- [[Locally AI]] — app using MLX Audio for voice
- [[Richie Mini]] — robot powered by MLX Audio
- [[Modular Speech Pipeline]] — key architectural concept
- [[WhisperFlow]] — cloud dictation alternative
- [[Super Whisper]] — cloud dictation alternative
- [[OnDeviceAI]] — core concept
