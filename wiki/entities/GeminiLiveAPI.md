---
title: "GeminiLiveAPI"
type: entity
tags: [api, google, deepmind, gemini, audio, real-time, websocket]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
The Gemini Live API is a stateful web socket API from Google DeepMind for real-time audio and video interaction with Gemini models. It enables streaming audio/video input to the model and receiving real-time audio responses, with built-in tool calling, Google Search grounding, and native multilingual support.

## Key Information
- Stateful web socket API for real-time communication
- Supports real-time text, audio, and video feeds (video at max 1 frame per second)
- Audio is streamed in buffer chunks from real-time capture
- Video can be camera feed, canvas, or screen share
- Returns real-time audio buffers and audio transcriptions
- Built-in tool calling and Google Search grounding by default
- Used by Shopify for Shopify Sidekick (tech support with screen sharing)
- Integration partners provide WebRTC: LifeKit, PipeCast, SoftwareMansion (Fish Jam), Vision Agents, Vox Implants
- Server-to-server approach: server creates web socket to Gemini, proxies to client
- Client-direct approach: ephemeral tokens for lower latency direct connections
- Coming to the Interactions API in the future (work in progress)
- Example apps available on GitHub (Python with FastAPI, JavaScript)

## Related
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — source
- [[GoogleDeepMind]] — developer
- [[ThorSchaeff]] — presenter
- [[GeminiInteractionsAPI]] — sister API (Live API coming to it)
- [[Gemini31FlashLive]] — model powering the API
- [[GoogleAIStudio]] — can be used to live-coach integrations
- [[Lyra3]] — music model used with Live API in demos
- [[GoogleSearchGrounding]] — built-in feature
- [[EphemeralTokens]] — client-direct connection method
- [[WebRTC]] — integration pattern via partners
- [[Shopify]] — enterprise user (Sidekick)
