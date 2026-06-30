---
title: "Firecracker"
type: concept
tags: [microvm, aws, infrastructure, virtualization, durable-execution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

Firecracker is an open-source microVM (micro virtual machine) technology developed by AWS that enables fast, lightweight virtual machine creation with full-machine snapshot and restore capabilities. Trigger.dev uses Firecracker microVMs as the foundation for their execution snapshot infrastructure for durable AI agents.

## Key Information

- **Developer**: AWS (Amazon Web Services)
- **Type**: MicroVM — a lightweight virtual machine designed for serverless and container workloads
- **Key capability**: Full-machine snapshots — can snapshot everything on the VM (files, memory, processes, network state) regardless of what's running
- **Advantages over CRIU for durable agents**:
  - Captures the entire machine, not just a single process (works with FFmpeg, Chrome instances, etc.)
  - No limitation to open files — captures the full filesystem
  - No container registry push/pull overhead when used directly
- **Optimization techniques used by Trigger.dev**:
  - Seekable compression: compressed snapshots from 512MB default to ~14MB
  - Layering: incremental snapshot layering
  - Lazy page restoration: only decompress memory pages when they're actually accessed during restore
- **Performance with FC Run**: Snapshots under 1 second, restores in hundreds of milliseconds
- **Use in Trigger.dev**: Replaced CRIU in 2025 as the snapshot/restore backend for durable agents
- **Comparison to CRIU**: CRIU is process-level (limited scope, registry overhead); Firecracker is VM-level (complete capture, faster)

## Related

- [[FCRun]] — Docker-like CLI for Firecracker
- [[CRIU]] — earlier process-level checkpoint tool
- [[Snapshot and Restore]] — the durability approach
- [[Execution Snapshot]] — the captured VM state
- [[MicroVMArchitecture]] — related infrastructure pattern
- [[Trigger.dev]] — company using Firecracker for durable agents
- [[Seekable Compression]] — optimization technique
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
