---
title: "PullRequestAlignment"
type: concept
tags: [ai, software-engineering, code-review, pull-request, alignment, bottleneck]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Definition
Pull request alignment is the phenomenon where the pull request becomes the sole remaining checkpoint for team alignment in agentic development, carrying the full weight of coordination, review, and decision-making that was previously distributed across planning meetings, Slack conversations, issue discussions, and draft PRs. PRs were never designed for this burden and perform poorly at it.

## Key Information
- Articulated by Maggie Appleton of GitHub Next
- In the old development process, alignment touchpoints were distributed across planning, building, and review phases
- As the implementation window collapsed, most early touchpoints disappeared
- The weight of all alignment now sits on the pull request — at the end of the process when it's too late
- PRs were never designed to be the sole alignment mechanism — they perform poorly at this role
- The time between logging an issue and an agent opening a PR is now a couple of minutes
- Review time for generated code has actually increased, creating more alignment points but on the wrong side of implementation
- Receiving critical feedback after something is finished often means tossing the whole thing out
- Many people inside GitHub Next believe the PR and the issue are not the future of software development
- The solution: alignment must happen before and during implementation, not after — through tools like ACE that embed planning and discussion alongside coding

## Related
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source transcript
- [[MaggieAppleton]] — articulated the concept
- [[ImplementationWindowCollapse]] — what eliminated other alignment touchpoints
- [[TeamAlignment]] — what PRs are now forced to carry alone
- [[CoordinationDebt]] — what accumulates when PR alignment fails
- [[CollaborativeAIEngineering]] — the paradigm that moves alignment earlier
- [[PlanningBuildingCycle]] — the replacement for PR-only alignment
- [[MultiplayerAgentSessions]] — the interface that distributes alignment
- [[GitHub]] — the platform where PRs live
