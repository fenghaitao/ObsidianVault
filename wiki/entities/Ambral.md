---
title: "Ambral"
type: entity
tags: [company, y-combinator, ai-agents, claude-agent-sdk, account-management]
sources: ["raw/01-articles/claude/2025-11-17 - How three YC startups built their companies with Claude Code.md"]
last_updated: 2026-07-04
---

## Definition

Ambral, founded by Jack Stettner and Sam Brickman, synthesizes customer activity and interaction signals into AI-powered models of every account, aiming to give every B2B customer the experience of a dedicated one-to-one account manager.

## Key Information

- Addresses account managers juggling 50–100 accounts, where customer context scatters across systems, logs, Slack, transcripts, and usage data.
- Pinpoints which accounts need attention and why, autonomously driving or recommending expansions and catching early churn signals.
- As sole engineer/CTO, Stettner built the core research engine on the [[ClaudeAgentSDK|Claude Agent SDK]] with dedicated [[ClaudeCodeSubagents|subagents]] per data type (Slack, meeting transcripts, product usage) — an architecture directly inspired by how well Claude Code subagents performed in his own development workflow.
- Development workflow: Opus 4.1 for research/planning, Sonnet 4.5 for implementing plans from markdown, with discrete sessions per phase (research, planning, implementation) to avoid context contamination.
- Stettner: "Context is critical... if there's any contradictions in your prompt, you're going to receive lower quality output."

## Related

- [[ClaudeAgentSDK]] — powers Ambral's core research engine
- [[ClaudeCodeSubagents]] — per-data-type subagent architecture
- [[YCombinator]] — Ambral's accelerator
- [[summary-2025-11-17 - How three YC startups built their companies with Claude Code]] — source article
