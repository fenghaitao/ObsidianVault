---
title: "Tiered Storage"
type: concept
tags: [storage, architecture, cost-optimization, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-23
---

## Definition

Tiered storage is a design that splits data across multiple tiers with different cost/performance trade-offs. Dropbox used two clusters in Magic Pocket: a temporary, access-efficient-but-storage-inefficient tier for fresh writes, and a colder, more static tier for bulk long-term storage.

## Key Information

- Fresh data was written to the temporary tier first, then moved in bulk in the background to the colder tier.
- The cold tier used more efficient algorithms and bulk writes; it could even go down for writes without harming users because it sat off the live path.
- This separated the live write path from the long-term read path — an example of Cowling's "systems is all about trade-offs."
- Tiering was enabled by knowing the data's size, access pattern, frequency, and deletion timing — tuning a general-purpose service like S3 cannot do.

## Related

- [[Magic Pocket]] — the storage system that used a two-tier design
- [[Dropbox]] — the company that built it
- [[Shingled Magnetic Recording]] — the disk technology in the cold tier
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
