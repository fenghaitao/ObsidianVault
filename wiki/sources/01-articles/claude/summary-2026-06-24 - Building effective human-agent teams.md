---
title: "summary-2026-06-24 - Building effective human-agent teams"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Core Summary

The way we work with AI is evolving from a single-player (one human, one chat window) to a multiplayer experience where humans and agents collaborate as a team in shared workspaces like Slack. Anthropic shares four practical lessons from months of internal testing: work in public with broad context so agents can learn from accessible information; define clear roles for every human and agent with the right tools; set a north star goal to guide agent proactivity; and build trust over time by granting autonomy proportional to demonstrated reliability.

## Key Points

- Multiplayer agents have their own credentials, persistent memory, and broad information access, living in team collaboration tools like Slack rather than individual chat windows.
- Working in public means defaulting to internally public channels and docs within clearly defined security boundaries, so agents can build understanding from searchable text — private messages and restricted documents are invisible to agents.
- Defined roles with specific tool access prevent duplication of work: humans hold roles only humans can hold (strategy, judgment), while agents own specific tasks like data analysis, design standards, or research synthesis.
- A north star is an ambitious, wide-reaching goal set by humans that gives agents consistent direction; explicitly naming which agents can proactively suggest new workstreams leads to measurable improvements.
- Trust is built incrementally: start with manual review, design verification checklists, use a "verifier" agent to check work, build reflection cycles, and expand autonomy by task type after repeated successes.
- Agents should treat human attention as a scarce resource — batching questions, repeating key context, and limiting how many items each human sees at once.
- The patterns (north star, clear roles, strong documentation, shared quality bar, room to learn from mistakes) are healthy team habits known for decades; agents make it even more important not to skip them.

## Related

- [[HumanAgentTeams]] — the core concept of humans and agents working as a team
- [[MultiplayerAI]] — the paradigm this article builds upon
- [[ClaudeTag]] — the product enabling human-agent teams in Slack
- [[WorkingInPublic]] — Lesson 1: making information broadly accessible
- [[NorthStar]] — Lesson 3: ambitious goals that guide agent proactivity
- [[DoerVerifier]] — Lesson 4: the verification pattern for building trust
- [[AgentIdentity]] — the access model underlying multiplayer agents
- [[Anthropic]] — the company whose internal practices are described
