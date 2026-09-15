---
title: "SRI International"
type: entity
tags: [organization, research, computing]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

SRI International (transcribed in the episode as "SRRI") is a research institute whose team was contracted to build a multiprocessor computer system for flying airplanes, motivating the work on the Byzantine generals problem.

## Key Information

- When Lamport joined, the SRI team was working on the same distributed-agreement problem he had solved using digital signatures.
- They appreciated the need for tolerating processes that can "do malicious things" because a flight-control computer really couldn't assume failures would be benign.
- Their framing — an algorithm for agreement on a single command, run repeatedly — was a "nicer abstraction" than Lamport's sequence-of-commands method.
- The resulting paper included both their signature-free algorithm and Lamport's signature-based one; Marshall Pease produced the brilliant general (n-process) algorithm.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Byzantine Generals Problem]] — the result of that contract
- [[Leslie Lamport]] — co-author of the paper
- [[Distributed Systems]] — the field of the work
