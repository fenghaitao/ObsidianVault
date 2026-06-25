---
title: "CodingAgents"
type: concept
tags: [agents, coding, ai, tools]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Coding agents are AI agents specialized in writing, editing, and managing code. They dominate RL training data because coding sessions produce measurable reward signals (tests pass, code committed). Examples: Claude Code, Codex, GitHub Copilot, Cursor. Armin Ronacher argues they are becoming the substrate for general-purpose agents because code is a universal expression medium.

## Key Information

- Coding sessions are overrepresented in RL training because they produce clear evaluation signals
- What's overrepresented in training: Unix workflows, files/diffs, build tools, incremental edits, REPL patterns
- What's underrepresented: UI clicking, proprietary systems, binary data, video
- Coding agents are absorbing non-coding tasks — people build on top of them rather than building separate agents
- Key tools: Claude Code, Codex, GitHub Copilot, Cursor, Windsurf, Pi, Antigravity

## Related

- [[ArminRonacher]] — analyzed why coding agents work
- [[ClaudeCode]] — Anthropic's coding agent
- [[Codex]] — OpenAI's coding agent
- [[GitHubCopilot]] — Microsoft's coding agent
- [[CodeExecution]] — the paradigm coding agents enable
- [[ReinforcementLearning]] — how they improve
