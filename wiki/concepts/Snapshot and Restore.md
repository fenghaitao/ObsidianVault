---
title: "Snapshot and Restore"
type: concept
tags: [durable-execution, microvm, agents, infrastructure, checkpoint]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

Snapshot and Restore is a durability approach for AI agents that captures the entire execution state of a virtual machine (files, memory, subprocesses, running servers) as a snapshot, saves it to disk, shuts down the machine, and restores it later when the agent needs to continue. It is the alternative to the Replay Model for making agents durable across turns.

## Key Information

- **Problem solved**: Agents accumulate execution state (cloned repos, installed packages, in-memory datasets, running dev servers, subprocesses) that cannot be made durable via a log-based replay approach.
- **How it works**: Snapshot the entire VM → shut it down → save to disk → when the next user message arrives, restore the VM and pick up exactly where it left off.
- **Cost efficiency**: Don't need to keep the machine running while waiting for user input (e.g., user goes to lunch). Compared to running the machine live, snapshot/restore is cheap.
- **Durability across turns**: Enables preserving everything the agent was doing between user interactions without continuous compute costs.
- **Error recovery**: LLM failures → snapshot and wait for retry; machine crashes → recover from context log instead.
- **Implementation history at Trigger.dev**:
  - **CRIU (2024)**: Process-level checkpoint/restore, millions of operations shipped. Limitations: process-only, only open files, container registry overhead.
  - **Firecracker microVMs (2025)**: Full-machine snapshots. Everything on the VM is captured. Optimized from 512MB to ~14MB compressed using seekable compression and lazy page restoration.
- **Performance**: Snapshots under 1 second, restores in hundreds of milliseconds. FC Run achieves ~15,000 VM starts per minute.
- **Combined with Context Log**: Snapshot handles execution durability; Context Log handles context durability. Together they yield truly durable agents.
- **Historical precedent**: IBM mainframes (1966) had checkpoint and restore for expensive long-running jobs.

## Related

- [[Replay Model]] — the alternative durability approach
- [[Execution Snapshot]] — the captured VM state
- [[Context Log]] — the complementary durability mechanism for LLM context
- [[Stateful Compute]] — the paradigm shift enabled by snapshot/restore
- [[FCRun]] — open-source CLI implementing snapshot/restore
- [[Firecracker]] — microVM technology used for snapshots
- [[CRIU]] — earlier process-level checkpoint tool
- [[Seekable Compression]] — optimization technique for snapshots
- [[DurableAgents]] — the broader concept
- [[MicroVMArchitecture]] — related infrastructure pattern
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
