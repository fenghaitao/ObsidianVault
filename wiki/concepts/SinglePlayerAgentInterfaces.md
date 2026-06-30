---
title: "SinglePlayerAgentInterfaces"
type: concept
tags: [ai, agents, interface-design, critique, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Single-player agent interfaces are the current generation of coding agent tools that operate as solo terminal-based or chat-based experiences on individual developers' machines. They scale up the work of one individual but ignore that software is made by teams, creating an alignment crisis as multiple developers each use their own agents in isolation.

## Key Information
- Articulated as a critique by Maggie Appleton of GitHub Next
- Described as "a wall of terminal-based coding agents all running in parallel on one person's machine"
- The "one man, two dozen Clods theory of the future" — the promise that one person with a fleet of agents replaces an entire team
- The main problem: it assumes software is made by one person in a vacuum
- These tools focus on scaling up the work of the individual, but there is limited value in scaling up one individual
- "Nine women make a baby in one month" logic — more individual output doesn't solve problems requiring communication and coordination
- Most coding agents have a local plan mode that is completely unshared with other people
- Teams don't align on whether the plan is good before shipping — if they even read it
- The result: all alignment weight shifts to the pull request at the end of the process
- Contrasts with multiplayer agent sessions (ACE) where agents are embedded in team-shared workspaces
- The solution is not to abandon agents but to embed them in collaborative environments where planning, discussion, and building happen together

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[MaggieAppleton]] — articulated the critique
- [[MultiplayerAgentSessions]] — the proposed alternative
- [[CollaborativeAIEngineering]] — the paradigm replacing single-player interfaces
- [[TeamAlignment]] — what single-player interfaces undermine
- [[ImplementationWindowCollapse]] — exacerbated by single-player interfaces
- [[ClaudeCode]] — example of a single-player agent interface
- [[Codex]] — example of a single-player agent interface
- [[Cline]] — example of a single-player agent interface
