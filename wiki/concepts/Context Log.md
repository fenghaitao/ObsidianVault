---
title: "Context Log"
type: concept
tags: [agents, durability, llm, append-only-log, context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

A Context Log is an append-only log of all LLM interactions within an agent session — system messages, user messages, tool calls, tool results, and assistant responses. It is the first and most important half of agent durability, providing context persistence that survives machine crashes and code version upgrades.

## Key Information

- **Contents**: Everything that went in and out of the LLM — system messages, user messages, tool calls, tool results, assistant responses.
- **Properties**:
  - Append-only: new entries are added, existing entries are never modified
  - Extremely valuable: represents the complete interaction history of the agent
  - Scales well: append-only logs are a well-understood, scalable primitive
- **Durability mechanisms**: Can be made durable using any existing primitive — databases, object storage, distributed file systems. Many technologies are specialized in making append-only logs durable.
- **Cross-version durability**: When the context log is saved externally, you can upgrade your agent harness (code) and still use the same context. The log is independent of the code that produced it.
- **Crash recovery**: If the machine crashes, the context log is saved elsewhere, so the agent can pick up where it left off.
- **Relationship to Replay Model**: Context logs are compatible with the replay approach — each LLM call and tool call can be a step in the replay journal.
- **Relationship to Snapshot and Restore**: Context logs handle the "what was said" half of durability; execution snapshots handle the "what was running" half. Together they provide complete agent durability.
- **Contrast with Execution Snapshot**: Context is an append-only log (easily durable); execution state (files, processes, memory) requires snapshot/restore.

## Related

- [[Execution Snapshot]] — the complementary durability mechanism for execution state
- [[Snapshot and Restore]] — the overall snapshot approach
- [[Replay Model]] — durability approach compatible with context logs
- [[DurableAgents]] — the broader concept
- [[Stateful Compute]] — the paradigm shift
- [[Agent Memory]] — related agent memory concept
- [[AppendOnlyLog]] — the underlying data structure pattern
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
