---
title: "Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind.md"
date: 2026-04-30
ingested: 2026-06-26
tags: [workshop, google-deepmind, gemini, conversational-agents, interactions-api, live-api, audio-models, coding-agents]
---

## Core Thesis
Thor Schaeff and Philipp Schmid from Google DeepMind present a hands-on workshop building conversational agents using two new Gemini APIs: the **Interactions API** (a unified API with server-side state management replacing the legacy Generate Content API) and the **Gemini Live API** (a real-time audio/video web socket API powered by native audio models). The workshop demonstrates building a coding agent with file and bash tools, then extends to real-time voice agents with multilingual support, tool calling, and music generation via Lyra 3.

## Key Topics
- **Gemini Interactions API**: Unified API for models and agents with server-side state management, implicit caching, background execution, and type-based content blocks. Designed to be less proto-specific and more aligned with industry standards (OpenAI, Anthropic).
- **Server-side state**: Previous interaction IDs eliminate the need for client-side history management, improving cache hit rates by 2-3x.
- **Agent skills**: Pre-built coding agent skills for Gemini APIs that agents can install and use, providing model awareness of latest models, documentation links, and best practices.
- **Coding agent workshop**: Building an agent class with GenAI client, read/write file tools, bash execution, and a continuous interaction loop — all using Gemini 3 Flash as the coding model.
- **Gemini Live API**: Web socket API for real-time audio/video streaming with native audio models (sound token to sound token, not cascading TTS). Supports 97 languages, voice activity detection, barge-in, tool calling, and Google Search grounding.
- **Gemini 3.1 Flash Live**: New native audio model released ~2 weeks before the talk, replacing the December 2.5 model with lower latency and better scalability.
- **Lyra 3**: Music generation model capable of creating full songs with lyrics, demonstrated as a tool call from a conversational DJ agent.
- **Live Jukebox DJ**: Demo built in Google AI Studio combining Gemini Live API with Lyra 3 for music generation via voice commands.
- **Ephemeral tokens**: Client-to-server direct connection approach for lower latency compared to server-to-server proxying.
- **Integration partners**: LifeKit, PipeCast, SoftwareMansion (Fish Jam), Vision Agents, Vox Implants provide WebRTC integrations for the Live API.

## Entities
- [[ThorSchaeff]] — Google DeepMind developer experience, Gemini API and AI Studio
- [[PhilippSchmid]] — Google DeepMind developer experience, Gemini API and AI Studio
- [[GeminiInteractionsAPI]] — Unified API for models and agents with server-side state
- [[GeminiLiveAPI]] — Real-time audio/video web socket API
- [[Gemini31FlashLive]] — New native audio model for the Live API
- [[Lyra3]] — Music generation model from Google DeepMind
- [[GoogleAIStudio]] — Web-based tool for trying Gemini models and building demos
- [[Shopify]] — Company using Gemini Live API for Shopify Sidekick tech support
- [[LifeKit]] — Integration partner for Gemini Live API WebRTC
- [[PipeCast]] — Integration partner for Gemini Live API WebRTC
- [[SoftwareMansion]] — Polish company building Fish Jam, a WebRTC service for Gemini Live API
- [[FishJam]] — WebRTC service by SoftwareMansion for Gemini Live API integration
- [[VisionAgents]] — Integration partner for Gemini Live API
- [[VoxImplants]] — Integration partner for Gemini Live API
- [[MetaRayBan]] — Smart glasses with SDK opened by Meta, compatible with Gemini Live API

## Concepts
- [[ServerSideStateManagement]] — Server maintains conversation history via interaction IDs
- [[ImplicitCaching]] — Automatic token caching on the server side for follow-up requests
- [[NativeAudioModels]] — Models processing sound tokens directly without text transcription
- [[GoogleSearchGrounding]] — Built-in real-time search capability in Gemini Live API
- [[EphemeralTokens]] — Client-direct authentication for lower latency Live API connections
- [[WebRTC]] — Real-time communication protocol for browser-based audio/video
- [[ContextCompaction]] — Technique for managing context window limits in long conversations
- [[ToolCombination]] — Combining built-in tools (e.g., Google Search) with custom functions
- [[BackgroundExecution]] — Asynchronous agent execution with polling or webhook notifications
- [[ConversationalAgents]] — AI agents designed for natural, real-time voice interaction

## Related
- [[GoogleDeepMind]] — parent organization
- [[Gemini3]] — base model used for coding
- [[NanoBananaPro]] — related Google DeepMind product
- [[AgenticLoop]] — the loop pattern used in the coding agent
- [[ToolCalling]] — underlying mechanism for the agent's tools
- [[MCP]] — remote MCP support in Interactions API
- [[PromptCaching]] — related to implicit caching benefits
- [[Skills]] — agent skills pattern used for Gemini API integration
- [[OpenClaw]] — open-source project mentioned for glasses integration
