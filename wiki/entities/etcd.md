---
title: "etcd"
type: entity
tags: [tool, infrastructure, consensus, Kubernetes]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md"]
last_updated: 2026-09-14
---

## Definition

etcd is a raft-based consensus key-value store (originally written by CoreOS) that became the persistence and coordination layer behind Kubernetes.

## Key Information

- Implements the Raft consensus protocol — "provably correct" but "way easier to implement" than Paxos — and provides a replicated, reliable store.
- Kubernetes forced all access through an API server with all persistence in etcd: every component was effectively stateless except the etcd-backed store.
- This design made the system stable but hard to debug, and made etcd the main bottleneck for scaling ("the storage layer that is the bottleneck").

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the system built on etcd
- [[Raft]] — the consensus algorithm etcd implements
- [[Paxos]] — the harder predecessor consensus algorithm
- [[Distributed Systems]] — the problem domain
