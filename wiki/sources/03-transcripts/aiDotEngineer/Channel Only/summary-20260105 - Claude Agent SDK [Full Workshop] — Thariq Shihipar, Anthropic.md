---
title: "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"
author: "aiDotEngineer"
speaker: "Thariq Shihipar"
organization: "Anthropic"
date: 2026-01-05
tags: [agent-sdk, claude-code, bash-tool, agent-design, anthropic]
last_updated: 2026-06-25
---

## Core Thesis
The Claude Agent SDK, built on top of Claude Code, packages battle-tested agent infrastructure (tools, bash, file system, skills, sub-agents, hooks, compacting) so developers can focus on domain-specific agent design problems rather than rebuilding harness components. The bash tool is the most powerful agent tool because it enables composability, code generation, and flexible action-taking that structured tools alone cannot match.

## Key Points
- Claude Agent SDK is built on Claude Code because users organically started using Claude Code for non-coding tasks, revealing that the bash tool and file system are universal agent primitives.
- The "Anthropic way" to build agents: Unix primitives (bash + file system), agents that build their own context, code generation for non-coding tasks, and every agent running in a container with its own file system.
- Three-part agent loop: gather context → take action → verify work. Verification should happen everywhere, not just at the end.
- Three action modalities: tools (structured, reliable, high context), bash (composable, low context, discoverable), code generation (highly dynamic, composable, longest execution).
- The bash tool was the first "code mode" — it lets agents compose functionality via grep, tail, awk, use existing software (FFmpeg, LibreOffice), and dynamically generate scripts.
- Sub-agents preserve main agent context by isolating intensive work; the Agent SDK has best-in-class sub-agent support with bash.
- Skills are a form of progressive context disclosure — folders of files the agent can CD into and read, providing repeatable expert instructions.
- Swiss cheese defense model: model alignment → harness permissions (AST parsing of bash) → sandboxing (network, file system).
- Hooks enable deterministic verification and context insertion at event boundaries in the agent loop.
- Simple is not easy: the final agent code should be small (~50 lines), but the design thinking around search interfaces, verification, and context engineering is deep.
- For spreadsheet/search agents: translate data into interfaces the model already knows well (SQL, XML, range strings) to make problems as in-distribution as possible.
- Agents are "grown, not designed" — reading transcripts and iterating on what the model actually does is the core meta-skill.

## Entities Referenced
- [[ThariqShihipar]] — Anthropic engineer, presenter
- [[ClaudeAgentSDK]] — Anthropic's agent framework built on Claude Code
- [[Anthropic]] — AI research company behind Claude
- [[ClaudeCode]] — Anthropic's coding agent, foundation of the Agent SDK
- [[AdamWolfe]] — Anthropic engineer who built the bash tool
- [[PokéAPI]] — RESTful Pokémon API used in the prototyping demo
- [[Smogon]] — Competitive Pokémon data source
- [[Bun]] — JavaScript runtime used for prototyping
- [[Modal]] — Sandbox provider mentioned for hosting
- [[Cloudflare]] — Sandbox provider with Agent SDK integration example
- [[DigitalOcean]] — Sandbox provider mentioned
- [[AWS]] — Sandbox provider mentioned
- [[FFmpeg]] — Multimedia framework usable via bash tool
- [[JQ]] — JSON processor usable via bash tool
- [[SQLite]] — Database engine usable for querying CSVs
- [[ESLint]] — Linting tool installable and runnable via bash
- [[LibreOffice]] — Office suite usable via bash tool

## Concepts Referenced
- [[BashTool]] — The most powerful agent tool; enables composability and code generation
- [[CodeGenerationForNonCoding]] — Using code generation for docs, data analysis, web queries, unstructured actions
- [[AgentLoop]] — Three-part structure: gather context, take action, verify work
- [[SwissCheeseDefense]] — Layered security model: model alignment, harness permissions, sandboxing
- [[LethalTrifecta]] — The three dangerous capabilities: execute code, change file system, exfiltrate data
- [[ProgressiveContextDisclosure]] — Pattern where agents discover capabilities incrementally (skills, --help flags)
- [[ToolsVsBashVsCodeGen]] — Three action modalities with different trade-offs in structure, composability, and latency
- [[AgenticSearchInterface]] — Designing search interfaces (SQL, XML, range strings) that make problems in-distribution for the model
- [[FileSystemAsContextEngineering]] — Using the file system to store memory, tool results, and agent state
- [[Hooks]] — Event-driven deterministic verification and context insertion points
- [[Sandboxing]] — Container-based isolation for agent execution
- [[YOLOMode]] — Claude Code mode that skips permission confirmations
- [[SubAgents]] — Isolated agents that preserve main context by handling intensive subtasks
- [[Verification in Agentic Loops]] — Testing correctness at every step; should happen everywhere, not just at the end

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — also covers agent loops and verification
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — sub-agents and context management
- [[summary-20251222 - No More Slop – swyx]] — Anthropic and Claude models
