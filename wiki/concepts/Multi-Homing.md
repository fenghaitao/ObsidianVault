---
title: "Multi-Homing"
type: concept
tags: [replication, distributed-systems, storage, availability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Multi-homing is the ability to keep data in two (or more) locations/homes, spanning from lazily replicated primary-secondary setups for business continuity to active-active replication where writes only externalize success after landing in all regions.
## Key Information
- Primary-secondary (lazily replicated) multi-homing: writes commit authoritatively in one region and replicate to a secondary, used for business continuity with a window of potential data loss.
- Active-active multi-homing: a truly authoritative copy exists in multiple locations; a write isn't reported as succeeded until it has landed everywhere.
- Dropbox's block storage was a genuine multi-region replicated system — an entire region (e.g., Ashburn, Virginia) could go down with zero downtime and safe data.
- Cowling generally advises most companies NOT to adopt active-active multi-homing: the cost is high because the speed of light is fixed (~60ms added to a cross-US commit path), and avoiding that complexity lets you move faster and build a better product.
- It makes sense only when storing data at exabyte scale for hundreds of millions of customers is the business, as at Dropbox.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — used true multi-region replication
- [[Erasure Coding]] — the other half of Dropbox durability
