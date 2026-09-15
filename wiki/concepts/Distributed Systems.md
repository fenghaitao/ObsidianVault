---
title: "Distributed Systems"
type: concept
tags: [distributed-systems, computer-science, concurrency]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

Distributed systems are computer systems whose components run on multiple networked computers that coordinate with one another by passing messages.

## Key Information

- The field's roots lie in time-sharing: synchronizing multiple users/processes that share resources (e.g., a printer) required solving the critical-section problem identified by Dijkstra.
- Leslie Lamport's "Time, Clocks, and the Ordering of Events in a Distributed System" supplied the "happens before" definition of event ordering — which he considers the first scientific result about distributed systems.
- A central design method is describing the system as a state machine; fault tolerance then means implementing that state machine (Paxos for fail-stop faults, the Byzantine-generals algorithms for arbitrary faults).
- Industry primarily cares about fail-stop faults (a process simply stops), not Byzantine ones, which is why Paxos became the practical workhorse.
- Digital-signature-based Byzantine solutions were initially ignored because signatures were historically expensive.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — foundational contributor
- [[Paxos]] — the fail-stop consensus algorithm
- [[Raft]] — the more-understandable consensus alternative
- [[Byzantine Generals Problem]] — the arbitrary-fault problem
- [[Logical Clocks]] — event ordering
- [[State Machine]] — the abstraction used to build them
- [[Bakery Algorithm]] — an early synchronization algorithm
