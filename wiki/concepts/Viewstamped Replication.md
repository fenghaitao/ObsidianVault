---
title: "Viewstamped Replication"
type: concept
tags: [distributed-systems, replication, consensus, storage]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-14
---

## Definition

Viewstamped Replication is a replication/consensus protocol developed by Barbara Liskov and Brian Oki, using incrementing "views" to track leader changeover after failures; it is essentially the same system as Leslie Lamport's Paxos and, in Liskov's telling, the beginning of cloud storage.

## Key Information

- Solves replicated storage with correct behavior and continued availability as long as enough nodes are up and the network works; originated from thinking about a file system.
- "Viewstamps" let the system notice node failures and determine which replicas have the most recent state, so a new leader can take over without losing anything — done with incrementing numbers ("view 25, next view 26"), not clocks.
- Liskov borrowed the idea of transactions from the database field; her Argus work on distributed atomic transactions led into it.
- Lamport developed Paxos independently; he "went around giving all the talks," while Liskov "implemented it" — and Paxos's catchier name and marketing account for its greater fame.
- Handled only crash faults; the first real use Liskov noticed was the Google File System (which thought it was Paxos).
- James Cowling wrote "Viewstamped Replication Revisited," redefining the protocol; the work proved influential to "a few really great companies like Tiger Beetle."

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — co-developer
- [[Brian Oki]] — her student and co-developer
- [[Paxos]] — the equivalent protocol
- [[Leslie Lamport]] — developed Paxos independently
- [[Byzantine Fault Tolerance]] — the later extension
- [[Google]] — where it was first used in a real system
- [[Distributed Systems]] — the field
- [[James Cowling]] — wrote VR Revisited
- [[Tiger Beetle]] — a company influenced by VR Revisited
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
