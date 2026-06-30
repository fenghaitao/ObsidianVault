---
title: "Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md"
author: "Luke Harries"
date: 2026-05-09
ingested: 2026-06-29
---

## Core Thesis

Chat agents became the default UI paradigm in 2025, but voice is a more natural, faster, and accessible medium. The next step is upgrading all chat agents into voice agents. ElevenLabs is releasing "Voice Engine" — a first-class primitive that wraps existing chat agents with voice capabilities (speech-to-text, text-to-speech, emotion-aware turn taking) via a simple SDK, without requiring developers to rebuild their agents.

## Key Points

- **2025: Year of chat agents**: Apps like Linear, PostHog, and gov.uk moved their home screens to chat interfaces. Chat is declarative, supports tool calling and RAG, and is a great quick start — but it doesn't feel like building the future.
- **Voice as natural medium**: Voice is quicker, more interactive, and more accessible for people who struggle with keyboards or dyslexia. It's also omni-channel — once you add voice, you unlock phone lines, Zoom calls, and other interaction paradigms.
- **Voice Engine product**: ElevenLabs took their voice engine stack (speech-to-text with Scribe, text-to-speech with V3, emotion-context-aware turn taking) and wrapped it into a first-class primitive that attaches to existing chat agents.
- **Developer experience**: Server SDK creates a client and voice engine, then adds a wrapper to the existing chat agent. Each new session kicks off a loop that proxies to the existing agent. Client SDK is ~3 lines to add a widget to a site. UI components built on shadcn/Vercel style.
- **One-prompt conversion**: Voice Engine ships with a skill that analyzes a codebase, identifies the chat agent, and converts it to a voice agent in about one prompt.
- **Tool calling**: Most tool calling is handled by the existing chat agent backend. The voice wrapper doesn't need to deal with tool calling issues. ElevenLabs also supports client-side and server-side tools for DOM manipulation.
- **Two offerings**: Voice Engine (wrapper for existing agents) or full conversational agent platform (out-of-the-box for those starting from scratch).
- **Prediction**: Chat agents will either die or start adding voice.

## Entities Mentioned

- [[LukeHarries]] — Speaker, Head of Growth at ElevenLabs
- [[ElevenLabs]] — Company building Voice Engine, Scribe, and TTS models
- [[Revolut]] — Customer using ElevenLabs for customer support voice agents
- [[Linear]] — Example app that moved home screen to chat interface
- [[PostHog]] — Example app that moved home screen to chat interface
- [[ScribeV2]] — ElevenLabs speech-to-text model, referenced as "Scribe" in Voice Engine
- [[Vercel]] — UI component style reference for Voice Engine widgets
- [[shadcn]] — UI component library used for Voice Engine widgets
- [[Zoom]] — Video platform; voice agents can join calls as an omni-channel use case

## Concepts Introduced

- [[Voice Agents]] — Agents with voice interaction capability, upgraded from chat agents
- [[Chat Agents]] — Text-based AI agents as default app interface; the baseline that voice agents upgrade
- [[VoiceEngine]] — ElevenLabs product: a wrapper primitive for adding voice to existing chat agents
- [[Turn Taking]] — Emotion-context-aware detection of pauses and semantic boundaries in voice interactions
- [[Omni-Channel Voice]] — Voice enabling multiple interaction paradigms: web widgets, phone lines, video calls
- [[Agent Wrapper Pattern]] — Wrapping existing agents with new capabilities via lightweight SDK without rebuilding

## Related

- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — also from ElevenLabs (speech-to-text, Scribe V2)
- [[summary-20260501 - Mastering AI Pricing — Mayank Pant, Stripe]] — ElevenLabs pricing model discussed
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — related Voice-to-Function Calling concept
