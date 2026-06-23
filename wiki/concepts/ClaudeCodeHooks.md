---
title: "ClaudeCodeHooks"
type: concept
tags: [claude-code, hooks, automation, determinism]
sources: [raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md]
last_updated: 2026-06-23
---

## Definition

Claude Code hooks are deterministic lifecycle event handlers that run commands at specific points during Claude Code's operation. Unlike prompt-based instructions, hooks always execute with no exceptions, providing guaranteed automation and safety enforcement.

## Key Information

- **Events:** UserPromptSubmit, PreToolUse, PostToolUse, Notification, Stop.
- **PostToolUse** is most common: auto-format files after edits using matchers like "edit" or "multi-edit".
- **PreToolUse** can block dangerous operations: exit code 0 proceeds, exit code 2 blocks (stderr becomes Claude feedback).
- **Blocking use cases:** writes to production config, destructive shell commands, commits to protected branches.
- **Configuration:** defined in settings.json with event, optional matcher, and command.
- **Project-level:** `.claude/settings.json` can be checked into version control; use `CLAUDE_PROJECT_DIR` env var for project-relative script paths.
- **Rule of thumb:** if something needs to happen every time without fail, use a hook, not a prompt.

## Related

- [[summary-hooks-in-claude-code]] — source summary
- [[ClaudeCode]] — the tool hooks extend
- [[CLAUDE-md]] — the non-deterministic alternative
