---
title: "AI Edge Gallery"
type: entity
tags: [app, google, open-source, on-device, gemma, agent-skills, gallery]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Google AI Gallery (also called AI Edge Gallery) is an open-source app available on iOS and Android for experimenting with on-device AI models. It supports chat, image analysis, transcription, translation, agent skills, and benchmarking of any LiteRT-LM compatible model.

## Key Information
- Open-source app available on iOS and Android
- Built on top of LiteRT-LM and LiteRT infrastructure
- Features: basic AI chat, image analysis, transcription, translation, audio-to-function calling, agent skills
- Agent skills: load custom skills from URLs, toggle skills on/off, community skills via GitHub discussions
- Can load any LiteRT-LM file for benchmarking (shows prefill/decode stats)
- Supports third-party models (Qwen, FastVLM from Apple, etc.)
- Skills use progressive disclosure architecture with skill.md + JavaScript
- Community can post skills on GitHub discussions; featured skills promoted in the app
- Team internally built ~80 skills, many "vibe coded" using Gemini CLI or Claude Code
- Skills can run fully offline (local JavaScript) or call web APIs with API keys
- Default model for demos: Gemma 4 E4B (2B also supported but with simpler skills)
- Source code available for developers to build their own apps

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[LiteRT-LM]] — underlying runtime
- [[Google AI Edge]] — creator
- [[Gemma4]] — default models
- [[Agent Skills]] — key feature
- [[Skill Architecture]] — how skills work under the hood
- [[ProgressiveDisclosure]] — design pattern for skills
- [[ConstrainedDecoding]] — technique for reliable tool calling
