---
title: "Distributed Systems"
type: concept
tags: [distributed-systems, computer-science, concurrency]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
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

### Kubernetes's Loosely Coupled Design
- Kubernetes is built from "a lot of independent actors" and control loops, loosely coupled for resiliency — a design that is stable but hard to debug.
- All persistence was forced through the etcd-backed API server, making every other component stateless; etcd (a raft-based consensus store) is the scaling bottleneck.
- Burns contrasts state-machine designs (easy to debug, hard to make reliable) with control loops driving current state toward desired state (stable, but hard to trace failures).

### Marc Brooker, Mike Stonebraker, and Barbara Liskov

- Marc Brooker: on-call and postmortem/COE analysis taught him distributed systems in practice; caches introduce metastable failures; Aurora D SQL uses multi-version concurrency control plus commit-time optimistic checks so misbehaving clients can't hold locks.
- Mike Stonebraker: a distributed database beats the "ridiculously inefficient" Hadoop; distributed commit is expensive (extra round trips), which motivated Google's eventual-consistency shortcut — later abandoned when Spanner shipped conventional transactions.
- Barbara Liskov: Argus ran computations as atomic transactions across "guardians"; Viewstamped Replication (leader/view changeover on failure) is essentially the same as Paxos, and Byzantine fault tolerance extends the model to malicious nodes.
- James Cowling: performance in large-scale systems is about eliminating points of coordination, not raw hardware horse-power; his Granola work coordinated one-shot transactions via timestamp exchange, and Magic Pocket's hardest problem was congestion collapse.
- Cowling (S3-migration clip): "systems is all about trade-offs" — e.g., trading the live write path against the long-term read path via a two-tier hot/cold storage design tuned to the organization's own workload.

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the control-loop system
- [[etcd]] — the consensus store
- [[State Machine]] — the contrasted alternative
- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — foundational contributor
- [[Paxos]] — the fail-stop consensus algorithm
- [[Raft]] — the more-understandable consensus alternative
- [[Byzantine Generals Problem]] — the arbitrary-fault problem
- [[Logical Clocks]] — event ordering
- [[State Machine]] — the abstraction used to build them
- [[Bakery Algorithm]] — an early synchronization algorithm
- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — hands-on distributed-systems learning
- [[Metastable Failures]] — the cache failure mode
- [[Multi-Version Concurrency Control]] — the D SQL mechanism
- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — distributed databases vs. Hadoop
- [[Eventual Consistency]] — the rejected model
- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — distributed transactions and replication
- [[Viewstamped Replication]] — the equivalent of Paxos
- [[Byzantine Fault Tolerance]] — the malicious-fault protocol
- [[Tiger Beetle]] — transaction system influenced by VR Revisited
- [[Granola]] — distributed transaction coordination
- [[Transactions]] — the abstraction for coordination
- [[Concurrency]] — the underlying problem
- [[Congestion Collapse]] — a harsh large-scale failure mode
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[Tiered Storage]] — the trade-off design Cowling describes
