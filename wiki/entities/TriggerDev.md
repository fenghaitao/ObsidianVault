---
title: "Trigger.dev"
type: entity
category: company
tags: [company, durable-agents, microvm, infrastructure, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

# Trigger.dev

## Definition

Trigger.dev is a platform for deploying durable AI agents to production. Founded by Eric Allam, the company has been working on making it easy to deploy long-running, durable agents that can recover from errors across turns and code versions. Their infrastructure combines context durability (append-only logs) with execution durability (VM snapshot/restore via Firecracker microVMs).

## Key Information

- **Founded by**: [[Eric Allam]], CEO and co-founder
- **Core technology**: Durable agent infrastructure combining context logs and execution snapshots
- **Snapshot history**: Shipped CRIU-based checkpoint/restore in 2024 (millions of operations); migrated to Firecracker microVMs for full-machine snapshots
- **Open-source tool**: FC Run ([[FCRun]]), a Docker-like CLI for running containers in Firecracker VMs with snapshot/restore capabilities
- **Performance**: Snapshots under 1 second, restores in hundreds of milliseconds; ~15,000 VM starts per minute with FC Run
- **Snapshot optimization**: Compressed snapshots from 512MB to ~14MB using seekable compression, layering, and lazy page restoration
- **Approach**: Two-pronged durability — context as append-only log (scalable, version-tolerant) plus execution as VM snapshots (preserves all machine state)

## Related

- [[Eric Allam]] — CEO and co-founder
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
- [[DurableAgents]] — the broader durable agents concept
- [[Replay Model]] — traditional durable execution approach
- [[Snapshot and Restore]] — VM-level checkpoint/restore
- [[Context Log]] — append-only log for LLM interactions
- [[Execution Snapshot]] — capturing full VM state
- [[Stateful Compute]] — paradigm shift
- [[FCRun]] — open-source Firecracker CLI
- [[Firecracker]] — AWS microVM technology
- [[CRIU]] — Checkpoint/Restore in Userspace
- [[Seekable Compression]] — snapshot compression technique
