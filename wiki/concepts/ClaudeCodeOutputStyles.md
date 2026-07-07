---
title: "ClaudeCodeOutputStyles"
type: concept
tags: [claude-code, output-styles, system-prompt, configuration]
sources: ["raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
---

## Definition

Claude Code output styles are files in `.claude/output-styles/` that inject instructions into the system prompt. They carry the highest instruction-following weight of any steering method and never get compacted, loading at the start of every session and caching after the first request.

## Key Information

- **Highest authority**: because output styles sit in the system prompt, they carry the strongest instruction-following weight. Use judiciously.
- **Replaces default coding instructions**: by default, a custom output style drops all of Claude Code's built-in coding instructions (how to scope changes, when to add comments, security concerns, verification habits). Without these, Claude Code behaves more like a general assistant than a software engineering assistant.
- **`keep-coding-instructions: true`**: set this in the style's frontmatter to preserve the default coding instructions alongside the custom style, rather than replacing them entirely.
- **Built-in styles**: **Proactive**, **Explanatory**, and **Learning** cover the most common needs (autonomy, teaching mode, collaborative coding) without requiring a maintained style file. Check these before writing a custom style.
- **Context cost**: moderate — loaded at session start, never compacted, cached after first request within a session.

## Comparison with Appending the System Prompt

Output styles modify or replace the system prompt and persist as files across sessions. Appending the system prompt via the `append-system-prompt` flag is additive only (does not modify Claude's default role), applies only to a single invocation, and is not persisted across sessions. See [[ClaudeCodeSystemPrompt]].

## Related

- [[summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more]] — source summary
- [[ClaudeCodeSystemPrompt]] — the additive, invocation-scoped alternative
- [[ClaudeCode]] — the tool output styles steer
- [[CLAUDE-md]] — lower-authority, non-system-prompt instruction method
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
