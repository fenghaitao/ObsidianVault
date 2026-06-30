---
title: "summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon"
type: source
tags: [source, transcript, ai, agent-orchestration, agent-craft, rts, gaming, collaboration, multi-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Core Summary
Ido Salomon, creator of AgentCraft, MCI, and MC apps, presents a gaming-inspired approach to agent orchestration. The core thesis: spinning up dozens of agents is easy, but humans are the bottleneck in orchestrating them. AgentCraft borrows patterns from RTS (real-time strategy) games — visual maps of the file system, muscle-memory agent cycling, heat maps for collision detection — to raise the ceiling of human-agent collaboration. The product progressively removes the human from the loop: from direct prompting, to agent-suggested quests, to autonomous campaigns running in containers, to cron-based channels that scan ideas and implement them, to shared workspaces for multi-human collaboration with agents.

## Key Points
- **The bottleneck is us**: Spinning up agents is trivial; the human is the limiting factor in orchestrating dozens of agents working in parallel.
- **Gaming as inspiration**: Managing dozens of units in RTS games maps directly to managing dozens of coding agents. AgentCraft transfers gaming learnings into productivity.
- **Physical agent visualization**: Agents are visualized as physical entities on a map that is a projection of the actual file system — directories become buildings, files become rooms.
- **File system map**: Each directory is a building, each file is a room. Users can visually track which agent is working on which file, see change lists, and get full lineage of what happened.
- **Collision detection via heat maps**: By knowing what every agent is working on, AgentCraft can visualize collisions and proactively prevent them.
- **Muscle-memory agent cycling**: Borrowed from RTS games — quickly cycle between agents that need attention (plan approval, questions) using familiar interaction patterns.
- **Agent Quests**: Agents can suggest missions/tasks ("find missions for me to do") — refactoring, testing, and other work the human doesn't want to do.
- **Campaigns**: High-level goals that spin up containers, let agents decompose tasks, plan, and present the plan for review. The campaign orchestrator handles babysitting, not the human.
- **Channels**: Cron-based autonomous agent runs — e.g., "go to Twitter every day, scan cool ideas, and implement them." The human only decides what they want.
- **Review Bundles**: PR review bundles with visual evidence (screenshots, videos) so humans can review agent work without investing too much time.
- **Shift from planning to review**: When agents can produce 10 variations, the human picks the best one — less time planning, more time reviewing.
- **Workspaces**: Shared collaboration spaces where multiple humans (e.g., product designer and engineer) can see each other's agents, hand off work, and collaborate with both humans and agents.
- **Agent-to-agent soft collaboration**: Agents know what files each other are changing and can coordinate implicitly through a shared chat between humans and agents.
- **Integrated tooling**: Built-in terminal, git integration, skills/plugins management, voice/text/image input — end-to-end workflow in one tool.
- **Free and experimental**: AgentCraft is free to download and use, with active development driven by community feedback via Discord.

## Related
- [[IdoSalomon]] — speaker, creator of AgentCraft
- [[AgentCraft]] — the orchestrator product
- [[MCI]] — also created by Ido Salomon
- [[MC apps]] — also created/co-maintained by Ido Salomon
- [[RTS-Inspired Agent Orchestration]] — gaming-inspired orchestration paradigm
- [[Agent Campaigns]] — autonomous containerized agent missions
- [[Agent Collision Detection]] — heat map visualization of file conflicts
- [[Agent Review Bundles]] — PR review with visual evidence
- [[Agent Workspaces]] — shared multi-human agent collaboration
- [[Agent Channels]] — cron-based autonomous agent execution
- [[Agent Quests]] — agent-suggested tasks
- [[Agent Orchestration]] — broader orchestration concept
- [[Agent-Human Collaboration]] — collaboration paradigm
- [[AgentVisualization]] — visual representation of agent activity
