---
title: "FCRun"
type: concept
tags: [microvm, firecracker, open-source, infrastructure, durable-execution, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

FC Run (also spelled FCRun or F Crun) is an open-source Docker-like CLI tool developed by Trigger.dev for running containers in Firecracker microVMs with built-in snapshot and restore capabilities. It provides a drop-in replacement for the Docker command, enabling fast VM starts, snapshots, restores, and forking.

## Key Information

- **Developer**: [[Trigger.dev]]
- **Status**: Open source, to be released soon (as of May 2026)
- **Interface**: Docker-like CLI — can be used as a drop-in replacement for the Docker command
- **Core capabilities**:
  - Run containers in Firecracker VMs (e.g., `fcrun run alpine`)
  - Snapshot a running VM (extremely fast)
  - Restore a VM from snapshot
  - Fork a VM (create a copy from a running VM)
- **Performance**:
  - ~15,000 VM starts per minute (~30 FPS equivalent)
  - Snapshots under 1 second
  - Restores in hundreds of milliseconds
- **Underlying technology**: Firecracker microVMs with seekable compression, layering, and lazy page restoration
- **Use case**: Powers Trigger.dev's future compute layer for durable agents
- **Benchmark**: TTI (Time to Interact — how long for a VM to become reachable on the internet) measured in milliseconds

## Related

- [[Firecracker]] — the microVM technology
- [[Trigger.dev]] — the company behind FC Run
- [[Eric Allam]] — Trigger.dev CEO
- [[Snapshot and Restore]] — the durability approach enabled by FC Run
- [[Execution Snapshot]] — the captured VM state
- [[Stateful Compute]] — the paradigm shift
- [[DurableAgents]] — the broader concept
- [[MicroVMArchitecture]] — related infrastructure pattern
- [[Seekable Compression]] — optimization technique used
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
