---
title: "CoordinationDebt"
type: concept
tags: [ai, software-engineering, agents, collaboration, technical-debt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Coordination debt is the accumulation of merge conflicts, duplicated work, and context-free code changes that results when multiple AI agents and developers work in parallel without shared alignment. As agents accelerate individual output, coordination debt grows faster than teams can manage with existing tools.

## Key Information
- Articulated by Maggie Appleton of GitHub Next
- A consequence of going fast without good alignment in agentic development
- Manifests as: hairy merge conflicts because agents touch the same files, developers doing duplicated work because they both picked up the same task, giant stacks of PRs to review that nobody has context for
- Agents shipping five features a day instead of half of one dramatically increases coordination surface area
- Existing coordination tools (GitHub, Slack, Jira, Linear) were not designed for the volume and speed of agentic development
- The ACE dashboard addresses coordination debt by summarizing what co-workers have been doing — helping teams keep up with the increased pace
- Multiplayer sessions reduce coordination debt by making work visible to the team as it happens, not just at PR time
- Contrasts with the old development process where the slower pace naturally allowed for coordination through meetings, Slack conversations, and draft PRs

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[MaggieAppleton]] — articulated the concept
- [[TeamAlignment]] — the preventative measure against coordination debt
- [[PullRequestAlignment]] — the overloaded mechanism that coordination debt overwhelms
- [[ImplementationWindowCollapse]] — what accelerates coordination debt
- [[CollaborativeAIEngineering]] — the paradigm for reducing coordination debt
- [[MultiplayerAgentSessions]] — the interface that makes work visible
- [[AgentSocialContext]] — the fabric that surfaces coordination needs
