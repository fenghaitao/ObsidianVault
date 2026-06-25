---
title: "DurableExecution"
type: concept
tags: [agents, reliability, infrastructure, state]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS.md, raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Durable execution is the pattern of checkpointing workflow progress so that if a process crashes or is interrupted, it can resume from the last checkpoint rather than restarting from the beginning. Critical for long-running AI agent workflows where restarting wastes tokens, time, and money.

## Key Information

### In AI Agents

- Agent workflows involve multiple LLM calls, tool invocations, and sub-agent delegations — each step costs tokens and time
- Without durable execution, a server crash or redeploy means restarting the entire workflow
- With durable execution, each step is checkpointed to a database; on restart, execution resumes from the last completed step

### Implementations

- **DBOS**: lightweight durable execution library built on Postgres. Wraps PydanticAI agents with `DBOSAgent`. Checkpoints every tool call and agent step. Supports workflow forking (explore alternative paths from any checkpoint).
- **Monty**: supports runtime snapshotting — serialize the entire interpreter state to binary, store in database, resume later. Orders of magnitude smaller than snapshotting a full VM.
- **Render Workflows**: platform-level durable execution with checkpoint, recovery, and retry for deployed agents

### Key Benefits

- Saves tokens: don't re-run completed LLM calls
- Saves time: resume from checkpoint instead of restarting
- Enables long-running agents: workflows that take hours or days
- Enables debugging: fork from any checkpoint to explore alternative paths
- Enables auditing: full history of every step preserved

## Related

- [[DBOS]] — durable execution library
- [[Monty]] — interpreter with snapshot support
- [[Render]] — platform with workflow support
- [[AgentInfrastructure]] — the broader infrastructure layer
- [[PydanticAI]] — agent framework with DBOS integration
