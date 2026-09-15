---
title: "Miguel Castro"
type: entity
tags: [person, distributed-systems, security, Byzantine]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Definition

Miguel Castro was Barbara Liskov's student who worked on Byzantine fault tolerance — protocols that work in the presence of malicious, compromised nodes. (The transcript records Liskov attributing "Paxos" to Castro, but the surrounding discussion of the DARPA Byzantine-attack proposal makes clear this refers to the Byzantine fault-tolerance protocol; Paxos is Lamport's.)

## Key Information

- Got interested via a DARPA request for proposals about Byzantine/malicious attacks on the internet, and asked whether a protocol could be built that works in the presence of Byzantine attacks.
- Viewstamped Replication and Paxos only handled crash faults; Byzantine fault tolerance was the "big step forward" for nodes that purport to work correctly but have been compromised.

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — his advisor
- [[Byzantine Fault Tolerance]] — the protocol he worked on
- [[Viewstamped Replication]] — the crash-only predecessor
- [[Leslie Lamport]] — coined "Byzantine" and authored Paxos
