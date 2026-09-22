---
title: "Dark Launch"
type: concept
tags: [migration, deployment, safety, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Dark launch, in the context of Dropbox's S3 migration, is the practice of dual-writing data to both the old and new storage systems while keeping the new one out of the read path, until safety is proven.
## Key Information
- During the migration, data was moved off S3 but kept in both locations; the team had to demonstrate no downtime, no data loss, and no incidents for six months before deleting any S3 data.
- A bug slipped through to production once; nothing bad happened, but Cowling went to the VP and voluntarily reset the launch clock, delaying the launch and costing double-digit millions — leadership endorsed prioritizing user safety.
- After durability was proven and validators ran 24/7 in production, the team switched over reads and migrated "as fast as we could," peaking around 764 Gbps of peering bandwidth.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company running the migration
- [[Amazon S3]] — the system being migrated off
