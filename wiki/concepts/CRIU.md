---
title: "CRIU"
type: concept
tags: [checkpoint, restore, linux, process, durable-execution, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

CRIU (Checkpoint/Restore in Userspace) is a Linux tool developed in 2011 that enables suspending and restoring a running process from userspace. It works by injecting a "parasite" code into the target process, forcing it to dump all state to memory, then removing all traces of the injection. Trigger.dev shipped CRIU-based snapshot/restore in 2024 before migrating to Firecracker microVMs.

## Key Information

- **Year developed**: 2011
- **Mechanism**: Injects a "parasite" into the target process → forces the process to dump all state (memory, file descriptors, etc.) → removes all traces of the parasite → the process continues normally. The dumped state can be restored later.
- **Key properties**:
  - Transparent to the process: the process doesn't need to participate or be modified
  - Compatible with container runtimes
  - Works from userspace (no kernel modifications needed)
- **Trigger.dev usage (2024)**: Shipped CRIU-based snapshot/restore and performed millions of operations
- **Limitations that led to Firecracker migration**:
  - Process-only: can only checkpoint a single process. Doesn't work with child processes, FFmpeg, Chrome instances, etc.
  - Open files only: only captures files that are open at the time of snapshot; closed files are not preserved
  - Container registry overhead: compatibility with containers means working with registries (push/pull), which is slow
- **Legacy**: Despite limitations, CRIU proved that process-level checkpoint/restore was viable and paved the way for VM-level approaches

## Related

- [[Firecracker]] — the VM-level replacement
- [[Snapshot and Restore]] — the durability approach
- [[Execution Snapshot]] — the captured state
- [[TriggerDev]] — company that used CRIU in production
- [[FCRun]] — the Firecracker-based CLI that replaced CRIU
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
