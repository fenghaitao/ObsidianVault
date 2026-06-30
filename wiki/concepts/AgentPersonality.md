---
title: "AgentPersonality"
type: concept
tags: [ai, agents, design, user-experience, personality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
Agent personality is the deliberate design of an AI agent's communication style, tone, and character to feel natural and human in specific contexts. It goes beyond basic politeness to match the norms of the communication channel and create delightful, memorable interactions. Personality can be a decisive factor in model selection, potentially outweighing technical performance metrics.

## Key Information
- Peter Steinberger pioneered the soul.md concept for OpenClaw after noticing Claude Code's default personality didn't fit WhatsApp conversations
- The realization came from using WhatsApp relay: "even though Claude Code already has some personality, it didn't really fit how people would write to you on WhatsApp"
- Key iteration goals: less wordy, fewer dots, matching how friends text — "try to write more like a human"
- This led to the soul.md file that defines the agent's personality, which became one of OpenClaw's distinctive features
- "The world changed" from 2023-2024 when AI was just a search replacement (no personality needed) to the agent era where personality matters
- "If my agent is going to text my friends on WhatsApp, it needs to feel right"
- Delightful details matter: OpenClaw includes roasting messages for users — "those are the delightful details you'll just not get if you prompt in a high level"
- Personality is an application of "taste" — the agent shouldn't "stink like AI"
- swyx noted: "I don't think people worked on enough soul until you came along"
- **Viktor model selection insight**: Fryderyk Wiatrowski reported that when Viktor's team tested GPT 5.4 as a replacement for Opus 4.6, it was actually better at tool calling and code generation and cheaper — but users rejected it. They "loved Opus" and "started raging when we did the AB test." Fryderyk noted "there is something beautiful in that model." Viktor's Opus has a slightly sassy tone that users appreciate. This demonstrates that personality can be the deciding factor in model selection, outweighing raw capability and cost
- Fryderyk lists "Make it friendly" as one of three pillars for a great AI coworker: "it makes a difference and you should make sure that Viktor likes your team. Your team likes Viktor."
- The concept connects to the broader shift from AI as tool to AI as collaborator with a distinct identity

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[OpenClaw]] — project that pioneered soul.md
- [[PeterSteinberger]] — creator of the soul.md concept
- [[ClaudeCode]] — baseline personality that didn't fit WhatsApp
- [[Taste (Software)]] — the broader quality framework personality is part of
- [[AgentIdentity]] — related concept
- [[WhatsApp]] — platform that drove the personality iteration
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (model personality degradation critique)
- [[Kitze]] — "box of oatmeal" critique of GPT-5 personality
- [[Agent Unreliability]] — personality degradation as a reliability failure mode
- [[Viktor]] — AI employee where personality drove model selection (Opus 4.6 over GPT 5.4)
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
- [[AI Employee]] — role where personality is critical for adoption
- [[Anthropic]] — provider of Opus 4.6, the model users preferred for its personality
