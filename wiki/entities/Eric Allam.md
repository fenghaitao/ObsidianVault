---
title: "Eric Allam"
type: entity
category: person
tags: [person, speaker, durable-agents, trigger-dev, microvm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

# Eric Allam

## Definition

Eric Allam is the CEO and co-founder of Trigger.dev, a platform for deploying durable AI agents to production. He presented "Two Roads to Durable Agents: Replay vs. Snapshot" at aiDotEngineer, where he traced the 30-year history of backend infrastructure and argued that agents demand a paradigm shift from stateless to stateful compute.

## Key Information

- **Role**: CEO and co-founder of Trigger.dev
- **Company**: [[Trigger.dev]]
- **Known for**: Building infrastructure for durable AI agents, developing snapshot/restore capabilities using Firecracker microVMs and CRIU
- **Presentation**: "Two Roads to Durable Agents: Replay vs. Snapshot" (2026-05-10, aiDotEngineer)
- **Key contributions**: Shipped CRIU-based snapshot/restore in 2024 (millions of operations), later migrated to Firecracker microVMs; building FC Run (FCRun), an open-source Docker-like CLI for Firecracker VMs
- **Core thesis**: Agents need both context durability (append-only log) and execution durability (snapshot/restore); combining replay and snapshot approaches yields truly durable agents

## Related

- [[Trigger.dev]] — company founded by Eric
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
- [[DurableAgents]] — the broader concept
- [[Replay Model]] — traditional durable execution approach
- [[Snapshot and Restore]] — VM-level checkpoint/restore
- [[Context Log]] — append-only log for LLM interactions
- [[Execution Snapshot]] — capturing full VM state
- [[Stateful Compute]] — paradigm shift from stateless compute
- [[FCRun]] — open-source Firecracker CLI
- [[Firecracker]] — AWS microVM technology
- [[CRIU]] — Checkpoint/Restore in Userspace
- [[Shared Nothing Architecture]] — the old stateless compute paradigm
- [[Seekable Compression]] — snapshot compression technique
- [[aiDotEngineer]] — conference
