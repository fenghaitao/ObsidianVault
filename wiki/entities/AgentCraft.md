---
title: "AgentCraft"
type: entity
tags: [tool, agent-orchestration, rts, gaming, multi-agent, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
AgentCraft is an agent orchestrator created by Ido Salomon that applies RTS (real-time strategy) gaming patterns to managing multiple AI coding agents. It provides a visual, map-based interface where the file system is projected as a game-like map, enabling developers to track, coordinate, and collaborate with dozens of agents simultaneously.

## Key Information
- Created by Ido Salomon, also creator of MCI and MC apps
- Core innovation: applies gaming UI/UX patterns (RTS unit management, muscle-memory cycling, heat maps) to agent orchestration
- **File system map**: Directories are buildings, files are rooms — agents are visualized moving through the map as they work
- **Agent lifecycle**: Can detect existing agent sessions on the device (Cursor, Claude Code, Codex, OpenClaw, etc.) or spawn new ones directly
- **Multi-modal input**: Supports voice, text, and image prompts
- **Integrated tooling**: Built-in terminal, git integration, skills/plugins management for end-to-end workflow
- **Side panel**: High-level mission status summaries for each agent
- **Collision detection**: Heat maps showing where multiple agents are touching the same files, with proactive conflict prevention
- **Agent cycling**: RTS-style quick switching between agents that need attention (plan approval, questions)
- **Quests**: Agents can suggest tasks (refactoring, testing) that the human can approve with one click
- **Campaigns**: High-level goals that spin up containers, let agents decompose/plan/execute autonomously with a campaign orchestrator handling coordination
- **Channels**: Cron-based autonomous agent runs (e.g., daily Twitter scan → idea implementation)
- **Review Bundles**: PR review with visual evidence (screenshots, videos) showing what changed and why
- **Workspaces**: Shared collaboration spaces for multiple humans to see each other's agents, hand off work, and collaborate
- **Agent-to-agent soft collaboration**: Agents coordinate implicitly via shared awareness of file changes and a shared chat
- Free and experimental; community-driven development via Discord
- Presented at aiDotEngineer 2026

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[IdoSalomon]] — creator
- [[MCI]] — related project by same creator
- [[MC apps]] — related project by same creator
- [[RTS-Inspired Agent Orchestration]] — the paradigm
- [[Agent Campaigns]] — feature
- [[Agent Collision Detection]] — feature
- [[Agent Review Bundles]] — feature
- [[Agent Workspaces]] — feature
- [[Agent Channels]] — feature
- [[Agent Quests]] — feature
- [[Agent Orchestration]] — broader concept
- [[AgentVisualization]] — related concept
