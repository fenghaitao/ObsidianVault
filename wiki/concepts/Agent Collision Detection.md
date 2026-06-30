---
title: "Agent Collision Detection"
type: concept
tags: [agents, orchestration, visualization, conflict-prevention, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Definition
Agent Collision Detection is a feature in AgentCraft that uses heat maps to visualize where multiple AI coding agents are working on the same files simultaneously, enabling proactive prevention of merge conflicts and coordination issues before they occur.

## Key Information
- **Heat map visualization**: The file system map shows "hot spots" where multiple agents are touching the same files
- **Proactive prevention**: Rather than detecting conflicts after they happen (merge conflicts), the system warns before agents create conflicting changes
- **Full lineage tracking**: The system knows which agent did what and when for every file change, enabling precise collision analysis
- **Visual change lists**: Users can see the entire change list for any file and which agents contributed
- Built on the file system map metaphor: directories as buildings, files as rooms — collisions are visually obvious
- Addresses a key challenge in parallel agent orchestration: agents working independently can create conflicting changes that are expensive to resolve
- Part of the broader RTS-inspired approach: just as RTS games show unit positions to avoid friendly fire, AgentCraft shows agent positions to avoid code conflicts

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[AgentCraft]] — the orchestrator implementing collision detection
- [[RTS-Inspired Agent Orchestration]] — the broader paradigm
- [[Agent Orchestration]] — broader orchestration concept
- [[AgentVisualization]] — related visualization concept
- [[Parallel Agents]] — the context where collision detection matters most
- [[Context Sharing Between Agents]] — soft coordination mechanism
