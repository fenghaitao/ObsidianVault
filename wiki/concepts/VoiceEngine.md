---
title: "VoiceEngine"
type: concept
tags: [voice, agents, elevenlabs, product, sdk, speech-to-text, text-to-speech]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Voice Engine is an ElevenLabs product that provides a first-class primitive for wrapping existing chat agents with voice capabilities. It combines speech-to-text (Scribe), text-to-speech (V3), and emotion-context-aware turn taking into a simple SDK that attaches to any existing chat agent without requiring a rebuild.

## Key Information
- **Server SDK**: Creates a client and voice engine, then adds a wrapper to the existing chat agent. Each new session kicks off a proxy loop to the existing agent.
- **Client SDK**: ~3 lines of code to add a voice widget to a site. Comes with shadcn/Vercel-style UI components.
- **Turn taking**: Emotion-context-aware — detects pauses and semantic boundaries for natural conversation flow.
- **One-prompt conversion**: Ships with a skill that analyzes a codebase, identifies the chat agent, and converts it in about one prompt.
- **Tool calling**: Existing chat agent handles tool calling; the voice wrapper proxies without needing to deal with tool calling complexity. Client-side and server-side tools supported for DOM manipulation.
- **Omni-channel**: Once voice is added, telephony and communication integrations become available out of the box.
- **Two ElevenLabs offerings**: Voice Engine (wrapper for existing agents) or full conversational agent platform (for those starting from scratch).
- Designed for developers who have already invested in building, evaluating, and prompt-engineering their chat agents and don't want to rebuild.

## Related
- [[ElevenLabs]] — company behind Voice Engine
- [[LukeHarries]] — Head of Growth, presented Voice Engine
- [[ScribeV2]] — speech-to-text model used in Voice Engine
- [[Voice Agents]] — the category of agents Voice Engine creates
- [[Chat Agents]] — the agents that Voice Engine wraps
- [[Turn Taking]] — key capability in Voice Engine
- [[Agent Wrapper Pattern]] — architectural pattern Voice Engine implements
- [[Omni-Channel Voice]] — capability unlocked by Voice Engine
- [[shadcn]] — UI component style used
- [[Vercel]] — UI component style reference
- [[Chat Agents]] — baseline paradigm Voice Engine upgrades
- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — source
