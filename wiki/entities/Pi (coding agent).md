---
title: "Pi (coding agent)"
type: entity
tags: [tool, coding-agent, open-source, typescript, extensibility, self-modifying]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md"]
last_updated: 2026-06-26
---

## Definition
Pi is a self-modifying, extensible coding agent harness built by Mario Zechner. It features a minimal core (AI abstraction, agent core as while loop + tool calling, bespoke TUI framework), only 4 tools (read, write, edit, bash), a tiny system prompt, and TypeScript-based extensions with hot reloading.

## Key Information
- Created by Mario Zechner as an alternative to Claude Code after frustration with context control, instability, and lack of extensibility
- Design philosophy: minimal core, maximum extensibility — the agent can modify itself
- Four packages: AI package (provider abstraction + context handoff), agent core (while loop + tool calling), bespoke TUI framework (no flicker, from game dev background), and the coding agent itself
- System prompt is minimal (fits on a slide); later added a few lines for skills (markdown files)
- Only 4 tools: read, write, edit, bash — tool definitions are tiny compared to other harnesses
- Thesis: models are RL-trained up to a zoo and already know they're coding agents; you don't need 10,000 tokens to tell them
- "Yellow by default" security: no nag dialogs for bash approval; users build their own security model via extensions
- Extensions are TypeScript modules (single file on disk in simplest case) with hot reloading
- Extension API lets you hook into everything: tools, slash commands, events, session state, compaction, providers, full tool control
- Extensions distributed via NPM/GitHub, not a new marketplace silo
- Ships its own documentation and code examples so the agent can write extensions for itself
- Users build extensions by telling Pi what they want and iterating with hot reload during the session
- Scored 6th on Terminal Bench before compaction was added
- Peter put Pi inside Open Claw as its agent core, making Pi the target of many Open Claw instances
- Community extensions include: slash commands, chat rooms for agents, NES games, Doom, sub-agents, plan mode, MCP support
- **Malte Ubl's perspective**: Cited Pi (made in Austria) as evidence of Europe's leadership in AI engineering innovation

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[MarioZechner]] — creator
- [[ClaudeCode]] — what Pi was built to replace
- [[OpenCode]] — OSS alternative Mario evaluated
- [[TerminalBench]] — benchmark Pi scored 6th on
- [[OpenClaw]] — Peter embedded Pi as its agent core
- [[SelfModifyingAgents]] — core design thesis
- [[MinimalAgentDesign]] — design philosophy
- [[AgentExtensibility]] — key feature
- [[ContextOwnership]] — problem Pi solves
- [[Skills]] — markdown-based instructions Pi adopted
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (cited as European innovation leader)
- [[Model Commoditization]] — context for application-layer innovation
