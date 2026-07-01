---
title: "summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev"
type: source
tags: [source, transcript, durable-agents, replay, snapshot, stateful-compute, microvm, trigger-dev]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Core Summary

Eric Allam, CEO of Trigger.dev, presents two fundamental approaches to building durable AI agents: the Replay Model (traditional durable execution via event sourcing and step caching) and the Snapshot Model (VM-level checkpoint/restore using Firecracker microVMs). He traces the 30-year history of backend infrastructure from CGI through the Shared Nothing Architecture to modern workflows, then argues that agents demand a paradigm shift from stateless to stateful compute. The key insight: agents have two halves — context (append-only log of LLM interactions) and execution (machine state like cloned repos, running servers) — and each requires a different durability strategy. Replay works for context but falls over for execution; snapshot/restore handles execution but not context. Combining both yields truly durable agents.

## Key Points

- **Historical context**: Backend infrastructure has been stateless for 30 years — from CGI (1993) to PHP/LAMP to Rails/Node/serverless — all following the Shared Nothing Architecture where compute is stateless and state lives in the database.
- **Replay Model**: Durable execution engines (Temporal, workflow engines) wrap side effects in cached steps. On retry, completed steps are skipped. Gives audit trail and resume capability but imposes rigid structure, requires deterministic code, and has versioning challenges.
- **Agent loop challenge**: The LLM orchestrates code (inverse of traditional workflows). Replay applied to agents means every LLM call and tool call becomes a step. Logs grow unboundedly and hit fundamental limits as agent durations increase (doubling every 4-7 months).
- **Agents are sessions, not transactions**: Unlike workflows with clear start/end, agents persist as long as the user wants. Replay is built for transactions; agents need session-level durability.
- **Two halves of an agent**: Context (system messages, user messages, tool calls, tool results, assistant responses) is an append-only log — durable via databases, object storage, or distributed file systems. Execution (files, memory, subprocesses, cloned repos, dev servers) needs snapshot/restore.
- **Context Log**: Append-only, scales well, durable across code versions. When the log is saved externally, you can upgrade your harness and still use the same context, or recover from machine crashes.
- **Snapshot and Restore**: Snapshot the entire VM, shut it down, save to disk, restore when the next user message arrives. Enables durability across turns without keeping the machine running (cost-efficient). Preserves everything the agent was doing.
- **Error recovery dual strategy**: LLM failures → snapshot and wait; machine crashes → recover from context log.
- **CRIU (2011)**: Checkpoint/Restore in Userspace — injects a "parasite" into a process to dump state. Trigger.dev shipped this in 2024 and did millions of snapshot/restores. Limitations: process-only, only captures open files, container registry overhead.
- **Firecracker microVMs**: Moved to Firecracker for full-machine snapshots. Snapshots everything on the VM regardless of what's running. Default 512MB snapshots reduced to ~14MB compressed using seekable compression, layering, and lazy page restoration.
- **FC Run (FCRun)**: Open-source Docker-like CLI for running containers in Firecracker VMs with snapshot/restore. ~15,000 VM starts per minute, snapshots under a second, restores in hundreds of milliseconds.
- **Paradigm shift**: Agents force the move from stateless compute to stateful compute, with snapshot/restore at the heart of it.

## Related

- [[Eric Allam]] — speaker, CEO of Trigger.dev
- [[TriggerDev]] — company building durable agent infrastructure
- [[Replay Model]] — traditional durable execution via event sourcing
- [[Snapshot and Restore]] — VM-level checkpoint/restore for execution durability
- [[Context Log]] — append-only log of LLM interactions
- [[Execution Snapshot]] — capturing full VM state for durability
- [[Stateful Compute]] — the paradigm shift from stateless to stateful
- [[FCRun]] — open-source Firecracker CLI tool
- [[Firecracker]] — AWS microVM technology
- [[CRIU]] — Checkpoint/Restore in Userspace
- [[Shared Nothing Architecture]] — the 30-year old stateless compute paradigm
- [[Seekable Compression]] — compression technique for efficient snapshots
- [[DurableAgents]] — the broader durable agents concept
- [[MicroVMArchitecture]] — micro-VM infrastructure pattern
- [[DurableAgenticLoop]] — combining agentic loop with durability infrastructure
- [[aiDotEngineer]] — conference where this talk was presented
