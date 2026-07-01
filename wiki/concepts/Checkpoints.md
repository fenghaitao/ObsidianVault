---
title: "Checkpoints"
type: concept
tags: [ai, claude-code, version-control, session-management, agent-state]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Checkpoints is a Claude Code 2.0 feature that tracks code state over time during an agent session, enabling the ability to rewind to previous points in the session if the agent takes a wrong turn or produces undesirable changes.

## Key Information
- **Claude Code 2.0 Feature**: Shipped with Claude Code 2.0 alongside the Agent SDK renaming
- **Rewind Capability**: Allows reverting to previous states of the codebase within a session — useful when the agent goes down a wrong path
- **Session-Level Version Control**: Tracks changes at a finer granularity than Git commits, capturing intermediate states during agent work
- **Release Context**: Shipped around the time of Sonnet 4.5 when models became more context-aware and could track their own token consumption
- **Part of Long-Running Agent Infrastructure**: One of the harness primitives that enable agents to run for extended periods — provides safety net for exploration and pivoting
- **Relationship to Agent Behavior**: Checkpoints enable the "throw everything away and restart" behavior that the generator-evaluator pattern exhibits — the agent can be more aggressive in exploration knowing it can rewind

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[ClaudeCode]] — product with this feature
- [[GeneratorEvaluator Pattern]] — harness pattern benefiting from checkpoints
- [[Agent Harness]] — broader category of agent infrastructure
- [[Snapshot and Restore]] — related technical pattern
- [[Git Ledger]] — complementary version control approach
