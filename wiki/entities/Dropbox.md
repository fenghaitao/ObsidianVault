---
title: "Dropbox"
type: entity
tags: [company, storage, file-sync, collaboration]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Dropbox is a file-sync, storage, and collaboration company founded by Drew Houston. James Cowling joined in 2012 and became its most senior engineer, leading the Magic Pocket storage system that migrated the company off Amazon S3.
## Key Information
- Started as a file sync-and-share category company, later reshaping itself around collaboration.
- Cowling spoke with founder Drew Houston about the S3 migration project as early as 2010, before joining in 2012.
- Owned an exabyte-scale storage system (Magic Pocket) advertising at least 12 nines of durability, modeled around 24 nines.
- Design goal of the storage system: make the cost pie chart almost entirely disks, minimizing spending on RAM, compute, network, power, and sheet metal.
- Went from S3 to an in-house storage system for strategic control and massive cost efficiencies before the company was public.
- Uses erasure coding with a custom Vandermonde encoding matrix, varied rack/power/disk generations, and multi-region replication.
- The S3 migration used a six-month "no incidents, no data loss" dark-launch contract; Cowling voluntarily reset the clock after a bug slipped through, a decision leadership endorsed.
- Cowling's team renamed itself from "Magic Pocket team" to "Storage team" so its identity would track the problem it solves, not the system it built.
- Early infra was tiny (~7–9 people); the culture emphasized ownership and "there's no other idiots out there — it's just us."
- Dropbox has cultural values that explicitly reward prioritizing user safety and doing the right thing.
- On the S3 exit, counter-negotiation details: Amazon was unaware of the migration for a long time (though data-center contacts noticed Dropbox buying capacity), and even Dropbox's already-deep S3 discounts couldn't beat Magic Pocket's cost efficiency.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[James Cowling]] — most senior engineer
- [[Drew Houston]] — founder
- [[Magic Pocket]] — the storage system
- [[Discotech]] — the disk technology project
- [[Trampoline]] — S3 overflow hatch
- [[Convex]] — founded by Cowling after Dropbox
- [[Jamie Turner]] — Dropbox engineer, later Convex co-founder
- [[Go (Programming Language)]] — Magic Pocket's primary language
- [[Silicon Valley (TV Show)]] — drew on Dropbox-era stories
- [[Dark Launch]] — the S3 migration safety strategy
- [[FMEA (Failure Mode and Effects Analysis)]] — reliability practice used
- [[System Bias]] — the org inertia Cowling fought
- [[Amazon S3]] — the service it migrated off
- [[Erasure Coding]] — durability technique used
- [[Multi-Homing]] — replication strategy considered
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[Tiered Storage]] — the hot/cold storage design
