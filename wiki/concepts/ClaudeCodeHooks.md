---
title: "ClaudeCodeHooks"
type: concept
tags: [claude-code, hooks, automation, determinism]
sources: [raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md, raw/01-articles/claude/2025-12-11 - Claude Code power user customization How to configure hooks.md]
last_updated: 2026-07-04
---

## Definition

Claude Code hooks are deterministic lifecycle event handlers that run commands at specific points during Claude Code's operation. Unlike prompt-based instructions, hooks always execute with no exceptions, providing guaranteed automation and safety enforcement.

## Key Information

- **PostToolUse** is most common: auto-format files after edits using matchers like "edit" or "multi-edit".
- **PreToolUse** can block dangerous operations: exit code 0 proceeds, exit code 2 blocks (stderr becomes Claude feedback).
- **Blocking use cases:** writes to production config, destructive shell commands, commits to protected branches.
- **Configuration:** defined in settings.json with event, optional matcher, and command.
- **Project-level:** `.claude/settings.json` can be checked into version control; use `CLAUDE_PROJECT_DIR` env var for project-relative script paths.
- **Rule of thumb:** if something needs to happen every time without fail, use a hook, not a prompt.

## The Eight Hook Events (December 2025)

Claude Code's lifecycle exposes eight hook events, covering startup through tool execution to completion:

| Event | Fires | Typical use |
|---|---|---|
| **PreToolUse** | After Claude picks a tool, before it runs | Inspect, approve, block, or modify the planned action |
| **PermissionRequest** | When Claude would show a permission dialog | Auto-allow/deny instead of prompting (e.g., auto-approve `npm test`) |
| **PostToolUse** | After a tool completes successfully | React to tool output (e.g., auto-run Prettier after Write/Edit) |
| **PreCompact** | Before Claude compacts conversation context | Back up the transcript before summarization loses detail; matcher distinguishes `auto` vs. `manual` compaction |
| **SessionStart** | On new session start or resume | Inject context (git status, TODOs) automatically into every session |
| **Stop** | When Claude finishes responding | Inspect output and force continuation (`"continue": true`) for multi-step workflows |
| **SubagentStop** | When a Task-tool subagent finishes | Same as Stop, but scoped to subagent completion |
| **UserPromptSubmit** | When a prompt is submitted, before processing | Inject dynamic context (e.g., sprint priorities) alongside the prompt |

- **Matchers** (apply to PreToolUse, PostToolUse, PermissionRequest only): exact string ("Write"), pipe-separated alternatives ("Write|Edit"), wildcard ("*"/empty matches all, case-sensitive), argument-level patterns ("Bash(npm test*)"), and MCP tool patterns (`mcp__servername__.*`).
- **Data flow**: hooks receive JSON via stdin (session_id, transcript_path, cwd, permission_mode, hook_event_name, plus tool_name/tool_input for tool hooks). Exit code 0 = success; exit code 2 = blocking error (stderr becomes Claude's feedback); other codes = non-blocking error (shown in verbose mode). Structured JSON output can set `decision`, `reason`, `continue`, and `updatedInput` directly.
- **Environment variables**: `CLAUDE_PROJECT_DIR`, `CLAUDE_CODE_REMOTE` (true in web environments), `CLAUDE_ENV_FILE` (SessionStart hooks persisting variables), plus standard shell vars.
- **Execution**: 60-second default timeout (configurable); matching hooks for the same event run in parallel; identical commands are deduplicated automatically.
- **Security**: hooks run arbitrary shell commands at the user's permission level; direct edits to hook configuration require review in the `/hooks` menu before taking effect, preventing silent malicious injection. Recommended practice: validate/sanitize stdin, quote shell variables, use absolute script paths, avoid touching `.env`/credential files.
- **Debugging**: every hook gets a `transcript_path` to a JSONL session log (`tail -f ... | jq` for live viewing); a small bash wrapper script logging tool name/event/exit-code per invocation helps debug *why* a hook approved or blocked something, which the transcript alone doesn't show.
- **Recommended starting point**: a single PostToolUse formatter hook — immediate, visible feedback — before expanding to more hooks.

## Hooks as Continuous Improvement, Not Just Guardrails (May 2026)

Most teams think of hooks primarily as scripts that prevent Claude from doing something wrong, but a more valuable use is making the setup self-improving:

- A **Stop** hook can reflect on what happened during a session and propose [[CLAUDE-md|CLAUDE.md]] updates while the context is still fresh.
- A **SessionStart** hook can load team-specific context dynamically, so every developer gets the right setup for their module without manual configuration.
- For automated checks like linting and formatting, hooks enforce rules deterministically and produce more consistent results than relying on Claude to remember an instruction each time.
- Hooks (and skills) built to compensate for specific model limitations become overhead once those limitations disappear: a hook that intercepted file writes to enforce `p4 edit` in a Perforce codebase became redundant once Claude Code added native Perforce mode — a concrete instance of the general "actively maintain your harness as models evolve" guidance. See [[CLAUDE-md]].

See [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

## Related

- [[summary-09 - Hooks in Claude Code]] — source summary
- [[ClaudeCode]] — the tool hooks extend
- [[CLAUDE-md]] — the non-deterministic alternative
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
- [[summary-2025-12-11 - Claude Code power user customization How to configure hooks]] — advanced configuration guide expanding hooks from 5 to 8 event types
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — self-improving hooks (Stop/SessionStart) and maintaining hooks as models evolve
