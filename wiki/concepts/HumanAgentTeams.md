---
title: "HumanAgentTeams"
type: concept
tags: [agent, team-collaboration, multiplayer-ai, organizational-pattern]
sources: ["raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

Human-agent teams are a collaboration model where humans and AI agents work together in a shared workspace — one roster, one set of artifacts, one working space — with humans setting strategy and agents executing work. This contrasts with the "single-player" model of one human working with one agent to accomplish individual tasks.

## Key Information

Human-agent teams represent the evolution from individual AI use to a multiplayer experience. At Anthropic, agents live in team collaboration tools like [[Slack]] via [[ClaudeTag]], with their own credentials, persistent memory, and broad information access.

### Technical Foundation

For agents to productively participate in a team, they need:

- **Persistent memory**: so they can remember goals and tune execution towards them
- **Ongoing broad access to information**: so they can learn how the organization works and take action in service of team goals

### Four Lessons for Success

Anthropic distilled four practices from months of internal testing:

1. **Work in public and give agents broad context** — Default to internally public channels and docs within clearly defined security boundaries. Agents build understanding entirely from searchable text; private messages and restricted documents are invisible to them. See [[WorkingInPublic]].

2. **Every human and agent get a defined role with the right tools** — Humans and agents share one roster. Different agents hold different roles (data analysis, design standards, research synthesis). Humans hold the roles only humans can hold: strategy, judgment, and the most important decisions. Without clear roles, people run fleets of personal AIs on the side, duplicating work and fracturing context.

3. **Set a north star to make agents more proactive** — An ambitious, wide-reaching goal set by humans, shared with agents, with explicit designation of which agents can proactively suggest new workstreams. A clear north star gives agents consistent direction. See [[NorthStar]].

4. **Build trust over time** — Grant autonomy proportional to demonstrated reliability, then expand deliberately. Start with manual review, design verification checklists, use verifier agents, build reflection cycles, and expand scope by task type after repeated successes. See [[DoerVerifier]].

### Roster Pattern

Anthropic engineering teams started creating rosters to codify human and agent roles. Key practices:

- Specific roles help humans track where responsibility lies
- Writing skill files to define specific agents' roles makes specialization easy
- Teams add new agents to focus on new areas as projects get more complex (e.g., adding a release manager agent)

### Agent Communication

Once agents are more independent, they should treat human attention as a scarce resource:

- Batch questions to be answered in a single pass
- Repeat key context to get a human up to speed quickly
- Limit how many things each human sees at once
- Some teams have agents whose sole role is deciding how to batch and elevate communication

### Guardrails

Some teams set guardrails around how much work agents should do per day, ensuring humans can meaningfully engage with the work, maintain important skills, and keep the number of review items sustainable.

## Related

- [[summary-2026-06-24 - Building effective human-agent teams]] — source article
- [[MultiplayerAI]] — the paradigm human-agent teams operate within
- [[ClaudeTag]] — the product enabling human-agent teams in Slack
- [[WorkingInPublic]] — Lesson 1: making information broadly accessible
- [[NorthStar]] — Lesson 3: ambitious goals that guide agent proactivity
- [[DoerVerifier]] — Lesson 4: the verification pattern for building trust
- [[AgentIdentity]] — the access model for multiplayer agents
- [[MultiAgentSystem]] — the broader multi-agent architecture patterns
- [[Anthropic]] — the company whose internal practices are described
