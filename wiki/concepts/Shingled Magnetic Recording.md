---
title: "Shingled Magnetic Recording"
type: concept
tags: [storage, disks, hardware, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-23
---

## Definition

Shingled magnetic recording (SMR) is a disk technology that overlaps ("shingles") data tracks to increase storage density. Dropbox used new, experimental SMR disks at scale — the first to do so, per James Cowling — to make Magic Pocket cheaper per byte than generic object storage.

## Key Information

- SMR boosts per-disk capacity but changes the write model; Dropbox paired it with zone-based control (ZBC) and addressed the disk directly rather than going through a filesystem.
- Cowling: adopting these experimental disks was one of two reasons Magic Pocket became more cost-efficient than Amazon S3 (the other being a deep understanding of Dropbox's own workloads).
- Driving SMR disks directly required operating off draft specifications provided by the disk manufacturers.

## Related

- [[Magic Pocket]] — the storage system built on SMR disks
- [[Discotech]] — the disk-technology project
- [[Zoned Storage]] — the interface pattern used to control SMR disks
- [[Dropbox]] — the company that adopted SMR at scale
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
