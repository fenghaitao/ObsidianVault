---
title: "Replay Model"
type: concept
tags: [durable-execution, workflow, agents, event-sourcing, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

The Replay Model is a durable execution approach that builds durability on top of existing stateless compute architecture. Each side effect is wrapped in a cached step; when execution is retried after a failure, previously completed steps are skipped and execution resumes from the point of failure. This is the approach used by workflow and durable execution engines like Temporal.

## Key Information

- **Mechanism**: Every side effect (API call, database write, email send) is wrapped as a step that gets cached upon execution. On retry, the system replays the event journal, skipping completed steps.
- **Benefits**:
  - Built on existing stateless compute architecture (no infrastructure changes needed)
  - Provides execution history / audit trail of everything that happened
  - Enables resuming to a specific point in time (waiting for external events like human input)
- **Downsides**:
  - Rigid structure: code must be written in a specific way (steps + deterministic code outside steps)
  - Replay journal versioning is tricky when deploying new code versions
  - Applied to agents: every LLM call and tool call becomes a step, causing logs to grow unboundedly
  - Hits fundamental limits (entry count, entry size) as agent durations increase
- **Agent mismatch**: Agents are sessions, not transactions. Replay was designed for multi-step workflows with clear start/end; agents persist indefinitely, making replay logs unsustainable.
- **Historical context**: Emerged 10-15 years ago to solve the problem of multi-step side effects (e.g., process order → charge credit card → send receipt, where retrying the whole thing would double-charge)
- **Contrast with Snapshot Model**: Replay reconstructs state from a log; Snapshot captures state directly.

## Related

- [[DurableAgents]] — the broader concept
- [[DurableAgenticLoop]] — combining agentic loop with durability
- [[Snapshot and Restore]] — the alternative approach
- [[Stateful Compute]] — the paradigm shift away from replay-friendly stateless compute
- [[Context Log]] — append-only log, compatible with replay
- [[Execution Snapshot]] — the snapshot approach for execution state
- [[StepCaching]] — the underlying caching mechanism in replay
- [[EventSourcing]] — the underlying pattern
- [[TemporalWorkflows]] — workflow engine using replay
- [[HappyPathProgramming]] — developer philosophy enabled by replay
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
