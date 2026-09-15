---
title: "Byzantine Generals Problem"
type: concept
tags: [distributed-systems, fault-tolerance, algorithms]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md"]
last_updated: 2026-09-14
---

## Definition

The Byzantine Generals Problem is the problem of reaching agreement among distributed processes when some may fail arbitrarily — possibly even maliciously — rather than simply stopping.

## Key Information

- Named by Leslie Lamport, who framed it as generals deciding whether to attack or retreat when some may be traitors — a catchy story, learned from Dijkstra's dining philosophers problem and inspired by Jim Gray's "Chinese generals problem."
- Lamport first considered calling them "Albanian generals" (Albania being a "black hole" at the time), then settled on Byzantine because "there aren't any Byzantines around."
- To tolerate one faulty process that can do anything, you need four processes without digital signatures, but only three with digital signatures.
- The general n-process algorithm without digital signatures was Marshall Pease's "work of genius"; Lamport later found an inductive proof for it.
- Motivation: SRI's contract to build a multiprocessor computer system to fly airplanes; with stable-but-awkward control surfaces during the 1970s oil crisis, computers would have to fly planes, and arbitrary faults couldn't be assumed away.
- Lamport's digital-signature-based solution was largely ignored because signatures were expensive then (a Boeing engineer's reaction was simply "we need four computers").

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — co-author and namer
- [[SRI International]] — the contract that motivated it
- [[Paxos]] — the fail-stop counterpart
- [[Edsger Dijkstra]] — whose story-telling approach Lamport emulated
- [[Distributed Systems]] — the field of the problem
