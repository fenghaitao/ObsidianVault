---
title: "Gemini31FlashLive"
type: entity
tags: [model, google, deepmind, gemini, audio, real-time]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Gemini 3.1 Flash Live is a native audio model from Google DeepMind, released approximately two weeks before April 30, 2026. It powers the Gemini Live API and the Gemini Live feature in the Gemini mobile app, processing audio as sound tokens directly rather than through a cascading text pipeline.

## Key Information
- Released ~2 weeks before April 30, 2026
- Native audio model: processes sound token to sound token, not TTS cascading
- Based on Gemini 3.1 architecture
- Replaces the previous Gemini 2.5 native audio model (from December 2025)
- Major underlying architecture rework for lower latency and better scalability
- Supports 97 languages in preview
- Can understand mixed languages (e.g., Denglish — German + English)
- Built-in voice activity detection and barge-in support
- Major improvements in tool use and instruction following
- Multiple thinking levels: no thinking (lowest latency), thinking low, thinking high
- Powers Gemini Live in the Gemini mobile app and Google Search Live
- 30 different base voices, modifiable via system instructions (e.g., "speak in a friendly Irish accent")
- Deep audio understanding allows voice modification through prompts

## Related
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — source
- [[GoogleDeepMind]] — developer
- [[GeminiLiveAPI]] — API it powers
- [[Gemini3]] — base architecture family
- [[NativeAudioModels]] — model category
- [[GoogleSearchGrounding]] — built-in capability
- [[ThorSchaeff]] — presenter who demonstrated it
