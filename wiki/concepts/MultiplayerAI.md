---
title: "MultiplayerAI"
type: concept
tags: [ai-paradigm, team-collaboration, agent, channel]
sources: ["raw/01-articles/claude/2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI.md", "raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

Multiplayer AI is a paradigm where an AI agent sits in a shared channel alongside many people simultaneously, drawing on tools and context that belong to the workspace rather than any one individual. It contrasts with the "single player" model of one person chatting with one assistant.

## Key Information

- In single-player AI, the user connects their own accounts (Google Drive, GitHub, calendar) and the agent acts on that user's behalf.
- In multiplayer AI, the agent needs its own accounts for tools, set up by an admin and tied to the workspace. This is the [[AgentIdentity|agent identity]] access model.
- The paradigm enables long-running, team-based AI work where the agent can combine context across connected systems (Slack threads, Drive documents, tracker tickets, warehouse queries) into answers no single tool could provide.
- [[ClaudeTag]] is Anthropic's multiplayer AI product, operating in shared Slack channels.
- Direct messages in multiplayer AI products typically run on individual user accounts (not the agent identity), making DMs the right place for personal tasks.
- The value of multiplayer AI compounds with tool and context access: each connected system makes every other one more useful through cross-system context combination.

### Making Multiplayer AI Work: Four Practices

Anthropic distilled four practices from months of internal testing with [[HumanAgentTeams|human-agent teams]]:

1. **[[WorkingInPublic|Work in public]]** — Default to internally public channels and docs within clearly defined security boundaries. Agents build understanding entirely from searchable text; what is not written down and accessible does not exist for them.
2. **Define clear roles** — Every human and agent gets a defined role with the right tools for the job. Humans hold strategy and judgment; agents own specific execution tasks.
3. **Set a [[NorthStar|north star]]** — An ambitious goal set by humans gives agents consistent direction and enables proactive suggestions.
4. **[[DoerVerifier|Build trust over time]]** — Grant autonomy proportional to demonstrated reliability, using verification agents, reflection cycles, and incremental scope expansion.

## Related

- [[summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI]] — source article
- [[summary-2026-06-24 - Building effective human-agent teams]] — source article on human-agent teams
- [[AgentIdentity]] — the access model that enables multiplayer AI
- [[ClaudeTag]] — Anthropic's multiplayer AI product
- [[HumanAgentTeams]] — the collaboration model multiplayer AI enables
- [[WorkingInPublic]] — the practice of making information broadly accessible to agents
- [[NorthStar]] — setting ambitious goals to guide agent proactivity
- [[DoerVerifier]] — the verification pattern for building trust in agent work
- [[Anthropic]] — the company behind the multiplayer AI paradigm
