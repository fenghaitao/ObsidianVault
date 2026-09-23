---
title: "Magic Pocket"
type: entity
tags: [project, storage, Dropbox, distributed-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Magic Pocket is the codename for Dropbox's in-house, exabyte-scale block storage system, built to migrate the company off Amazon S3 and reduce storage cost while achieving extreme durability.
## Key Information
- Built by a very small team (roughly 3–6 initial engineers), not thousands.
- Advertised at least 12 nines of durability; internally modeled around 24 nines ("the universe will be extinct before any data is lost").
- Used erasure coding with a custom Vandermonde encoding matrix, spreading fragments across racks, power feeds, drive generations, and manufacturers to avoid correlated failures; reads that "complete on the first six of nine fragments" make erasure-coded reads faster than non-replicated ones.
- Used new shingled magnetic recording (SMR) disks at scale (first to do so) and directly addressed disks via ZBC (zone-based control) rather than a filesystem.
- Language path: Python prototype → Go (pre-GA) → Rust (pre-GA) for storage nodes, coinciding with the Discotech disk work.
- Block mapping used a cluster of ~1,000 MySQL nodes keyed by block ID — deliberately "unsophisticated" so validation services could walk the table and verify placement.
- Migration off S3 used a six-month dark launch with double writes; at peak reached ~700–764 Gbps of peering bandwidth.
- Hardest problem: congestion collapse — OOMed nodes looked like disk failures, triggering many simultaneous re-replications (one fire hose of load becoming seven).
- Reserved a "trampoline" to dump overflow data (e.g., 30 PB) to S3 under worst-case capacity pressure; never compromised user durability.
- Renamed team identity to "Storage team" after shipping so the team advocated for storage needs, not for Magic Pocket itself.
- Workload-aware tiering: fresh writes landed first in a temporary (access-efficient, storage-inefficient) cluster, then moved in bulk in the background to a colder, more static cluster with more efficient bulk algorithms; the cold tier could go down for writes without affecting the live path.
- Optimization extended to power: rack amperage was sized against access patterns via the rack's PDU circuit-breaker, and a bad hardware batch could force extra re-replication that ran racks "really hot."
- Cowling cautions the migration only made sense at Dropbox's scale and that he "wouldn't recommend another company do this right now."
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company that built it
- [[James Cowling]] — its leader
- [[Discotech]] — the disk technology project
- [[Trampoline]] — the S3 overflow hatch
- [[Erasure Coding]] — its durability scheme
- [[Congestion Collapse]] — its hardest failure mode
- [[MySQL]] — the block-metadata store
- [[Go (Programming Language)]] — the primary implementation language
- [[Rust]] — the storage-node language
- [[Amazon S3]] — the service it replaced
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[Shingled Magnetic Recording]] — the experimental disks used
- [[Tiered Storage]] — the two-tier write/read design
