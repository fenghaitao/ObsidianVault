---
title: "Coding Agents as Building Blocks"
type: concept
tags: [coding-agents, architecture, product-design, agent-embedding, thesis]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md"]
last_updated: 2026-06-29
---

## Definition
Coding Agents as Building Blocks is the thesis that coding agents (LLM agents with shell/runtime access that can write and execute code) will become fundamental building blocks for software products, not just developer tools. Rather than building standalone coding agents, organizations should embed coding agent capabilities into their products as composable components.

## Key Information
- Articulated by Matthias Luebken at AIE Code Summit: "Coding agents are and will be a core building block for your software systems"
- A coding agent is an agent core (LLM + tools in a loop) plus a runtime and shell — the shell gives agents access to system tools they can discover and compose autonomously
- Cohere's Excel skill is the canonical example: instead of building a complex Excel integration, they wrapped existing CLI tools (Pandas, OpenPyXL, LibreOffice) into a skill that their coding agent can use
- OpenClaw autonomously discovering FFmpeg on the local machine to process voice messages demonstrates the emergent power: the agent didn't have a voice plugin, but it composed available tools through the shell
- The building block pattern: expose functionality as CLIs → agent discovers and composes them → embed the capability into a product skill
- Contrasts with building standalone coding agents for developer use — the vision is embedding agent capabilities into domain-specific products (sales, finance, etc.)
- There are no established patterns yet — "we're in the fuck around and find out phase for coding agents"
- Ken Thompson's Unix philosophy ("Write programs that do one thing and do one thing well") is cited as a guiding principle: build small, focused tools that agents can compose

## Related
- [[summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon]] — source
- [[Pi (coding agent)]] — the agent framework enabling this
- [[OpenClaw]] — multi-channel agent platform using this pattern
- [[Make it Easy for Agents]] — the architectural pattern for implementing this
- [[CLI for Agents]] — the pattern of exposing tools as CLIs
- [[Cohere]] — Excel skill as canonical example
- [[FFmpeg]] — tool autonomously discovered by OpenClaw
- [[Ken Thompson]] — Unix philosophy as guiding principle
- [[Matthias Luebken]] — speaker who articulated the thesis
- [[Seven AI]] — company implementing this pattern
