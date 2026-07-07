---
title: "ClaudeCodeSystemPrompt"
type: concept
tags: [claude-code, system-prompt, configuration, invocation]
sources: ["raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
---

## Definition

Appending the system prompt is a Claude Code invocation method that adds instructions to Claude's default system prompt via the `append-system-prompt` flag. Unlike [[ClaudeCodeOutputStyles|output styles]], it is purely additive — it does not modify or replace Claude's default role — and applies only to a single invocation rather than persisting as a file across sessions.

## Key Information

- **Additive, not replacement**: the `append-system-prompt` flag adds instructions on top of Claude's default system prompt. It does not strip away the built-in coding instructions the way a custom output style does by default.
- **Invocation-scoped**: passed at invocation time and applies only to that specific invocation. Not persisted as a file across sessions.
- **Context cost**: can be higher than other methods since it increases input tokens. Prompt caching reduces this cost after the first request in a session.
- **Output token impact**: instructing Claude to use a more verbose or longer style also increases output tokens.
- **Diminishing returns**: the more instructions provided via this method, the less strictly Claude will follow them, particularly if any contradict each other.
- **Best for**: specific coding standards, output formatting, or domain-specific knowledge that should apply to a single session rather than every session.

## Comparison with Output Styles

Output styles modify or replace the system prompt and persist as files across all sessions. Appending the system prompt is additive only, applies to a single invocation, and does not persist. The key trade-off: output styles have stronger adherence but broader (potentially unintended) effects; system prompt appending is scoped but weaker. See [[ClaudeCodeOutputStyles]].

## Related

- [[summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more]] — source summary
- [[ClaudeCodeOutputStyles]] — the system-prompt-modifying alternative
- [[ClaudeCode]] — the tool this flag steers
- [[CLAUDE-md]] — the persistent, project-level instruction method
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
