---
title: "How Emergent Is Making App Building More Accessible with Claude"
type: source
tags: [emergent, app-building, no-code, multi-agent, startups, democratization]
sources: [raw/03-transcripts/Claude/How teams use Claude/02 - How Emergent is making app building more accessible with Claude.md]
last_updated: 2026-06-23
---

## Core Summary

Makinde, CEO of Emergent, discusses building a text-to-app platform that democratizes software engineering for small businesses and domain experts. Starting from automated software testing at YC, the team discovered that solving the verification loop enables long-running agents. Emergent uses multi-agent systems with refactoring agents, pre/post-deployment security agents, and long-term memory that learns across all apps being built. Deployment rates improved from 84% to 98%. Key insight: code generation is only 20% of the problem; deployment, maintenance, security, and feedback loops are the other 80%. Emergent indexes on quality over speed, comparing themselves to dev shops ($250K, 3-month projects) rather than IDEs.

## Key Points

- **Origin:** Started with automated software testing at YC; discovered that solving verification enables long-running agents.
- **Multi-agent system:** Refactoring agent, pre-deployment security agent, post-deployment agent. One of the first teams to productionize multi-agent systems.
- **Long-term memory:** Agents learn across all apps being built, not just within a single user session. First-time errors and library upgrades are learned once and applied everywhere.
- **Full-stack ownership:** Own container technology (disk/memory snapshotting on Kubernetes), deployment, hosting, and feedback loops. The last mile is where most solutions trip.
- **User base:** 7 million users across 190 countries. Primarily business operators and domain experts, not semi-technical users as initially expected.
- **Deployment rates:** Improved from 84% to 98% through tightening feedback loops and self-learning agents.
- **Model philosophy:** Index on highest quality output, not speed or cost. Users compare to $250K dev shops, not IDEs. Opus is the workhorse.
- **Rewrite philosophy:** Delete everything and reimagine with each new model class. Systems rewritten 4 times in 9 months.
- **Next product:** Wingman — agents for automating entire business operations (finances, operations, sales, marketing).
- **Market thesis:** Small businesses are 70% of global employment, 50% of GDP. AI can serve million niches at zero marginal cost for the first time.

## Related

- [[ClaudeFable5]] — Opus as the workhorse model
- [[ClaudeCode]] — the coding agent foundation
- [[Emergent]] — the company entity
- [[AgenticMemory]] — long-term memory across apps
- [[ClaudeCodeSubagents]] — multi-agent system patterns
