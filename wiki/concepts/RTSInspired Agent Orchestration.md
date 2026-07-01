---
title: "RTS-Inspired Agent Orchestration"
type: concept
tags: [agents, orchestration, gaming, rts, visualization, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Definition
RTS-Inspired Agent Orchestration is a paradigm for managing multiple AI coding agents by applying interaction patterns and visual metaphors from real-time strategy (RTS) games. It treats the file system as a game map, agents as controllable units, and uses muscle memory, heat maps, and quick-cycling to help humans coordinate dozens of agents without becoming the bottleneck.

## Key Information
- Core insight: managing dozens of agents is analogous to managing dozens of units in an RTS game — the skills already exist, they just haven't been applied to productivity
- **File system as game map**: Directories are buildings, files are rooms — agents move through the map as they work on files, providing spatial awareness
- **Agent visualization**: Each agent is a physical entity on the map, not an abstract process, making their activity immediately understandable
- **Muscle-memory cycling**: Quick-switch between agents that need attention (plan approval, questions) using familiar RTS interaction patterns
- **Heat maps for collision detection**: Visualize where multiple agents are touching the same files, enabling proactive conflict prevention
- **Full lineage tracking**: Know which agent did what and when for every file change
- **Side panel summaries**: High-level mission status for each agent, analogous to unit status panels in RTS games
- The paradigm progressively removes the human from the loop: direct control → quests (agent-suggested tasks) → campaigns (autonomous containerized missions) → channels (cron-based autonomous runs)
- Implemented concretely in AgentCraft by Ido Salomon
- The gaming metaphor addresses the fundamental problem: spinning up agents is easy, but humans cannot effectively orchestrate them without the right interface

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[AgentCraft]] — implementation of this paradigm
- [[IdoSalomon]] — creator of the paradigm and AgentCraft
- [[Agent Orchestration]] — broader orchestration concept
- [[AgentVisualization]] — visual representation of agent activity
- [[Agent Collision Detection]] — heat map feature
- [[Agent Campaigns]] — autonomous mission feature
- [[Agent Quests]] — agent-suggested task feature
- [[Agent Channels]] — cron-based autonomous feature
- [[Agent Workspaces]] — multi-human collaboration feature
