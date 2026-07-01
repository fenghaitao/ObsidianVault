---
title: "Seekable Compression"
type: concept
tags: [compression, microvm, optimization, snapshot, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

Seekable Compression is a compression technique used by Trigger.dev to dramatically reduce snapshot sizes for Firecracker microVMs. Unlike standard compression, it allows decompressing only the specific memory pages that are needed at restore time rather than decompressing the entire snapshot, enabling fast partial restores.

## Key Information

- **Purpose**: Reduce VM snapshot sizes from hundreds of megabytes to tens of megabytes while maintaining fast restore times.
- **How it works**: Instead of decompressing the entire snapshot at restore time, only the specific memory pages that are actually accessed are decompressed on demand. This is combined with lazy page restoration.
- **Results at Trigger.dev**: Snapshots reduced from 512MB (default VM size) to approximately 14MB compressed.
- **Combined techniques**:
  - Seekable compression (on-demand decompression of individual pages)
  - Layering (incremental snapshots that only store changes)
  - Lazy page restoration (restore pages only when accessed, not all at once)
- **Tunable**: Compression level is a knob that can be adjusted based on performance requirements — more compression saves storage/transfer costs, less compression improves restore speed.
- **Impact**: Makes snapshot/restore economically viable for production agent infrastructure by reducing storage costs, network transfer costs, and restore latency.

## Related

- [[Firecracker]] — microVM technology using seekable compression
- [[Snapshot and Restore]] — the durability approach
- [[Execution Snapshot]] — the compressed VM state
- [[FCRun]] — the CLI implementing these optimizations
- [[TriggerDev]] — company that developed the technique
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
