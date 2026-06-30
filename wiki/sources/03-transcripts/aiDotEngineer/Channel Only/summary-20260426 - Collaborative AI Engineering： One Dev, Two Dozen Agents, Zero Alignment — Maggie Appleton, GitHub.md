---
title: "summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub"
type: source
tags: [source, transcript, ai, collaborative-ai-engineering, team-alignment, agent-collaboration, multiplayer-agents, ace, github-next]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"]
last_updated: 2026-06-29
---

## Core Summary
Maggie Appleton, a staff research engineer on GitHub Next's Labs team, argues that current coding agent tools are fundamentally single-player — they scale individual productivity but ignore that software is a team sport. The real bottleneck is no longer implementation but alignment: agreeing on what to build and why. She presents ACE (Agent Collaboration Environment), a research prototype that embeds coding agents into multiplayer sessions backed by cloud micro-VMs, enabling teams to plan, discuss, and build together with agents as collaborative participants rather than solo tools.

## Key Points
- Current agent tools are "single-player interfaces" — the "one man, two dozen Clods" theory assumes software is made by one person, but software is a team sport
- "Nine women make a baby in one month" logic: more individual output doesn't solve problems requiring communication and coordination — it makes them worse
- Implementation is rapidly becoming a solved problem — writing code is fast, cheap, and improving in quality. The hard question is no longer "how to build it" but "should we build it?"
- When production is cheap, opportunity cost becomes the real cost — you can't build everything, and whatever you pick comes at the cost of everything else
- Alignment has always been a bottleneck, but agents have made the cost of not being aligned much, much higher
- Current coordination tools (GitHub, Slack, Jira, Linear) are not designed for the agentic development world — they were built for an outdated way of building software
- The old development process had planning, building, and review phases with many alignment touchpoints along the way — the implementation window has now collapsed
- Because implementation is cheap, teams skip planning — most early alignment touchpoints disappear, and review time for generated code actually increases
- The time between logging an issue and an agent opening a PR is now minutes — code is so cheap that teams don't stop to think before prompting
- Most coding agents have a local plan mode that is completely unshared — teams lose even more alignment points
- All alignment weight now sits on the pull request, at the end of the process when it's too late — PRs were never designed for this
- Going fast without alignment leads to wasted work: features no one asked for, critical feedback after completion requiring total rework, coordination debt (merge conflicts, duplicated work, giant PR review stacks with no context)
- The solution: tools that help teams align before agents start working, not after — alignment must happen constantly alongside implementation
- Planning and building are no longer separate phases — they are now a cycle
- Most context needed for alignment is not in the codebase but in people's heads: business context, financial resources, political dynamics, product vision, user research, organizational history
- Agents can never discover this human context on their own — teams need ways to share it early and naturally without adding process overhead
- ACE (Agent Collaboration Environment): GitHub Next's research prototype for collaborative AI engineering
- ACE features: multiplayer chat sessions backed by micro-VMs (sandboxed cloud computers on their own Git branches), shared prompting history, live previews, automatic commits, session summaries, VS Code integration with real-time multiplayer editing
- Sessions are isolated — parallel tasks can run without stashing or branch switching
- Agents can read the whole team conversation as input — teammates discuss, then say "@Ace, do it"
- Slack-like interface makes coding agents accessible to designers, PMs, and customer support — not just developers
- ACE includes collaborative plan editing with shared cursors — teams can discuss and refine agent-generated plans before execution
- ACE dashboard provides team-wide summaries of what co-workers have been doing, helping with the speed/volume challenge of agentic development
- Agents with access to team conversations create a "social information fabric" — they can notify about decisions, pull people into relevant conversations, and help teams stay oriented
- The micro-VM architecture means sessions don't die when laptops close — agents keep working in the cloud, and mobile access will work seamlessly
- ACE is going into technical preview with a few thousand people to learn how people collaborate in it
- The ultimate goal: tools that create environments where teams can think rigorously together about hard problems, do higher quality work, and build a few exceptional things rather than a thousand crappy ones
- In a world of fast, cheap software, quality becomes the new differentiator — craftsmanship sets you apart from "vibe-coded slop"
- Craft still costs time and energy — to buy it, you need to do fewer things better, which requires strong alignment
- Agents should help reclaim the time that implementation used to consume, redirecting it toward rigorous critical thinking, better alignment, exploration, research, and deeper problem-solving

## Related
- [[MaggieAppleton]] — speaker, GitHub Next
- [[ACE]] — Agent Collaboration Environment, the research prototype
- [[GitHubNext]] — GitHub's experimental research team
- [[GitHub]] — parent organization
- [[CollaborativeAIEngineering]] — the core paradigm
- [[TeamAlignment]] — the bottleneck in agentic development
- [[ImplementationWindowCollapse]] — how agents have compressed the development timeline
- [[PlanningBuildingCycle]] — planning and building as a continuous cycle
- [[OpportunityCostAsRealCost]] — when production is cheap, opportunity cost dominates
- [[QualityAsDifferentiator]] — craftsmanship vs vibe-coded slop
- [[MultiplayerAgentSessions]] — shared agent coding sessions
- [[MicroVMArchitecture]] — cloud sandbox architecture for isolated sessions
- [[AgentSocialContext]] — agents with access to team social fabric
- [[CoordinationDebt]] — merge conflicts and duplicated work from parallel agents
- [[PullRequestAlignment]] — PRs as the overloaded alignment bottleneck
- [[SinglePlayerAgentInterfaces]] — current tools' fundamental limitation
- [[Slack]] — existing tool not designed for agentic development
- [[Jira]] — existing tool not designed for agentic development
- [[Linear]] — existing tool not designed for agentic development
- [[ClaudeCode]] — referenced as "Claude" in the "one man, two dozen Clods" framing
