---
title: "Agent Wrapper Pattern"
type: concept
tags: [agents, architecture, pattern, sdk, extensibility]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
The Agent Wrapper Pattern is an architectural approach where new capabilities (such as voice) are added to an existing agent by wrapping it with a lightweight SDK layer, rather than rebuilding the agent from scratch. The wrapper proxies interactions to the underlying agent while adding new input/output modalities.

## Key Information
- Preserves existing agent investments: evals, prompt engineering, tool calling, RAG infrastructure
- The wrapper sits between the user and the existing agent, translating between modalities (e.g., voice ↔ text)
- ElevenLabs Voice Engine implements this pattern: server SDK wraps the chat agent, each new session kicks off a proxy loop
- Contrasts with the "rebuild from scratch" approach that requires replacing the entire agent stack
- Enables incremental adoption: developers can add voice without changing their existing agent code
- Generalizable beyond voice: the pattern could apply to other modality upgrades (e.g., video, AR)
- Requires the underlying agent to have well-defined interfaces (tool calling, message handling)

## Related
- [[VoiceEngine]] — ElevenLabs product that implements this pattern for voice
- [[Voice Agents]] — agents created via this pattern
- [[Chat Agents]] — the underlying agents being wrapped
- [[OmniChannel Voice]] — capability unlocked by wrapping with voice
- [[AgentExtensibility]] — broader concept of extending agent capabilities
- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — source
