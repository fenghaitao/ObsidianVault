---
title: "Cursor Cloud Agents"
type: entity
tags: [tool, cursor, cloud, agent-infrastructure, vm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md"]
last_updated: 2026-06-26
---

## Definition
Cursor Cloud Agents are isolated VM-based agent execution environments that allow AI coding agents to work autonomously in reproducible, side-effect-free sandboxes, with computer-use capabilities for self-testing.

## Key Information
- Each agent gets its own separate VM with a reproducible environment
- Enables infinite scaling — Cursor runs "multiple thousands" of agents per day
- Agents can start dev servers, run databases, and use internal tooling within the VM
- Includes computer-use tool: agents can control the browser/keyboard to test their own work and return video evidence
- More expensive than shared workspaces but provides clean, side-effect-free branches
- Eric Zakariasson recommends Cloud Agents over git worktrees for parallel agent work
- Internal Cursor dev tool (`cursor dev tool backend start`, `cursor dev tool frontend start`) abstracts away complex service startup
- Supports authentication via stored snapshots
- Estimated cost: ~$1 per turn for a typical task

## Related
- [[Cursor]] — the parent product
- [[Cursor3]] — the agent-first IDE that integrates with Cloud Agents
- [[IsolatedEnvironments]] — the architectural pattern they implement
- [[Computer Use]] — the self-testing capability they provide
- [[EricZakariasson]] — uses Cloud Agents extensively
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — source
