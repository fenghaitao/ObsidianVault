---
title: "Amazon S3"
type: entity
tags: [product, AWS, storage, object-storage]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-14
---

## Definition

Amazon S3 (Simple Storage Service) is AWS's object storage service, built about 20 years ago, which Marc Brooker cites as the durability layer underneath Aurora D SQL.

## Key Information

- Object store built ~20 years ago; Brooker describes D SQL as making "this block store… object store… the underlying durability layer of this new database."
- Brooker credits S3's success to its builders being deep in the details, grounded in the use cases and economics, from all levels of leadership.
- Al Vermeulen was a major contributor to S3's design.
- James Cowling: Dropbox migrated off S3 to its own Magic Pocket storage system — among the largest data migrations in history, peaking at ~764 Gbps of peering bandwidth — and kept a "trampoline" to overflow data back to S3 under capacity pressure; Cowling calls S3 "effectively elastic storage."

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[AWS]] — the provider
- [[Amazon]] — the parent company
- [[Marc Brooker]] — describes S3's role in D SQL
- [[Al Vermeulen]] — helped design S3
- [[Amazon Aurora]] — the database built on S3
- [[Dropbox]] — the company that migrated off S3
- [[Magic Pocket]] — the system that replaced it at Dropbox
- [[Trampoline]] — Dropbox's S3 overflow hatch
- [[Dark Launch]] — the migration safety strategy
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
