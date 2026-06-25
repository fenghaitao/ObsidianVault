---
title: "summary-20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS"
type: source
tags: [source, pydantic, dbos, durable-execution, agents]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS.md"]
last_updated: 2026-06-25
---

## Core Summary

Samuel Colvin and Qian Li (DBOS co-founder) demonstrate the PydanticAI + DBOS integration for durable, reliable AI agents. DBOS is a lightweight durable execution library built on Postgres that checkpoints agent workflow progress, enabling crash recovery without restarting from scratch. The demo shows a deep research agent with planning, search, and analysis agents that survives server crashes and can fork workflows from any checkpoint.

## Key Points

- DBOS provides durable execution by checkpointing every agent step and tool call to Postgres
- Integration is one line: wrap a PydanticAI agent with `DBOSAgent` to make it durable
- Sub-agent calls are also checkpointed and traced through DBOS
- Parallel search workflows fan out using `start_workflow_async` for concurrency
- Workflow forking allows exploring alternative paths from any checkpoint without rerunning earlier steps
- Logfire integration provides full observability of durable agent runs
- Demo: deep research agent searching for Python AI conferences survives kill/restart, resumes from analysis phase

## Related

- [[PydanticAI]] — agent framework
- [[DBOS]] — durable execution library
- [[Logfire]] — observability platform
- [[DurableExecution]] — concept of checkpointed, resumable workflows
