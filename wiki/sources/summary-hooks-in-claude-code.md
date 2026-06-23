---
title: "summary-hooks-in-claude-code"
type: source
tags: [source, claude-code, hooks, automation, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

Hooks provide deterministic control over Claude Code's lifecycle by running commands at specific events. Unlike CLAUDE.md instructions (which Claude may sometimes skip), hooks always run with no exceptions. Common uses: auto-formatting after edits, logging commands for compliance, blocking dangerous operations, and sending notifications. Hooks are configured in settings.json with an event, optional matcher, and command. Project-level hooks in .claude/settings.json can be checked into version control for team-wide enforcement.

## Key Points

- Hooks are deterministic: they always run, unlike prompt-based instructions which Claude may occasionally miss.
- **Events:** UserPromptSubmit (before processing), PreToolUse (before a tool call), PostToolUse (after a tool call), Notification (on notification), Stop (when Claude finishes responding).
- **PostToolUse** with matcher "edit" or "multi-edit" is the most common: auto-format files after edits (Prettier, Go format, Ruff, etc.).
- **PreToolUse** can block tool calls: hook receives tool name and input as JSON on stdin. Exit code 0 = proceed, exit code 2 = block (stderr fed back to Claude as feedback).
- Blocking examples: writes to production config, `rm -rf` commands, commits to main.
- **Project-level hooks** in `.claude/settings.json` can be checked into the repo; use `CLAUDE_PROJECT_DIR` env var to reference project scripts.
- Rule: if something needs to happen every time without fail, put it in a hook, not a prompt.

## Related

- [[ClaudeCode]] — the tool hooks control
- [[CLAUDE-md]] — the non-deterministic alternative hooks replace
- [[summary-the-claude-md-file]] — related source on CLAUDE.md
