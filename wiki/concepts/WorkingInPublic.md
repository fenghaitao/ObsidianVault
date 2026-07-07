---
title: "WorkingInPublic"
type: concept
tags: [organizational-pattern, transparency, agent-context, security]
sources: ["raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

Working in public is the practice of defaulting team communication, documentation, and decisions to internally public channels within clearly defined security boundaries, so that AI agents — which build their understanding entirely from searchable text — have broad context to work effectively.

## Key Information

### Why It Matters for Human-Agent Teams

Agents build their understanding entirely from the text a team makes searchable: Slack, code, docs, and meeting notes. Private messages, hallway conversations, and restricted documents cannot provide agents with context. For an agent, if it is not written down and accessible, it does not exist.

### Security Boundaries Over Per-Item Sharing

Instead of deciding what information should be available to agents one doc or Slack channel at a time, Anthropic uses clearly defined security boundaries that apply to entire Slack workspaces, meeting transcripts, and doc libraries. Within the security boundary, context flows to every teammate — whether human or AI. This approach:

- Increases what agents and humans get access to
- Reduces confusion about what can be shared and with whom
- Removes decision fatigue from day-to-day work (public vs. private channel, sharing per doc, per thread)

### Benefits of High Transparency

- Agents that can read decisions from team meetings will not suggest tasks that were deprioritized
- Agents with access to product specs beyond their own team can recommend patterns that have succeeded for others
- Agents can read enormous volumes of text far faster than humans, routinely surfacing relevant work humans would have missed
- Teams lean on agents heavily to stay informed and coordinated

### Practical Implementation at Anthropic

- Choosing a handful of security boundaries at the company and creating workspaces and document sharing settings that match each boundary
- Defaulting new communication channels to public within the organization, ensuring decisions land in channels, docs, and meeting notes
- Writing artifacts and meeting notes so that agents can find them, since agents are a primary consumer of team documentation
- Making sure AI has access to the right tools and information needed to get the job done

### Private Interactions

Some interactions are sensitive and need to remain private between a single human and AI. For those, [[ClaudeTag]] supports direct messages to @Claude, and the existing [[Claude.ai]] and [[ClaudeCowork]] applications provide private conversation channels using personal MCP connectors. These tools give Claude access to private information with the knowledge that the conversation and shared content remain private.

### Cultural Shifts Required

Defaulting information to be internally public can require cultural shifts. However, the difference between human-agent teams with context and those without is described as too stark to ignore.

## Related

- [[summary-2026-06-24 - Building effective human-agent teams]] — source article
- [[HumanAgentTeams]] — the broader collaboration model this practice enables
- [[MultiplayerAI]] — the paradigm of AI in shared, team-wide channels
- [[ClaudeTag]] — the product where working in public is implemented
- [[AgentIdentity]] — the access model that supports security boundaries
- [[NorthStar]] — the complementary practice of giving agents direction
- [[Anthropic]] — the company whose internal practices are described
