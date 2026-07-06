---
title: "summary-2026-01-23 - Building multi-agent systems When and how to use them"
type: source
tags: [source, multi-agent-systems, architecture, orchestration]
sources: ["raw/01-articles/claude/2026-01-23 - Building multi-agent systems When and how to use them.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's guide to the orchestrator-subagent multi-agent pattern (a lead agent spawning specialized subagents), arguing most teams don't need multi-agent systems — coordination overhead means they typically use 3-10x more tokens than a single agent for equivalent tasks — but identifying three scenarios where the tradeoff pays off: context pollution, parallelizable tasks, and specialization needs. First in a planned series on multi-agent patterns.

## Key Points

- **Three scenarios that justify multi-agent systems**: (1) **context pollution** — isolating a subtask (e.g., a 2000+ token order lookup) in its own subagent keeps the main agent's context focused, returning only a compact summary; (2) **parallelizable tasks** — a lead agent decomposes a query into independent facets and runs subagents concurrently (Anthropic's Research feature works this way), trading higher token cost for broader coverage, not necessarily speed; (3) **specialization** — different tasks need different toolsets, personas, or domain context (e.g., a CRM agent vs. a marketing-automation agent, each with 8-10 focused tools instead of one agent juggling 40+).
- **Concrete adoption signals**: approaching context limits (though compaction is reducing this), managing 15-20+ tools (consider the Tool Search Tool first — up to 85% token reduction via on-demand tool discovery — before splitting agents), and naturally parallelizable subtasks.
- **Context-centric decomposition, not problem-centric**: splitting by work type (one agent writes features, another writes tests, a third reviews) creates a "telephone game" where each handoff loses context — in one experiment, role-specialized subagents (planner/implementer/tester/reviewer) spent more tokens coordinating than working. Instead, split along context boundaries: an agent handling a feature should also handle its own tests, since it already has the needed context.
- **Verification subagents** are a consistently effective pattern: a dedicated agent whose only job is testing/validating the main agent's work, since verification requires minimal context transfer (blackbox testing an artifact against explicit criteria, not understanding how it was built). More capable orchestrators (e.g., Claude Opus 4.5) increasingly evaluate subagent work directly without needing this step, but it remains valuable with less capable orchestrators or specialized verification tooling. Main failure mode: a verifier declaring success after only shallow testing — mitigated by requiring complete test-suite runs and explicit pass criteria.
- **Default advice**: start with the simplest single-agent approach that works; add multi-agent complexity only when evidence (not intuition) supports it.
- Written by Cara Phillips, with Paul Chen, Andy Schumeister, Brad Abrams, Theo Chu.

## Related

- [[MultiAgentSystem]] — the concept this article defines in depth
- [[ClaudeCodeSubagents]] — Claude Code's own subagent implementation, exemplifying the same context-isolation and verification patterns
- [[ContextEngineering]] — the discipline underlying context-centric decomposition
- [[Research]] — Anthropic's own parallel multi-agent research feature
