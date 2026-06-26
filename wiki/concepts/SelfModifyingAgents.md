---
title: "SelfModifyingAgents"
type: concept
tags: [agents, architecture, extensibility, self-modification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Self-modifying agents are coding agents that can modify their own behavior, tools, and capabilities at runtime. Mario Zechner's core thesis is that the current form of coding agents is not their final form, and the path forward is agents that can adapt themselves to the user's workflow rather than forcing the user to adapt to the agent.

## Key Information
- Mario Zechner's second thesis: "We need better ways to around [and find out]. For me, that means self-modifying malleable agents. Things that the agent itself can modify, and I can modify, depending on my workflow."
- Pi implements this by shipping its own documentation and code examples of extensions, then telling the agent: "Here's the documentation. Here's some code that shows you how to modify yourself by writing extensions."
- Extensions are TypeScript modules that hot reload — changes take effect immediately during the session
- Users don't write extensions; they tell Pi to build extensions based on their specifications, then iterate with hot reload
- This creates an agent that "adapts to your workflow instead of the other way around"
- Contrasts with Claude Code's approach where the harness controls the context behind the user's back

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[Pi (coding agent)]] — implements this concept
- [[MarioZechner]] — originator of the thesis
- [[AgentExtensibility]] — the mechanism that enables self-modification
- [[ContextOwnership]] — the problem self-modifying agents solve
- [[MinimalAgentDesign]] — related design philosophy
