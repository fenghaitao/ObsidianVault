---
title: "State Machine"
type: concept
tags: [distributed-systems, concurrency, abstraction, formalism]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

A state machine is an abstract model — something with a state, and commands (or, even more simply, a next-state relation) that change the state — which Leslie Lamport champions as the fundamental abstraction for describing and building concurrent and distributed systems.

## Key Information

- First appears in Lamport's logical-clocks paper as the way to describe a distributed system; that part of the paper was "completely ignored," to the point people told him the paper never mentioned state machines.
- Paxos and the Byzantine-generals algorithms both implement a fault-tolerant state machine; Butler Lampson connected this to "you can implement anything."
- Lamport now thinks of state machines as effectively "the Turing machine of concurrency" — but notes they lack the Turing machine's ability to describe only what's possible, and that's intentional and useful.
- Mathematical abstraction is a feature: "infinity was introduced to simplify things" — modeling a variable over all integers is simpler than over fixed-width machine integers.
- He rejects language-centered formalisms (e.g., Petri nets): "programmers are hung up on languages"; the semantics of any language would itself be given in terms of a state machine.
- For understanding a program, the key tool is the invariant — a Boolean-valued function of the state that guarantees correctness — and invariance proofs scale better (quadratic in process count) than reasoning over exponentially many execution sequences.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — the champion of this abstraction
- [[Paxos]] — implements a state machine
- [[Logical Clocks]] — the paper that first described systems this way
- [[Byzantine Generals Problem]] — implements a state machine under arbitrary faults
- [[Abstraction]] — the underlying gift
- [[Distributed Systems]] — the field the abstraction organizes
