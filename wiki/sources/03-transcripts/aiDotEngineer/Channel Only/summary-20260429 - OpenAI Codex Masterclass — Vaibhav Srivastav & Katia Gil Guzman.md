---
title: "OpenAI Codex Masterclass — Vaibhav Srivastav & Katia Gil Guzman"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - OpenAI Codex Masterclass — Vaibhav Srivastav & Katia Gil Guzman.md"
date: 2026-04-29
tags: [openai, codex, masterclass, plugins, automations, sub-agents, code-review]
---

## Core Thesis
OpenAI Codex is a full software engineering agent — not just a coding tool — powered by a rapidly evolving model flywheel (GPT-5.2 through GPT-5.4), a unified agent harness, and accessible through multiple surfaces (app, IDE, CLI, Slack, GitHub). Its latest features — plugins, automations, sub-agents, code review, and experimental capabilities like guardian approvals and hooks — position it as a comprehensive platform for delegating engineering work to AI.

## Key Points
- Codex is built on a foundation of frontier models with a unified agent harness managing tool execution, environment setup, and safety
- The model flywheel: GPT-5.2 → GPT-5.2 Codex → GPT-5.3 Codex → GPT-5.3 Codex Spark (Cerebras) → GPT-5.4 → GPT-5.4 Mini/Nano
- WebSockets provide ~1.75x faster token delivery; Fast Mode adds another 2x
- Codex app supports native worktrees for parallel feature work without context switching, and native Windows sandbox support
- Plugins bundle skills, apps (integrations), and MCP servers into reusable workflows
- Automations are scheduled background tasks (cron-like) that can use plugins and connected apps
- Game Studio plugin bundles Imagen (asset generation) and Playwright Interactive (browser debugging) for game development
- Sub-agents decompose master tasks into parallel, independent tasks; shipped with 3 default personas (general-purpose, worker, explorer)
- Custom sub-agents can define model, reasoning effort, sandbox mode, MCP access, and skills
- Codex code review is used on 100% of pull requests across all OpenAI repos by default
- Guardian Approvals: experimental feature that spins up a sub-agent to verify privileged tool requests, reducing human approval fatigue
- Hooks: experimental feature supporting pre-tool-use, session-start, and session-stop hooks for programmatic behavior
- Codex Security: state-of-the-art model for finding and fixing vulnerabilities commit-by-commit
- Crossed 3 million weekly active users, more than tripled since January 2026
- Cloud Code plugin enables Codex within cloud code sessions for review and rescue

## Entities
- [[Vaibhav Srivastav]] — OpenAI DX team, presenter
- [[Katia Gil Guzman]] — OpenAI DX team, presenter
- [[OpenAI]] — company behind Codex
- [[Codex]] — OpenAI's software engineering agent
- [[Cerebras]] — hardware partner for GPT-5.3 Codex Spark
- [[Imagen]] — image generation tool used for game assets
- [[Playwright]] — browser automation used interactively for debugging

## Concepts
- [[Codex Plugins]] — bundled skills, apps, and MCP servers
- [[Codex Automations]] — scheduled background agent tasks
- [[Guardian Approvals]] — sub-agent-based privileged tool verification
- [[Codex Code Review]] — automated PR review used across OpenAI
- [[WebSocket Streaming]] — faster token delivery mechanism
- [[Plan Mode]] — automatic complex task detection and planning
- [[Best of N]] — cloud parallelization for picking best output

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — comparison context
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — sub-agents and hooks comparison
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — Codex on Temporal
