---
title: "DBOS"
type: entity
tags: [durable-execution, postgres, python, infrastructure]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS.md]
last_updated: 2026-06-25
---

## Definition

DBOS is a lightweight durable execution library built on top of Postgres. It checkpoints workflow progress so applications can survive crashes and resume from where they left off. Integrates with PydanticAI via a one-line `DBOSAgent` wrapper.

## Key Information

- Built on Postgres — no separate orchestration server or dedicated workers needed
- Python decorators make functions durable
- PydanticAI integration: wrap any agent with `DBOSAgent` for automatic checkpointing
- Supports parallel workflows via `start_workflow_async`
- Workflow forking: explore alternative paths from any checkpoint
- Auto-exports traces to Logfire
- Co-founded by Qian Li

## Related

- [[DurableExecution]] — the concept
- [[PydanticAI]] — agent framework
- [[Logfire]] — observability integration
- [[summary-20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS]] — source
