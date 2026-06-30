---
title: "summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM"
type: source
tags: [source, transcript, agent-harness, reliability, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-29
---

## Core Summary

Tejas Kumar from IBM presents a deep dive on AI agent harnesses. An agent harness is "everything around the model that gives it grounding in reality" — the scaffolding that ties a black-box LLM to a stable environment for reliability. He covers the anatomy of harnesses, why they matter for token-paying users, and how they co-evolve with models.

## Key Information

- Agent harness = everything around the model that gives it grounding in reality. Claude Code is an example of a harnessed coding agent.
- Why harness: models are black boxes you rent; harness provides reliability irrespective of model behavior.
- Harness anatomy: agent loop, tools, MCP servers, sub-agents, context (claude.md, skills, slash commands), permissions, verification.
- ML harness vs AI agent harness: ML harness is a test suite for model quality; agent harness is the runtime scaffolding.
- Harnesses co-evolve with models: as models get smarter, some harness components become less necessary or evolve.
- IBM's work includes training frontier models and building harnesses.

## Related

- [[TejasKumar]] — speaker, AI developer advocate at IBM
- [[IBM]] — company
- [[AgentHarness]] — core concept
- [[ClaudeCode]] — example of a harnessed coding agent
- [[AgentLoop]] — core harness component
- [[ModelReliability]] — why harnesses matter
