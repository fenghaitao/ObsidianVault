---
title: "summary-using-subagents-effectively"
type: source
tags: [source, claude-code, subagents, best-practices, transcript]
sources: [raw/03-transcripts/Claude/Claude Code subagents/01 - Using subagents effectively.md]
last_updated: 2026-06-23
---

## Core Summary

Sub-agents help when intermediate work doesn't matter to the main thread, and hinder when each step depends on the previous step's discoveries (information gets lost in handoff). They excel at research tasks, code review (fresh eyes, no creation history), and tasks needing different system prompts (copywriting, styling). Avoid sub-agents for "expert" claims (Claude already has that knowledge), sequential pipelines (information loss between steps), and test runners (hide diagnostic output). The key question: does the intermediate work matter?

## Key Points

- **When sub-agents shine:** research where only the answer matters, code review (separate context = fresh eyes), tasks needing different system prompts (copywriting tone, design system references).
- **When sub-agents fail:** sequential pipelines (each step depends on prior discoveries), test runners (hide full output needed for diagnosis), "expert" claims (Claude already has the knowledge; overhead isn't justified).
- **Code review benefit:** a reviewer sub-agent sees changes with fresh eyes, without the history of how code was written. Project-specific review standards can be encoded in the system prompt.
- **Copywriting benefit:** Claude Code's default prompt is concise and technical; a copywriting sub-agent with different tone/audience instructions produces better marketing text.
- **Styling benefit:** a styling sub-agent that @-mentions design system files loads color variables, spacing conventions, and component patterns automatically.

## Related

- [[summary-03 - What are subagents]] — what sub-agents are
- [[summary-02 - Designing effective subagents]] — design patterns
- [[ClaudeCode]] — the tool sub-agents extend
