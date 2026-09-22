---
title: "Dataflow Architecture"
type: concept
tags: [concept, hardware, parallel-computing, functional-programming]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
Dataflow architecture is a hardware/execution model where instructions fire when their input data arrives, rather than under a program counter.

## Key Information
- MIT's dataflow group (led by Arvind) built the Monsoon machine around a token store and matching: when inputs arrive at a node (e.g., both sides of a `+`), the node fires.
- The model aimed to exploit functional languages' natural parallelism by "throwing the whole graph into the token store" and running every runnable node.
- In practice, very fine-grained parallel execution was slow (heavy memory traffic, synchronization costs); the project moved to coarser threads, and it never really caught on.
- Associated with the FPCA (Functional Programming Computer Architecture) conference era.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Arvind]] — led MIT's dataflow group
- [[MIT]] — where the group was based
- [[SKI Combinators]] — the other FP-hardware thread
