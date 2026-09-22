---
title: "Transactions"
type: concept
tags: [distributed-systems, databases, abstractions, concurrency]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
A transaction groups several operations ("a bunch of things at once") so they execute atomically, letting programmers manage concurrency — which James Cowling calls "probably the most difficult problem in computer science."
## Key Information
- Cowling calls transactions "one of the most incredible abstractions we've invented."
- Distributed transactions require coordination: ensuring a read/write set across multiple shards commits atomically.
- The standard approach is two-phase commit with two-phase locking, but it is low-performance (blocking for the duration) and high-risk (taking a dependency on another node).
- Cowling's Granola work was about coordinating one-shot / independent transactions efficiently by timestamp exchange rather than locking/blocking.
- Convex uses transactions as its core abstraction: TypeScript functions run as serializable stored procedures.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Concurrency]] — the problem transactions manage
- [[Distributed Systems]] — the context
- [[Two-Phase Commit]] — the standard coordination alternative
- [[Convex]] — transactions as a product primitive
- [[Granola]] — efficient one-shot transaction coordination
