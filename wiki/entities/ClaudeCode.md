---
title: "ClaudeCode"
type: entity
tags: [tool, ai-coding-assistant, anthropic, agent-cli, claude]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
last_updated: 2026-06-19
---

## Definition

Claude Code is [[Anthropic]]'s terminal-based AI coding assistant — a CLI tool that runs Claude as an autonomous coding agent in your local development environment. By mid-2025 it overtook generalist IDE-based assistants ([[Cursor]], [[Windsurf]]) as [[ColeMedin]]'s primary driver for serious work, with Cole calling it "the most agentic and widely considered the most powerful AI coding assistant right now." It's the **execution surface** of the [[ContextEngineering]] / [[PRPFramework]] discipline that dominates Cole's content from this point forward.

## Key Information

### What it is

A CLI Cole runs in any terminal. It reads/writes files in the current directory, runs shell commands (lint, tests, build), uses the Claude API as the model backend, and supports extensions Cole heavily relies on:

- **Slash commands** — markdown files in `.claude/commands/` become executable `/<name>` commands. Cole's [[PRPFramework]] uses `/generate-prp`, `/execute-prp`, `/prp-mcp-create`, `/generate-pydantic-ai-prp`, etc.
- **`CLAUDE.md`** — project-root file with global rules and conventions Claude reads on startup. The persistent layer of [[ContextEngineering]].
- **Auto-edit mode** — toggle (Shift+Tab in Cole's demos) that lets the agent apply file changes without per-edit confirmation. Required for long-running PRP execution.
- **MCP support** — Claude Code is a first-class [[ModelContextProtocol]] client. Mount [[Crawl4AIRAG]], [[Supabase]] MCP, Brave MCP, etc.
- **Subagent / agent-team support** — by 2026 Claude Code has built-in subagent functionality (covered in later batches; central to "Claude Code subagent dream team" content).
- **Long-running jobs** — Cole frequently kicks off a `/execute-prp` and walks away for 30+ minutes. The agent runs autonomously, validates, iterates.

### Why Cole prefers it over [[Cursor]] / [[Windsurf]]

- **More agentic by default.** Other IDEs are interactive-first (suggestions, inline edits); Claude Code is loop-first (executes long task lists autonomously).
- **CLAUDE.md + slash commands together.** No other AI IDE has the same first-class support for both persistent-rules + executable-prompts as Markdown files.
- **Strong with [[ContextEngineering]].** As the PRP-friendly surface, Claude Code is where the [[PRPFramework]] feels native.
- **Anthropic max-plan economics.** Cole notes most of his content uses the Claude max plan rather than per-token API billing — meaningful for long PRP runs that would otherwise cost real money.
- **The Claude 4 unlock.** [[Rasmus]] reports the framework moved from "reliable on 100-line PRPs" (Claude 3.7) to "reliable on 1000-line PRPs" (Claude 4). Claude Code rides on whatever the latest Claude is.

### How it integrates with [[PRPFramework]]

The PRP framework was designed around Claude Code's primitives. The full lifecycle:

1. `CLAUDE.md` at project root — global rules.
2. `.claude/commands/<name>.md` — slash commands for `/generate-prp`, `/execute-prp`, `/prp-mcp-create`, etc.
3. User edits `initial.md`, runs `/generate-prp initial.md`.
4. Claude Code researches, writes a PRP file in `PRPs/`.
5. User reads + iterates the PRP.
6. User clears context (`/clear`), runs `/execute-prp PRPs/<feature>.md`.
7. Claude Code implements, runs validation gates ([[ValidationGates]]), iterates, declares done.

### Shipping ergonomics

- **Cross-IDE portability** — slash commands are markdown. If a different IDE doesn't support `/foo`, paste the markdown contents into the prompt and tell the model to "use this as the prompt." Cole demonstrates this with Kiro AI in `summary-context-engineering-blueprint-for-ai-agents`.
- **`copy-template.py`** — Cole's pattern for instantiating a fresh working directory from a use-case template (so you don't pollute the canonical repo).

### What's coming (referenced for later batches)

- **Subagents** — "Claude Code subagent dream team" content (batch B/C of this ingest).
- **Skills** — Anthropic's later layer for packaging reusable agent capabilities (`Claude Skills Aren't Just for Claude` — batch B/C).
- **2000+ hours, harness era** — by 2026 Cole's content treats Claude Code as the default harness for any serious agentic engineering work.

## Related

- [[Anthropic]] — author
- [[ColeMedin]] — primary advocate in this corpus
- [[PRPFramework]] — Cole's primary use of Claude Code
- [[ContextEngineering]] — the discipline Claude Code is the execution surface for
- [[ValidationGates]] — sub-pattern run inside Claude Code
- [[ModelContextProtocol]] — first-class integration
- [[AICodingAssistant]] — Claude Code's category (the agentic-default end of the spectrum)
- [[Cursor]], [[Windsurf]] — interactive-first counterparts
- [[summary-context-engineering-is-new-vibe-coding]], [[summary-context-engineering-101]], [[summary-context-engineering-blueprint-for-ai-agents]] — primary sources
