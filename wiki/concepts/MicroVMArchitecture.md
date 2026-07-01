---
title: "MicroVMArchitecture"
type: concept
tags: [ai, infrastructure, cloud, sandbox, agents, ace]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Micro-VM architecture is the infrastructure pattern of backing each collaborative agent session with an isolated, sandboxed cloud computer (micro-VM) on its own Git branch. This enables persistent, always-on workspaces that multiple people can access simultaneously without local machine dependencies.

## Key Information
- Core architectural pattern of ACE (Agent Collaboration Environment) by GitHub Next
- Each session is backed by a micro-VM — a sandboxed computer in the cloud on its own Git branch
- Changes in each session are isolated, enabling parallel work on different tasks
- Instant switching between sessions without stashing or branch management
- Sessions persist when laptops close — agents keep working in the cloud
- Teammates can continue prompting agents and making progress even when the session creator is offline
- Enables mobile access without SSH — no need for a Mac Mini to keep things available
- Shared dev server, terminal, and preview — everyone sees the same environment
- Real-time multiplayer editing in VS Code because everyone is on the same cloud computer
- Automatic commits with descriptive messages
- PR creation directly from the session with backlinks
- "No one is going to say this doesn't work on my machine" — eliminates environment inconsistencies
- Contrasts with local terminal-based agents that die when the laptop closes

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[ACE]] — the prototype using this architecture
- [[MaggieAppleton]] — creator of ACE
- [[MultiplayerAgentSessions]] — the user-facing feature enabled by micro-VMs
- [[Agent Sandbox]] — related sandboxing concept
- [[CloudBased Agent Sandboxes]] — related infrastructure pattern
- [[CollaborativeAIEngineering]] — the paradigm enabled by this architecture
