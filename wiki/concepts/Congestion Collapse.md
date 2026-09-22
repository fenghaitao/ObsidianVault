---
title: "Congestion Collapse"
type: concept
tags: [reliability, distributed-systems, failure-modes, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Congestion collapse is the failure mode where a system's workload crosses a threshold and it collapses — in Magic Pocket, sparked when OOMed storage nodes look like disk failures and trigger a wave of re-replication that multiplies load many times over.
## Key Information
- Trigger example: a band released an album on Dropbox, spiking load onto a few files; the machines (and their disks) OOMed.
- Because an OOM/restart looks like a disk failure, the system tried to recover each affected node's data from replicas — turning one fire hose of incoming load into roughly seven fire hoses of reconstruction load.
- These cyclical behaviors can tip a system into congestion collapse, which Cowling calls the hardest part of building Magic Pocket.
- OOM unpredictability was a key reason the storage nodes were migrated from Go (garbage-collected runtime) to Rust.
- The team designed against it with pre-mortem/threat modeling (FMEA) and by keeping systems simple and decoupled.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Magic Pocket]] — the system where it occurred
- [[Metastable Failures]] — the broader failure-mode family
- [[Distributed Systems]] — the context
- [[Go (Programming Language)]] — its runtime contributed to the OOM storms
