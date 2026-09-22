---
title: "Two-Phase Commit"
type: concept
tags: [distributed-systems, transactions, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Two-phase commit (with two-phase locking) is the standard protocol for having multiple nodes agree to commit a transaction atomically: participants lock their state, block other work, and then commit together.
## Key Information
- James Cowling describes it as the default approach for multi-node agreement on a transaction.
- Downside 1 — low performance: nodes block for the duration of the transaction.
- Downside 2 — high risk: it takes a dependency on another node ("you basically block waiting for another node to return").
- Cowling's Granola work aimed to coordinate one-shot/independent transactions without it, by exchanging timestamps instead.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Transactions]] — what it coordinates
- [[Granola]] — the approach that avoids it
