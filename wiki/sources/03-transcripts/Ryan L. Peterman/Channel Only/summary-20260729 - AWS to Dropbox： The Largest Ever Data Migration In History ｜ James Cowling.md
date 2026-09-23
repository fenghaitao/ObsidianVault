---
title: "summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-23
---

## Core Summary

James Cowling explains why Dropbox migrated off Amazon S3 to its own Magic Pocket storage system: strategic control of the company's destiny plus massive, pre-IPO cost savings. A small team made the system cheaper than S3 by pairing shingled magnetic recording (SMR) disks with a deep, workload-specific understanding of Dropbox's access patterns — trading the live write path against a colder bulk tier — while surviving the hardest challenge, congestion collapse, through Rust, direct disk control, and relentless failure-mode planning.

## Key Points

- Migration motivation: owning the file system was strategically valuable while Dropbox was a file sync/share company; the effort saved "a huge amount of money" before the company went public.
- Hard problems attract engineers: the tiny team dispersed after shipping — Jamie Turner redesigned the sync protocol/desktop client, while Cowling worked on the file system and distributed databases.
- AWS counter-negotiation: Amazon was unaware for a long time, then couldn't match Magic Pocket's efficiency despite Dropbox's already-deep S3 discounts, because S3 must optimize for every workload while Dropbox only had to optimize for its own.
- Workload-aware design: two tiers — an access-efficient temporary cluster and a colder, more static bulk cluster — separated the live write path from the long-term read path.
- Language path: Python prototype → Go (pre-GA) → Rust (pre-GA) for storage nodes, with the Rust rewrite coinciding with removing the filesystem and driving disks directly via ZBC draft specs (the Discotech project).
- Congestion collapse: one hot file (possibly a De La Soul album release) made nodes OOM; OOM restarts look like disk failures, triggering ~7x reconstruction load and potential cascading failure.
- Durability was non-negotiable; Dropbox instead kept load-shedding knobs (background CPU/memory/test load) and a "trampoline" to dump up to 30 PB of overflow to S3.
- Physical reality: two server-delivery trucks crashed in one week (~6 weeks of lost capacity), forcing buffer planning via FMEA-style pre-mortem.

## Related

- [[James Cowling]]
- [[Dropbox]]
- [[Drew Houston]]
- [[Amazon S3]]
- [[AWS]]
- [[Magic Pocket]]
- [[Discotech]]
- [[Trampoline]]
- [[Rust]]
- [[Go (Programming Language)]]
- [[Python]]
- [[Congestion Collapse]]
- [[FMEA (Failure Mode and Effects Analysis)]]
- [[Shingled Magnetic Recording]]
- [[Zoned Storage]]
- [[Tiered Storage]]
