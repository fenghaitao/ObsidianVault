---
title: "ClaudeCodeSubagents"
type: concept
tags: [claude-code, subagents, context, delegation]
sources: [raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md, raw/03-transcripts/Claude/Claude Code subagents/01 - Using subagents effectively.md, raw/03-transcripts/Claude/Claude Code subagents/02 - Designing effective subagents.md, raw/03-transcripts/Claude/Claude Code subagents/04 - Creating a subagent.md]
last_updated: 2026-06-23
---

## Definition

Claude Code sub-agents are specialized assistants that run in isolated context windows with custom system prompts. Claude delegates tasks to them, and they return only a summary -- keeping the main context clean by hiding intermediate exploration.

## Key Information

- **Isolation:** each sub-agent runs in its own context window; all intermediate work (file reads, edits, tool calls) stays isolated and is discarded after the summary is returned.
- **Built-in sub-agents:** general-purpose (multi-step exploration + action), explore (fast codebase searching), plan (research and analysis for plan mode).
- **Custom sub-agents:** created via `/agents` command; markdown files with YAML frontmatter (name, description, tools, model, system prompt).

### When to Use

- **Good for:** research tasks (only the answer matters), code review (fresh eyes, no creation history), tasks needing different system prompts (copywriting tone, design system references).
- **Bad for:** sequential pipelines (information loss between steps), test runners (hide diagnostic output), "expert" claims (Claude already has the knowledge; overhead isn't justified).
- **Key question:** does the intermediate work matter? If not, delegate it.

### Design Principles

- **Structured output format:** the most important improvement; creates natural stopping points and prevents over-researching.
- **Obstacle reporting:** explicitly ask for workarounds, environment quirks, special flags so the main thread doesn't rediscover them.
- **Specific descriptions:** guide both when the main agent launches the sub-agent and what input prompt it writes.
- **Limited tool access:** read-only for research, bash for diff, edit/write only for code-changing agents.
- **Model selection:** Haiku (fast), Opus (complex), Sonnet (balanced), or inherit (same as main conversation).

## Related

- [[summary-03 - What are subagents]] — source summary
- [[summary-01 - Using subagents effectively]] — when to use
- [[summary-02 - Designing effective subagents]] — design patterns
- [[summary-04 - Creating a subagent]] — creation tutorial
- [[ClaudeCode]] — the tool sub-agents extend
- [[ContextWindow]] — the memory constraint sub-agents help manage
- [[ClaudeCodeSkills]] — skills vs. sub-agents comparison
