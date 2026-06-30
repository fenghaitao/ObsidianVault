---
title: "Skill Architecture"
type: concept
tags: [agents, skills, architecture, progressive-disclosure, on-device]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Skill Architecture is the structural design pattern for agent skills used in Google AI Edge Gallery. Skills consist of a skill.md file (metadata + instructions) with optional scripts/assets (JavaScript), loaded via progressive disclosure: one-line descriptions are always visible, full details load on demand, and constrained decoding ensures reliable tool calling on small models.

## Key Information
- **Structure**: skill.md (metadata + instructions) + optional scripts/assets (JavaScript)
- **Progressive disclosure**: one-line descriptions always in context; full skill.md loaded only when the model decides to use the skill
- **Three predefined tools**: load_skill (loads skill metadata), run_javascript (executes skill JavaScript), run_intent (calls Android system intents)
- **Orchestrator**: manages skill registry, loads skills on demand
- **Constrained decoding**: applied during tool calls, constrained to the specific tool being called for stronger guardrails
- **Token efficiency**: progressive disclosure is critical for edge models with limited context windows
- **Skills can extend both input** (Wikipedia, weather, CRM, local RAG) **and output** (maps, cards, music synthesis)
- **Skills can run fully offline** (local JavaScript) or call web APIs with API keys
- **Community sharing**: skills posted on GitHub discussions, featured skills promoted in the app
- **Low barrier to entry**: skills can be "vibe coded" using Gemini CLI or Claude Code
- Works with both 2B and 4B models; simpler skills and fewer concurrent skills for 2B

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Agent Skills]] — broader concept
- [[ProgressiveDisclosure]] — design pattern
- [[ConstrainedDecoding]] — reliability technique
- [[AI Edge Gallery]] — app implementing this architecture
- [[Gemma4]] — models running skills
- [[Function Calling]] — underlying capability
