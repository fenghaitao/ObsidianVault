---
title: "summary-2025-12-11 - Claude Code power user customization How to configure hooks"
type: source
tags: [source, claude-code, hooks, automation]
sources: ["raw/01-articles/claude/2025-12-11 - Claude Code power user customization How to configure hooks.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's advanced configuration guide for [[ClaudeCodeHooks|Claude Code hooks]], covering all eight hook event types (an expansion from the five documented previously), their JSON configuration format, matcher syntax, exit-code/structured-JSON control flow, environment variables, security safeguards, and debugging via transcript files and wrapper scripts.

## Key Points

- **Eight hook events**: PreToolUse (inspect/approve/block/modify before a tool runs), PermissionRequest (intercept the permission dialog itself to auto-allow/deny/still-ask), PostToolUse (react after a tool completes, e.g., auto-run Prettier), PreCompact (back up the transcript before context compaction, distinguishing `auto` vs. `manual` triggers), SessionStart (inject context like git status/TODOs at session start or resume), Stop (inspect Claude's completed response and force continuation via `"continue": true` for multi-step workflows), SubagentStop (same as Stop, but for Task-tool subagent completion), UserPromptSubmit (inject dynamic context, e.g., a sprint-priorities file, alongside every submitted prompt).
- **Configuration**: JSON in settings files at three levels — project (`.claude/settings.json`, shareable/committed), user (`~/.claude/settings.json`, all projects), local (`.claude/settings.local.json`, personal/uncommitted) — with project-level taking precedence; enterprise-managed policy settings also available.
- **Matchers** (apply only to PreToolUse, PostToolUse, PermissionRequest): exact string ("Write"), pipe-separated alternatives ("Write|Edit"), wildcard ("*" or empty matches all), and argument-level patterns ("Bash(npm test*)"); case-sensitive; MCP tool patterns use `mcp__servername__.*`.
- **Data flow**: hooks receive JSON via stdin (session_id, transcript_path, cwd, permission_mode, hook_event_name, plus tool_name/tool_input for tool-related hooks); exit code 0 = success (stdout processed as JSON or added to context), exit code 2 = blocking error (stderr shown to Claude as the reason), other codes = non-blocking error shown in verbose mode; structured JSON output can also set decision/reason/continue/updatedInput fields directly.
- **Environment variables**: `CLAUDE_PROJECT_DIR`, `CLAUDE_CODE_REMOTE` (true in web environments), `CLAUDE_ENV_FILE` (for SessionStart hooks to persist variables), plus standard shell env vars. Hooks default to a 60-second timeout (configurable), run in parallel when multiple match an event, and identical commands are deduplicated automatically.
- **Security**: hooks execute arbitrary shell commands at the user's permission level; Claude Code requires direct edits to hook config files to be reviewed in the `/hooks` menu before taking effect, preventing silent malicious hook injection. Recommended practices: validate/sanitize stdin input, quote shell variables, use absolute script paths, avoid processing `.env`/credential files.
- **Debugging**: every hook receives a `transcript_path` to a JSONL session log (`tail -f ... | jq` to watch live); a small bash wrapper script can log tool name, event, and exit code per hook invocation for hook-specific debugging beyond what the transcript shows.
- **Recommended starting point**: a single PostToolUse formatter hook (e.g., auto-running Prettier after writes/edits) — immediate, visible feedback before expanding to more hooks.

## Related

- [[ClaudeCodeHooks]] — the concept this article substantially expands (from 5 to 8 hook types, plus matchers/exit-codes/security/debugging detail)
- [[ClaudeCode]] — the tool hooks extend
