---
title: "MasterWhileLoop"
type: concept
tags: [agent-architecture, coding-agents, tool-calling, design-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
The master while-loop is the core architectural pattern behind modern coding agents like Claude Code, Codex, and Cursor. It is a simple loop: while there are tool calls to execute, run the tool, give the tool results back to the model, and repeat until no tool calls remain, then ask the user what to do next. Claude Code internally calls this loop "N0."

## Key Information
- Replaces complex DAG-based architectures that dominated agent design for years
- The model itself decides when to keep calling tools and when to stop — no hardcoded branching logic
- Works because modern models are surprisingly good at knowing when to keep calling tools and when to fix their own mistakes
- The first time Jared Zoneraich used tool calls in a while-loop, he was shocked at how well models handle error recovery autonomously
- The more you lean on the model to explore and figure things out, the more robust the system becomes with better models
- Essentially four lines of code: loop, run tool, feed results, check for more tool calls
- All major coding agents (Claude Code, Codex, Cursor, Amp Code) use this pattern
- The simplicity of this architecture was itself revolutionary compared to prior agent designs

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ToolCalling]] — the mechanism that enables the loop
- [[DAGvsLoopArchitecture]] — the trade-off this pattern represents
- [[SimpleDesignPhilosophy]] — the philosophy behind this approach
- [[ClaudeCode]] — primary example
- [[Core Loop as Orchestrator]] — related but distinct pattern for task decomposition
