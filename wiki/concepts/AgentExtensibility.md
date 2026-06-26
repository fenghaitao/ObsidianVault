---
title: "AgentExtensibility"
type: concept
tags: [agents, architecture, extensibility, plugins, typescript]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Agent extensibility is the ability for a coding agent harness to be extended with custom tools, slash commands, event hooks, session state, compaction strategies, providers, and full tool control. Mario Zechner's Pi implements this through TypeScript modules with hot reloading, distributed via NPM/GitHub rather than a proprietary marketplace.

## Key Information
- Pi extensions are TypeScript modules — in the simplest case, a single TypeScript file on disk
- Extension API lets you hook into everything: tools, slash commands, events, session state, compaction, providers, full tool control
- Hot reloading: changes take effect immediately during the session without restarting
- Users build extensions by telling Pi what they want and iterating with hot reload
- Extensions distributed via NPM/GitHub — "we don't need to reinvent another bunch of silos called marketplaces. We already have package managers."
- Contrasts with Claude Code's hooks: "every time a hook triggers, what actually happens is a new process gets spawned... I don't find that specifically efficient"
- Community extensions include: slash commands, agent chat rooms, NES games, Doom, sub-agents, plan mode, MCP support
- Pi ships its own documentation and code examples so the agent can write extensions for itself

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[Pi (coding agent)]] — implements this
- [[SelfModifyingAgents]] — the broader thesis enabled by extensibility
- [[MarioZechner]] — creator
- [[Hooks]] — Claude Code's more limited approach
- [[Skills]] — markdown-based extension mechanism Pi also supports
- [[MCP]] — can be added via extensions
