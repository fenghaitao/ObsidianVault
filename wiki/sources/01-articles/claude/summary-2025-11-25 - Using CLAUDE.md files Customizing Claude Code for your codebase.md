---
title: "summary-2025-11-25 - Using CLAUDE.md files Customizing Claude Code for your codebase"
type: source
tags: [source, claude-md, claude-code, context-management]
sources: ["raw/01-articles/claude/2025-11-25 - Using CLAUDE.md files Customizing Claude Code for your codebase.md"]
last_updated: 2026-07-04
---

## Core Summary

A practical guide to structuring `CLAUDE.md` files: what to include (project summary, directory map, custom tools/MCP servers, standard workflows), how to bootstrap one via `/init`, and three complementary context-management techniques — `/clear` between tasks, subagents for isolated-perspective phases, and custom slash commands for repeated prompts.

## Key Points

- **`/init`** analyzes the codebase (package files, docs, config, code structure) and generates a starter CLAUDE.md with build/test commands, key directories, and detected conventions — a starting point to refine, not a finished product; can also be re-run on an existing CLAUDE.md to suggest improvements.
- **What to include**: project summary and directory tree for orientation; custom tools/scripts with usage examples; MCP server usage notes (e.g., a Slack MCP server scoped to "post to #dev-notifications only, rate limited to 10 messages/hour"); standard workflows (e.g., explore-plan-code-commit for features, TDD for algorithmic work) so Claude thinks before acting instead of jumping straight to changes.
- **Iterative growth**: use the `#` key during a session to add instructions you find yourself repeating, accumulating a CLAUDE.md that reflects actual team practice rather than a one-time, speculative setup.
- **`/clear`**: resets the context window between distinct tasks (e.g., after finishing an auth-debugging session, before starting a new API endpoint) while preserving CLAUDE.md — prevents accumulated irrelevant history from degrading focus.
- **Subagents for phase isolation**: e.g., "use a sub-agent to perform a security review of that code" after implementing a payment processor, so debugging context doesn't color the security analysis with already-resolved concerns.
- **Custom slash commands**: markdown files in `.claude/commands/` (e.g., `performance-optimization.md`) become reusable `/performance-optimization` commands supporting `$ARGUMENTS`/`$1`/`$2` placeholders; Claude can write these command files for you on request.
- **Security note**: never put secrets, API keys, or vulnerability details in CLAUDE.md — it becomes part of the system prompt and should be treated as shareable documentation.

## Related

- [[CLAUDE-md]] — the concept this article substantially expands (workflows, `/clear`, subagents, custom commands)
- [[ClaudeCodeSubagents]] — used here for isolated-perspective phase separation
- [[ModelContextProtocol]] — MCP server documentation pattern within CLAUDE.md
