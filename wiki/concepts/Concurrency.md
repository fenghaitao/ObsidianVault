---
title: "Concurrency"
type: concept
tags: [computer-science, distributed-systems, abstractions]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Concurrency is the situation where multiple operations or parties progress simultaneously and may interfere with each other; James Cowling calls managing it "probably the most difficult problem in computer science."
## Key Information
- Transactions are, in Cowling's view, the abstraction that lets engineers manage concurrency.
- In large-scale systems, performance comes from eliminating points of coordination — allowing systems to progress without contention among parties.
- Coordination imposes the cost of reducing parallel throughput to serial throughput across many transactions.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Transactions]] — the abstraction that manages it
- [[Distributed Systems]] — where it becomes hardest
