---
title: "Edsger Dijkstra"
type: entity
tags: [person, computer-scientist, concurrency, distributed-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Edsger Dijkstra (transcribed in the episode as "Dystra," "Dysterra," "Dyster," and "Dextrous," and once as "Edkar Dystra") is a Dutch computer scientist and pioneer of concurrent programming, best known here for posing the critical-section problem and for his "EWD" notes.

## Key Information

- In a 1965 paper, formalized the critical-section/mutual-exclusion problem, which Leslie Lamport considers the beginning of the theory of concurrency.
- His original solution had an unsatisfactory property: an individual process could be starved and never get access to the critical section.
- Wrote and circulated short notes ("EWDs," his initials) with new ideas, one of which was a concurrent garbage-collection algorithm that Lamport simplified — earning Lamport authorship.
- Invited Lamport to spend a month in the Netherlands (1976) working with him and colleague Carel Scholten.
- Reportedly found Lamport's simplification "impressive" and said Lamport had "a remarkable ability at abstraction."
- Authored the dining philosophers problem, whose catchy story Lamport later emulated when naming the Byzantine generals problem.

### Barbara Liskov on Dijkstra

- "Go To Statement Considered Harmful" was a letter to the editor of Communications of the ACM, arguing that reasoning about the correctness of code is nontrivial and that gotos can be misused.
- It was controversial because assembly required gotos, languages lacked today's constructs, compilers were less optimizing, and Dijkstra wasn't diplomatic — yet "clearly, Dijkstra won the day."
- In person, Liskov says, Dijkstra was "not always as tactful as he might be," but a very distinguished researcher.

### Leonardo de Moura on Dijkstra
- de Moura opened this episode with Dijkstra's dictum — "program testing can be used to show the presence of bugs, but never to show their absence" — and framed Lean/formal proof as the tool that can show their absence.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — the collaborator who built on his work
- [[Bakery Algorithm]] — Lamport's solution to Dijkstra's problem
- [[Byzantine Generals Problem]] — named with a story inspired by Dijkstra's approach
- [[Distributed Systems]] — the field his concurrency work helped open
- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — recounts the "Go To..." letter
- [[Modularity]] — the correctness concerns it relates to
- [[Formal Verification]] — the field anchored by his "show the absence" dictum
- [[Leonardo de Moura]] — quotes the dictum to frame Lean
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
