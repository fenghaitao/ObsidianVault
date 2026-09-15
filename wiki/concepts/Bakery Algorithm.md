---
title: "Bakery Algorithm"
type: concept
tags: [concurrency, algorithms, distributed-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

The Bakery Algorithm is Leslie Lamport's mutual-exclusion algorithm for Dijkstra's critical-section problem, the first with first-come-first-served ordering, and notable for working without requiring atomic shared registers.

## Key Information

- Solves the problem of synchronizing processes so that at most one executes its critical section at a time — the problem Edsger Dijkstra identified in 1965.
- Inspired by a deli counter's ticket system: each customer/process takes a ticket and the lowest-numbered unserved ticket is served next.
- Requires no central control — each process chooses its own ticket.
- Each shared register is written by only one process; even if a reader catches a value mid-write ("absolutely any value"), the algorithm still works — no underlying atomicity assumption needed.
- Lamport wrote a proof of correctness; colleague Anatol Holt found the result so remarkable he insisted "there must be something wrong with it" but never found an error.
- Prior solutions (Dijkstra's, and Don Knuth's) allowed starvation — an individual process could be locked out — which the bakery algorithm's first-come-first-served property fixes.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — the author
- [[Edsger Dijkstra]] — posed the critical-section problem
- [[State Machine]] — Lamport's broader abstraction for concurrency
- [[Abstraction]] — the gift behind his simple formulations
