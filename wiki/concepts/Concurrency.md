---
title: "Concurrency"
type: concept
tags: [computer-science, distributed-systems, abstractions]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---
## Definition
Concurrency is the situation where multiple operations or parties progress simultaneously and may interfere with each other; James Cowling calls managing it "probably the most difficult problem in computer science."
## Key Information
- Transactions are, in Cowling's view, the abstraction that lets engineers manage concurrency.
- In large-scale systems, performance comes from eliminating points of coordination — allowing systems to progress without contention among parties.
- Coordination imposes the cost of reducing parallel throughput to serial throughput across many transactions.
### Anders Hejlsberg on shared-memory concurrency
- JavaScript was "engineered to be a single-threaded language" (hence callbacks/async); web workers can't share data except by remoting it (via JSON), so there is no shared-memory concurrency.
- Concurrency with mutable data is very hard (races, deadlocks); functional programming with immutable data is much easier to reason about.
- Moore's law now delivers more CPUs rather than faster ones, so compute-intensive workloads must use shared-memory concurrency or "leave money on the table" — the core motivation for porting the TypeScript compiler to Go.

## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Transactions]] — the abstraction that manages it
- [[Distributed Systems]] — where it becomes hardest
- [[TypeScript]] — native rewrite motivation
- [[Go (Programming Language)]] — shared-memory concurrency target
- [[Anders Hejlsberg]] — on shared-memory concurrency
- [[Moore's Law]] — more cores, not faster CPUs
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
