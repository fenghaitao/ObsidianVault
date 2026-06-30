---
title: "MultiplayerAgentSessions"
type: concept
tags: [ai, agents, collaboration, interface-design, multiplayer, ace]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Multiplayer agent sessions are shared coding environments where multiple humans and AI agents collaborate in the same workspace. Unlike single-player terminal-based agent interfaces, multiplayer sessions allow teammates to see each other's prompting history, share context, discuss plans, and collectively direct agents — making software development a team activity rather than a solo one.

## Key Information
- Core feature of ACE (Agent Collaboration Environment) by GitHub Next
- Each session is a chat channel with teammates and coding agents, backed by an isolated cloud micro-VM
- Sessions are isolated — parallel tasks can run without stashing or branch switching
- Teammates can jump into each other's sessions with one click — no need to stash changes or pull branches
- Full prompting history with the agent is visible to all session members
- Agents can read the entire team conversation as context for execution
- Workflow: teammates discuss what to build, then say "@Ace, do it" — the agent executes based on the full conversation
- Shared dev server, preview, and terminal — everyone sees the same outputs
- "No one is going to say this doesn't work on my machine"
- Automatic commits with descriptive messages
- Session summaries keep members oriented when switching between parallel sessions
- Designed to be accessible to non-developers (designers, PMs, customer support) — Slack-like interface lowers the barrier
- Contrasts with current tools where coding agents are "single-player interfaces" focused on individual productivity
- Enables the planning-building cycle: teams plan together, refine plans collaboratively, then execute — all in one shared space

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[ACE]] — the prototype implementing this concept
- [[MaggieAppleton]] — creator of ACE
- [[CollaborativeAIEngineering]] — the paradigm enabled by multiplayer sessions
- [[MicroVMArchitecture]] — the infrastructure enabling multiplayer sessions
- [[AgentSocialContext]] — the context fabric created by shared sessions
- [[PlanningBuildingCycle]] — the workflow enabled by multiplayer sessions
- [[SinglePlayerAgentInterfaces]] — the current paradigm being replaced
- [[TeamAlignment]] — the goal multiplayer sessions serve
