---
title: "ACE"
type: entity
tags: [product, ai, collaborative-ai-engineering, agent-collaboration, github-next, research-prototype]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
ACE (Agent Collaboration Environment) is a research prototype built by GitHub Next's Labs team that embeds coding agents into multiplayer sessions backed by cloud micro-VMs. It aims to solve the alignment bottleneck in agentic development by making planning, discussion, and building a shared team activity rather than a solo one.

## Key Information
- Built by GitHub Next Labs team, led by Maggie Appleton
- Not a production product yet — entering technical preview with a few thousand users to learn how people collaborate
- Core concept: multiplayer chat sessions backed by micro-VMs (sandboxed cloud computers on their own Git branches)
- Described as "Slack, GitHub, Copilot, and a bunch of cloud computers had a baby"
- Each session is a chat channel with teammates and coding agents, backed by an isolated cloud computer
- Sessions are isolated — parallel tasks can run without stashing or branch switching
- Shared prompting history visible to all session members
- Live previews, automatic commits, session summaries
- VS Code integration with real-time multiplayer editing
- Agents can read the entire team conversation as context — teammates discuss, then say "@Ace, do it"
- Slack-like interface designed to be accessible to designers, PMs, and customer support — not just developers
- Collaborative plan editing with shared cursors — teams refine agent-generated plans together
- Dashboard with team-wide summaries of co-worker activity to combat the speed/volume challenge
- Micro-VM architecture means sessions persist when laptops close — agents keep working in the cloud
- Mobile interface planned — micro-VM architecture makes this seamless
- PR creation directly from ACE with backlinks to the ACE session
- Backwards compatible — some team members can use ACE while others stay on existing tools
- Designed explicitly for software development, unlike Slack which lacks the right primitives (diffs, terminal commands, etc.)

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[MaggieAppleton]] — creator
- [[GitHubNext]] — team that built it
- [[GitHub]] — parent organization
- [[GitHubCopilot]] — related GitHub AI product
- [[CollaborativeAIEngineering]] — the paradigm ACE embodies
- [[MultiplayerAgentSessions]] — core feature
- [[MicroVMArchitecture]] — architectural foundation
- [[AgentSocialContext]] — enabled by shared session context
- [[PlanningBuildingCycle]] — supported by collaborative plan editing
