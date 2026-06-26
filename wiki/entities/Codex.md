---
title: "Codex"
type: entity
tags: [tool, coding-agent, open-source, openai, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Codex is OpenAI's open-source coding agent CLI. It uses a master while-loop architecture similar to Claude Code but with a Rust core, event-driven design, and kernel-based sandboxing. Being open source, it allows developers to study how coding agents work internally.

## Key Information
- Open source, allowing direct analysis of its internal architecture
- Built with a Rust core
- More event-driven than Claude Code, with more work put into concurrent threading
- Uses submission queues and event outputs for I/O handling
- Sandboxing is kernel-based (macOS Seatbelt and Linux Land), differing from Claude Code's approach
- State management handled through threading and permissions
- The real differentiator from Claude Code is the model itself (OpenAI models vs Anthropic models)
- Zoneraich personally uses Codex for hard problems and Claude Code for human-like actions requiring back-and-forth
- Open-source nature allowed hackers to use the Codex CLI with custom prompts before OpenAI released the dedicated Codex model
- Includes an "explore" sub-agent type
- **Runs on Temporal**: OpenAI Codex runs on Temporal for durability and workflow orchestration
- Peter Steinberger used Codex extensively: at peak ran almost 10 sessions simultaneously, especially when Codex with GPT 5.1 was slow; used Codex security to test NeMo Claw and found 5 sandbox breakout methods in 30 minutes
- Peter's workflow has evolved: now ~5-6 windows instead of 10 as loops got faster with improvements and fast mode

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[OpenAI]] — company behind Codex
- [[ClaudeCode]] — comparable coding agent from Anthropic
- [[MasterWhileLoop]] — shared architectural pattern
- [[SandboxingAndPermissions]] — key architectural difference
- [[Temporal]] — infrastructure Codex runs on
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source for Temporal usage
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[RyanLopopolo]] — uses Codex as primary coding agent
- [[Harness Engineering]] — discipline built around Codex
- [[Auto-compaction]] — improved in GPT 5.4 for Codex
- [[GPT 5.2]] — model that made Codex capable of full software engineering
- [[Paperclip]] — agent orchestrator supporting Codex as an employee agent
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (Peter's workflow, NeMo Claw testing)
- [[PeterSteinberger]] — heavy Codex user
- [[Nvidia]] — NeMo Claw tested with Codex security
- [[OpenClaw]] — project Peter built using Codex