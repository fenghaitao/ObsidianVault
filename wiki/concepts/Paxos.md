---
title: "Paxos"
type: concept
tags: [distributed-systems, consensus, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-14
---

## Definition

Paxos is Leslie Lamport's algorithm for implementing a fault-tolerant distributed state machine, handling the class of faults where a process simply stops (fail-stop faults).

## Key Information

- Solves the same problem as Lamport's Byzantine-generals work, but for non-malicious, fail-stop faults — the fault class industry actually cared about.
- Has a two-phase structure built around a leader: the first phase (leader election/preparation) is done once per leader, after which only the second phase is repeated until the leader fails; on failure you elect a new leader and redo the first phase.
- Was derived at DEC Systems Research Center when Lamport set out to prove their fault-tolerant storage couldn't work — and realized mid-proof that "this isn't a proof, it's an algorithm."
- Publication lagged eight years (as "The Part-Time Parliament," with a manuscript framing and a preface by Keith Marzullo) because early referees found it unremarkable and Butler Lampson's recognition meant there was no urgency.
- Lamport is puzzled by its reputation for being hard: "I've explained it to some people in five minutes and they understood it."

- Barbara Liskov: Viewstamped Replication and Paxos are essentially the same system, developed independently; the big step forward in both is leader changeover (moving to a new leader when the old one fails).
- Lamport "went around giving all the talks, and she implemented it"; the catchier "Paxos" name is part of why it's better known.
- The Google File System used Viewstamped Replication (which Google's people thought was Paxos).
- James Cowling: Paxos, Raft, Viewstamped Replication, and Virtual Synchrony are "all basically the same thing"; his Viewstamped Replication Revisited paper redefined the protocol that pre-dated Paxos.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — the author
- [[Raft]] — the algorithm designed as a simpler alternative
- [[Byzantine Generals Problem]] — the more general fault model
- [[State Machine]] — what Paxos implements
- [[DEC Systems Research Center]] — where it was developed
- [[Butler Lampson]] — who grasped its importance
- [[Distributed Systems]] — the field of the algorithm
- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — independently developed the equivalent
- [[Viewstamped Replication]] — her equivalent protocol
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
