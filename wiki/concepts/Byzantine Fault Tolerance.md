---
title: "Byzantine Fault Tolerance"
type: concept
tags: [distributed-systems, security, consensus, fault-tolerance]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Definition

Byzantine fault tolerance handles nodes that purport to be working correctly but have actually been compromised by malicious attacks — a step beyond the crash-only faults that Viewstamped Replication and Paxos handle.

## Key Information

- Viewstamped Replication and Paxos only handled crashes, and could tell when messages had been tampered with upon arrival (about the extent of their fault model).
- The "big step forward" was protocols that work when nodes have been compromised and lie about their state.
- Leslie Lamport coined the term "Byzantine"; Miguel Castro, Liskov's student, took up a DARPA request for proposals about Byzantine/malicious attacks and asked whether a protocol could work in their presence.

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — co-developer
- [[Miguel Castro]] — her student who worked on it
- [[Viewstamped Replication]] — the crash-only predecessor
- [[Paxos]] — the crash-only equivalent
- [[Leslie Lamport]] — coined "Byzantine"
- [[Byzantine Generals Problem]] — the related framing
- [[Distributed Systems]] — the field
