---
title: "summary-what-are-subagents"
type: source
tags: [source, claude-code, subagents, transcript]
sources: [raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md]
last_updated: 2026-06-23
---

## Core Summary

Sub-agents are specialized assistants that Claude can delegate tasks to. Each runs in its own isolated context window with a custom system prompt, and returns only a summary to the main thread. This keeps the main context clean by hiding intermediate exploration. Built-in sub-agents include general-purpose, explore, and plan. Custom sub-agents can be created with custom system prompts and tool access. The trade-off: main thread loses visibility into how the sub-agent reached its conclusions.

## Key Points

- Sub-agents run in separate context windows; all intermediate work (file reads, edits, tool calls) stays isolated.
- Only a summary is returned to the main thread; the sub-agent's full conversation is discarded.
- **Without sub-agents:** Claude reads 15 files, runs searches, traces calls -- all filling the main context window, even if you only needed one fact.
- **With sub-agents:** you get the answer without the journey; the sub-agent explores, discovers, and returns a focused summary.
- Built-in sub-agents: general-purpose (multi-step exploration + action), explore (fast codebase searching), plan (research and analysis for plan mode).
- Custom sub-agents can be created with custom system prompts and restricted tool access.

## Related

- [[ClaudeCode]] — the tool sub-agents extend
- [[ContextWindow]] — the memory constraint sub-agents help manage
- [[summary-using-subagents-effectively]] — when sub-agents help vs. hinder
