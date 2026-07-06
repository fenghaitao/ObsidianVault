---
title: "HumanLayer"
type: entity
tags: [company, y-combinator, ai-agents, claude-code, human-in-the-loop]
sources: ["raw/01-articles/claude/2025-11-17 - How three YC startups built their companies with Claude Code.md"]
last_updated: 2026-07-04
---

## Definition

HumanLayer (YC F24) is a startup, founded by Dexter Horthy, providing an API/SDK that lets AI agents contact humans for feedback, input, and approvals across Slack, email, SMS, and other channels — built on the insight that an agent's most useful functions are often also its riskiest.

## Key Information

- **Origin**: Horthy was building autonomous AI agents to manage SQL warehouses and found companies uncomfortable giving agents unsupervised access to risky operations (e.g., dropping database tables); the MVP wired in human-approval steps via Slack.
- Published **"12-Factor Agents: Patterns of reliable LLM applications"** (April 2025) after extensive customer discovery revealed every team was rolling its own agent architecture; the guide went viral and helped establish shared patterns for the emergent discipline of context engineering.
- Pivoted around [[ClaudeCode]] and the [[ClaudeAgentSDK|Claude Agent SDK]]'s headless execution (launched with Opus 4 and Sonnet 4) to build **CodeLayer**, which runs multiple Claude Code sessions in parallel using worktrees and remote cloud workers.
- Key insight: once an engineer masters Claude Code, individual productivity gains are large enough that the real bottleneck becomes organizational — communication, collaboration, and tooling problems for teams shipping AI-written code at scale.
- Closed several large pilots with engineering teams of all sizes starting Q4 2025.

## Related

- [[ClaudeCode]] — the tool HumanLayer's workflows and CodeLayer are built on
- [[ClaudeAgentSDK]] — headless execution underlying CodeLayer
- [[YCombinator]] — HumanLayer's accelerator batch (F24)
- [[ContextEngineering]] — discipline HumanLayer's 12-Factor Agents guide helped codify
- [[summary-2025-11-17 - How three YC startups built their companies with Claude Code]] — source article
