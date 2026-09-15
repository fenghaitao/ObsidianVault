---
title: "Raft"
type: concept
tags: [distributed-systems, consensus, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

Raft is a consensus algorithm created to be simpler and more understandable than Paxos.

## Key Information

- The authors sent Leslie Lamport a draft of the original paper; he replied (he recalls) "send it back to me when you have an algorithm" or "…when you have a proof," and they added one.
- In Lamport's view, Raft is essentially Paxos with some of the unfinished details filled in, but described in the opposite order — repeating the second phase until the leader fails, then doing the first phase — which matches how programmers like to think.
- The authors taught Paxos to one class and Raft to another, and students found Raft more understandable.
- A bug was discovered in Raft and fixed; Lamport suspects the version students found "more understandable" was the one with that bug.
- For Lamport, understanding means being able to write a proof of correctness, whereas for most people it means "a warm fuzzy feeling" — which is why Raft's description feels more intuitive.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Paxos]] — the algorithm Raft aims to be more understandable than
- [[Leslie Lamport]] — author of Paxos and critic of Raft's framing
- [[State Machine]] — the abstraction both implement
- [[Distributed Systems]] — the field of consensus
