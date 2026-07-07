---
title: "ClaudeCodeHooks"
type: concept
tags: [claude-code, hooks, automation, determinism]
sources: [raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md, raw/01-articles/claude/2025-12-11 - Claude Code power user customization How to configure hooks.md, "raw/01-articles/claude/2026-06-03 - Lessons from building Claude Code How we use skills.md", "raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
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

## Hooks as the Right Tool for Deterministic Behavior (June 2026)

- **"Every time X, always do Y"** patterns in CLAUDE.md are an anti-pattern. If the behavior should happen reliably — like running prettier after every edit or posting to Slack on completion — use a hook in `settings.json` instead. The model choosing to run a formatter is different from the formatter running automatically.
- **"Never do this"** instructions in CLAUDE.md are the wrong tool. When something absolutely must not happen, an instruction is insufficient — Claude will follow it most of the time but can fail under pressure, in long sessions, or due to prompt injection. A real guardrail needs to be deterministic: a `PreToolUse` hook can inspect a call and exit code 2 to block it. **Managed settings** go further: they are admin-deployed, cannot be overridden by local config, and are the only way to enforce a deterministic, organization-wide guardrail.
- **Low context cost**: hooks are code that the harness runs rather than instructions loaded into context. The configuration or instruction lives outside the main context window. Most hooks don't save output to the main window unless explicitly configured to return it.

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

## Skill-Scoped Session Hooks (June 2026)

Skills can include hooks that are only activated when the skill is called, and that only last for the duration of the session. This enables opinionated hooks you don't want running all the time but that are extremely useful in specific contexts:

- **`/careful`** — blocks `rm -rf`, `DROP TABLE`, force-push, `kubectl delete` via PreToolUse matcher on Bash. Only wanted when touching production; having it always on would be disruptive.
- **`/freeze`** — prevents any edits, useful when you want Claude to only read and analyze.

Skill-scoped hooks are configured within the skill's own folder structure, using the same hook event types as global hooks. They activate only when the skill is loaded and deactivate when the session ends. See [[ClaudeCodeSkills]] and [[summary-2026-06-03 - Lessons from building Claude Code How we use skills]].

## Related

- [[summary-09 - Hooks in Claude Code]] — source summary
- [[ClaudeCode]] — the tool hooks extend
- [[CLAUDE-md]] — the non-deterministic alternative
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
- [[summary-2025-12-11 - Claude Code power user customization How to configure hooks]] — advanced configuration guide expanding hooks from 5 to 8 event types
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — self-improving hooks (Stop/SessionStart) and maintaining hooks as models evolve
- [[summary-2026-06-03 - Lessons from building Claude Code How we use skills]] — skill-scoped session hooks (/careful, /freeze)
- [[ClaudeCodeSkills]] — skills system that can include scoped hooks
- [[summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more]] — steering framework: hooks for deterministic enforcement, not prompted instructions
- [[ClaudeCodeRules]] — path-scoped rules as the middle ground between CLAUDE.md and hooks
- [[ClaudeCodeOutputStyles]] — system-prompt-level authority for instructions that must carry weight
