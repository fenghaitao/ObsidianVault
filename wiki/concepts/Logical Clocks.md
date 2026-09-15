---
title: "Logical Clocks"
type: concept
tags: [distributed-systems, concurrency, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

Logical Clocks are Leslie Lamport's mechanism for ordering events in a distributed system through the "happens before" relation, introduced in his paper "Time, Clocks, and the Ordering of Events in a Distributed System," without relying on physical clocks.

## Key Information

- The origin was a paper on distributed databases whose replication executed events in a sequence that could differ from the real order in which they happened.
- Lamport drew on the space-time view of special relativity (Einstein's 1905 paper, plus a 1909 four-dimensional view): one event happens before another if a signal emitted at the first could reach the second before it occurs.
- In a distributed system, event A "happens before" B if information sent in an actual message from A could have affected B.
- He realized an algorithm producing an ordering that satisfies happens-before could synchronize any distributed system described as a state machine — Lamport calls this the paper's practically important idea, which was "completely ignored" (people later claimed the paper said nothing about state machines).
- The paper is his most-cited and, in his view, the first with a scientific result about distributed systems.
- He warns against cramming two ideas into one paper and against over-relying on partial-order reasoning when invariance proofs are the practical method.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — the author
- [[State Machine]] — the ignored second idea in the paper
- [[Paxos]] — later work in the same line
- [[Distributed Systems]] — the field the paper shaped
- [[Abstraction]] — the relativity analogy as an abstraction transfer
