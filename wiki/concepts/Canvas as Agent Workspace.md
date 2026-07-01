---
title: "Canvas as Agent Workspace"
type: concept
tags: [agents, canvas, workspace, shared-state, spatial, collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
Canvas as Agent Workspace is the concept of using a spatial canvas as the shared state and working environment for multiple AI agents, where the canvas itself serves as the medium for coordination, output, and mutual awareness rather than relying on explicit message passing.

## Key Information
- **Canvas as shared state**: The canvas is the single source of truth that all agents read from and write to, eliminating the need for separate state synchronization
- **Spatial partitioning**: Different agents can work on different spatial regions of the canvas simultaneously without conflict
- **Implicit coordination**: Agents can see what others are doing by observing the canvas state, enabling coordination without explicit communication
- **Persistence**: The canvas preserves all agent outputs, creating a persistent, visible history of collaboration
- **Human-readable**: Unlike code-based agent outputs, canvas outputs are visual and immediately understandable by humans
- **Bidirectional**: Humans can draw on the canvas alongside agents, creating a truly collaborative workspace
- The canvas serves as both the input mechanism (humans draw what they want) and the output medium (agents produce visual results)
- Contrasts with chat-based interfaces where agent state and output are ephemeral and linear
- Enables the "agent as collaborator" paradigm rather than "agent as tool"
- Key challenge: agents are "essentially blind while they're working" — they need to periodically re-read the canvas to stay aware of changes

## Related
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[Agents on Canvas]] — the paradigm this enables
- [[TLDraw]] — platform implementing this concept
- [[Fairies]] — concrete multi-agent implementation
- [[Agent Workspaces]] — related concept from AgentCraft
- [[AgentHuman Collaboration]] — the collaboration model
- [[HighBandwidth Artifacts]] — the interface paradigm
