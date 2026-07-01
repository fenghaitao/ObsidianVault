---
title: "ValidationContracts"
type: concept
tags: [multi-agent, missions, orchestration, testing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory.md"]
last_updated: 2026-06-29
---

## Definition

Validation contracts are definitions of "done" established before any coding begins in a multi-agent mission. Created by the orchestrator during planning, they define what constitutes successful completion and are used by validators to verify behavior end-to-end, preventing drift over long-running autonomous tasks.

## Key Information

- Part of Factory's missions architecture (three-role system: orchestrator, worker, validator)
- Defined during planning phase, before implementation
- Goes beyond lint/type-check/tests to validate actual behavior end-to-end
- Enables missions to run for hours or days without drifting

## Related

- [[summary-20260506 - The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory]] — source
- [[FactoryAI]] — implementing platform
- [[MultiAgentArchitecture]] — broader context
- [[Agent Orchestration]] — orchestrator role
