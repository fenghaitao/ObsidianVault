---
title: "AgentFirstObservability"
type: concept
tags: [observability, agents, platform-engineering, monitoring, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Agent-first observability is the practice of exposing logs, metrics, traces, and system health information through programmatic interfaces (APIs, CLIs, MCP servers) so that AI agents can verify the success of their actions without relying on graphical dashboards designed for human consumption.

## Key Information
- Juan Herreros Elorza argues that traditional observability (dashboards, graphical interfaces) is invisible to AI agents — "agents are not going to be looking at those graphical interfaces"
- Agents need programmatic access to close the verification loop: "this is how you know you have succeeded at the task"
- Key requirements for agent-first observability:
  - Logs, metrics, and traces available via API or CLI
  - MCP server wrappers as an alternative interface
  - Clear success/failure signals that agents can parse and act on
- Without programmatic observability, agents cannot verify their own work — they deploy an application but cannot confirm it is running correctly
- Enables the agent to "close the loop": do something → check if it worked → adjust if needed
- Contrast with human observability workflows: humans check dashboards, interpret graphs, notice anomalies visually — none of which an agent can do
- Part of the broader principle that platforms must serve AI agents as a user class with different interface needs than humans

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[AgentReadyPlatform]] — the goal state
- [[APIFirstDesign]] — the enabling approach
- [[PlatformEngineering]] — parent discipline
- [[AgentsAsPlatformUsers]] — the paradigm shift
- [[AgentObservability]] — related concept for agent-specific observability
- [[MCP]] — wrapper pattern for observability APIs
