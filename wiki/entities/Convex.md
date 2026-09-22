---
title: "Convex"
type: entity
tags: [company, backend, database, TypeScript, agentic-development]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Convex is a backend application platform co-founded by James Cowling (CTO) and Jamie Turner. It is a transactional database whose transactions are written in TypeScript and run as serializable stored procedures, with automatic reactivity so clients see a consistent view of server state.
## Key Information
- Founded pre-agentic era, from Cowling's belief that a project's real differentiator is the quality of its abstractions/design/architecture, and that distributed state management is the hardest challenge in engineering.
- Primitives include queries, mutations, actions, and subscriptions flowing over web sockets to a custom distributed database.
- Designed to "make problems go away" — developers don't reason about state management, concurrency, scheduling, transactions, polling, data sync, or type safety.
- Positioned as a higher-level abstraction above AWS or hosted Postgres, sold as obvious-in-retrospect ("everyone thought we were idiots" before).
- Agentic development has been a tailwind: coding agents are bad at large codebases, action-at-a-distance, and long-lived simple architectures — the very gaps Convex fills as a backend abstraction.
- Currently developing lower-level operating-system-like primitives (background singletons, fork) for high-performance background workloads such as scheduling and aggregates.
- Example: a voting tally can be maintained by a background singleton that sleeps on a condition variable until new votes arrive, rather than doing a full table scan per query.
- Cowling finds designing Convex's new APIs genuinely hard and exciting: "I still find Convex very hard... I struggle every day."
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[James Cowling]] — co-founder and CTO
- [[Jamie Turner]] — co-founder
- [[Dropbox]] — where Cowling worked before founding Convex
- [[TypeScript]] — language of its transactions
- [[Transactions]] — its core abstraction
- [[Simplicity]] — its design philosophy
