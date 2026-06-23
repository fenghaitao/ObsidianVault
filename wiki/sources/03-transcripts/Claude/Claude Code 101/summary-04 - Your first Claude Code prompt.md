---
title: "summary-your-first-claude-code-prompt"
type: source
tags: [source, claude-code, prompting, plan-mode, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/04 - Your first Claude Code prompt.md]
last_updated: 2026-06-23
---

## Core Summary

Effective Claude Code usage starts with descriptive prompting and choosing the right permission mode. Shift+Tab cycles between default (ask before edits and commands), auto-accept edits (auto-approves file changes but asks for commands), and plan mode (read-only analysis that produces a detailed implementation plan before execution). Plan mode excels at complex multi-step features and safe code reviews. The transcript demonstrates implementing a dark mode toggle across an app using plan mode.

## Key Points

- Be as descriptive as possible with prompts; the more context, the better the output.
- Shift+Tab cycles through permission modes: default, auto-accept edits, and plan mode.
- Plan mode uses read-only tools to analyze the codebase, ask clarifying questions, and produce a detailed plan before executing.
- Plan mode is ideal for complex changes, multi-step implementations, and safe code reviews.
- Users can stay in the loop at every step if desired, or let Claude work more autonomously.

## Related

- [[ClaudeCode]] — the tool being prompted
- [[AgenticLoop]] — the loop that executes the plan
- [[summary-03 - How Claude Code Works]] — details on permission modes
