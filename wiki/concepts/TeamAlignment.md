---
title: "TeamAlignment"
type: concept
tags: [ai, software-engineering, collaboration, bottleneck, agentic-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Team alignment is the process of ensuring everyone on a software team agrees on what to build and why before implementation begins. In the agentic development era, alignment has become the critical bottleneck — agents have made the cost of not being aligned much higher, as code can be generated in minutes without proper planning or shared understanding.

## Key Information
- Articulated by Maggie Appleton as the central bottleneck in agentic development
- Alignment has always been a bottleneck, but agents have dramatically increased the cost of misalignment
- The old development process had many alignment touchpoints: planning meetings, Slack conversations, issue comments, draft PR discussions
- As the implementation window collapsed, most early alignment touchpoints disappeared
- All alignment weight now sits on the pull request — at the end of the process when it's too late
- PRs were never designed to carry this alignment burden and perform poorly at it
- Going fast without alignment leads to: features no one asked for, critical feedback after completion requiring total rework, coordination debt
- Most context needed for alignment is not in the codebase — it's in people's heads (business context, financial resources, political dynamics, product vision, user research, organizational history)
- Agents can never discover this human context on their own
- The solution: tools that help teams align before agents start working, not after
- Alignment must happen constantly alongside implementation — planning and building are now a continuous cycle
- ACE's approach: embed coding agents in multiplayer sessions where teams can discuss plans and share context naturally

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[MaggieAppleton]] — articulated the bottleneck
- [[CollaborativeAIEngineering]] — the paradigm addressing this bottleneck
- [[ImplementationWindowCollapse]] — what eliminated early alignment touchpoints
- [[PlanningBuildingCycle]] — the continuous cycle replacing phased development
- [[PullRequestAlignment]] — the overloaded alignment mechanism
- [[CoordinationDebt]] — the consequence of poor alignment
- [[AgentSocialContext]] — how agents can help with alignment
- [[OpportunityCostAsRealCost]] — why alignment matters economically
