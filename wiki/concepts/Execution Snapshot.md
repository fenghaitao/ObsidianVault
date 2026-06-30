---
title: "Execution Snapshot"
type: concept
tags: [durable-execution, microvm, agents, infrastructure, checkpoint]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

An Execution Snapshot is a point-in-time capture of the entire virtual machine state — files, memory, subprocesses, running servers, cloned repositories, installed packages — used to make the execution layer of an AI agent durable across turns without keeping the machine continuously running.

## Key Information

- **Purpose**: Preserve everything an agent was doing (cloned GitHub repos, installed packages, in-memory datasets, running dev servers, sandboxed subprocesses) between user interactions.
- **Why needed**: Execution state cannot be made durable via a log (unlike context). You can't replay your way back to a running dev server or in-memory state.
- **Mechanism**: Snapshot the VM → shut down → save to disk → restore when next user message arrives.
- **Cost model**: Much cheaper than keeping the machine running continuously while waiting for user input.
- **Error recovery role**: When the LLM is temporarily unavailable, snapshot and wait rather than keeping the machine alive in memory.
- **Trigger.dev implementation**:
  - Started with CRIU (process-level, 2024)
  - Migrated to Firecracker microVMs for full-machine snapshots
  - Optimized with seekable compression, layering, and lazy page restoration
  - Compressed from 512MB default to ~14MB
- **Performance**: Snapshots under 1 second, restores in hundreds of milliseconds
- **Contrast with Context Log**: Execution snapshots handle the "what was running" half of durability; context logs handle the "what was said" half.

## Related

- [[Snapshot and Restore]] — the overall approach
- [[Context Log]] — the complementary durability mechanism for LLM context
- [[Stateful Compute]] — the paradigm shift enabled by execution snapshots
- [[FCRun]] — open-source CLI implementing snapshot/restore
- [[Firecracker]] — microVM technology
- [[CRIU]] — earlier process-level checkpoint tool
- [[Seekable Compression]] — optimization technique
- [[DurableAgents]] — the broader concept
- [[MicroVMArchitecture]] — related infrastructure pattern
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
