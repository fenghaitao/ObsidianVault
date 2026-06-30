---
title: "KP Sawhney"
type: entity
tags: [person, deepmind, ai-platform, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
KP Sawhney is a software engineer on DeepMind's AI platform team. He previously worked on the deep research agent (available via the Interactions API) and now focuses on scaling and generalizing the Antigravity agent harness for a variety of use cases beyond coding.

## Key Information
- Software engineer in DeepMind's AI platform team
- Worked on the deep research agent, now available via the Gemini Interactions API
- Current focus: scaling the Antigravity harness internally for Google's giant monorepo and generalizing it for use cases beyond coding (e.g., re-architecting deep research with shared file system collaboration)
- Advocates for skills over MCP, calling MCP "a bit of a flash in the pan" but acknowledging its value for auth
- Describes skills governance as a "Darwinian" process in large organizations — only the best skills survive
- Identifies token-hungry agents as a top-of-mind scaling challenge, with quota management currently handled through brute-force limits
- Emphasizes mixing model tiers (e.g., Gemma 4 for cheap components, advanced models for specific parts) to manage costs
- Highlights evaluation as a major focus area, including using mock TPUs to test harnesses without consuming real compute
- Received an agent-generated PR review comment without manually triggering it, showcasing internal code review automation

## Related
- [[GoogleDeepMind]] — employer
- [[Ian Ballantyne]] — co-presenter
- [[Antigravity]] — agent harness/platform he works on
- [[Deep Research Agent]] — agent he previously worked on
- [[Skills]] — mechanism he prefers over MCP
- [[SkillsGovernance]] — the Darwinian curation process he describes
- [[Agent Quota Management]] — scaling challenge he discusses
- [[Model Tiering]] — cost management strategy
- [[Agent Trajectory Store]] — observability tooling
- [[Agentic Code Review]] — automated PR review he experienced
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source
