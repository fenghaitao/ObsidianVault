---
title: "ClaudeTag"
type: entity
tags: [product, claude, multiplayer-ai, team-collaboration, agent-identity]
sources: ["raw/01-articles/claude/2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI.md", "raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

Claude Tag is Anthropic's "multiplayer" AI product where Claude sits in shared Slack channels alongside many people, drawing on tools and context that belong to the workspace rather than any individual user. It enables long-running, team-based AI work through an [[AgentIdentity|agent identity]] access model.

## Key Information

- Announced as a "multiplayer AI" experience, contrasting with the "single player" model where one person chats with one assistant.
- Uses [[AgentIdentity]]: Claude has its own accounts for each connected system (e.g., Slack app, GitHub App, warehouse service account), set up by an admin and tied to the workspace.
- Each private channel gets a distinct Claude identity; public channels share a workspace-level identity.
- Admins define a baseline identity at the workspace level; channels inherit it by default, with channel-level overrides for scoped access.
- Role-Based Access Control (RBAC) on Enterprise plans lets admins decide which members can invoke Claude in a given channel.
- Direct messages work differently: they run on users' individual claude.ai accounts with their own connectors and credentials.
- Every routine, memory write, and network call made with agent credentials is recorded; actions also land in each connected system's own logs.
- Future roadmap includes just-in-time credential grants and an identity-aware overlay for organizations with complex clearance structures.
- Anthropic's internal experience found that Claude Tag's value compounds with tool and context access -- each connected system makes every other one more useful through cross-system context combination.

### Human-Agent Teams

Claude Tag enables [[HumanAgentTeams|human-agent teams]] where humans and agents collaborate in shared Slack channels as a single roster with shared artifacts and workspace. Teams use Claude Tag to assign specific roles to agents (data analysis, design standards, research synthesis) while humans hold strategy and judgment roles. Direct messages to @Claude provide a private channel for sensitive one-on-one interactions, while the existing [[Claude.ai]] and [[ClaudeCowork]] applications offer additional private conversation channels using personal MCP connectors.

## Related

- [[summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI]] — source article
- [[summary-2026-06-24 - Building effective human-agent teams]] — source article on human-agent teams
- [[AgentIdentity]] — the access model Claude Tag is built on
- [[MultiplayerAI]] — the paradigm of AI in shared, team-wide channels
- [[HumanAgentTeams]] — the collaboration model Claude Tag enables
- [[WorkingInPublic]] — the practice Claude Tag supports through shared channels
- [[Anthropic]] — the company behind Claude Tag
- [[ClaudeCode]] — Anthropic's developer agent (Noah Zweben, the article's author, is on the Claude Code team)
- [[summary-28 - Tag @Claude in]] — source summary
