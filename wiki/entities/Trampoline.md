---
title: "Trampoline"
type: entity
tags: [project, storage, Dropbox, overflow]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Trampoline was a Dropbox system that let the storage team, under worst-case capacity pressure, dump excess data to Amazon S3 and later move it back — an "escape hatch" that let them run capacity closer to the edge without sacrificing durability.
## Key Information
- Allowed, for example, offloading 30 petabytes to S3 when the system got too close to a capacity threshold.
- Rarely used in anger; the team tested it periodically to ensure it worked.
- Served as a safety valve precisely because S3 acts as effectively elastic storage one hop away.
- Never used as a way to reduce durability — durability was an absolute, non-negotiable constraint.
- Contrasted with Instagram-style "DEFCON knobs": Dropbox never degraded durability, but kept load-shedding knobs for background processes, CPU, memory, and test load to ride out spikes.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company that built it
- [[Magic Pocket]] — the storage system it backstopped
- [[Amazon S3]] — the overflow destination
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
