---
title: "Abstraction"
type: concept
tags: [thinking, mathematics, engineering, concurrency]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---

## Definition

Abstraction is the ability to separate the essential from the inessential — the gift Leslie Lamport identifies as the real reason for his scientific success.

## Key Information

- Edsger Dijkstra said Lamport had "a remarkable ability at abstraction."
- An algorithm is "something more abstract than a program": a program is written in particular code, while an algorithm can be implemented in any code — concurrency work should be done as an algorithm before code.
- LaTeX embodies it: the idea/logical structure is what matters, not the typesetting.
- "Infinity was introduced to simplify things" — modeling over infinite integers simplifies versus fixed machine integers; mathematical abstraction simplifies rather than complicates.
- "I'm interested in what the language is expressing, not the language" — hence his rejection of language-centered concurrency formalisms.
- Lamport only realized in his last decade how much better he is at abstraction than most people, reframing his own success as a specific gift rather than raw "smartness."

- Barbara Liskov's data abstraction is a specific instance: a module exposes an interface of operations while its implementation and data stay hidden — a new type of module enabling correctness to be reasoned about one module at a time.

- Bjarne Stroustrup's "zero-overhead abstraction": in C++, higher-level abstractions "compile away" and can even be "negative overhead" relative to low-level, hand-written code.
- James Cowling: one of his two lifelong research threads is abstractions — "how to build simple models for complex problems" and how to design APIs; Convex is an attempt to raise the abstraction floor one level up the stack.

## Related

- [[summary-20260223 - Turing Award Winner： Thinking Clearly, Paxos vs Raft, Working With Dijkstra ｜ Leslie Lamport]] — source summary
- [[Leslie Lamport]] — identifies this as his gift
- [[Edsger Dijkstra]] — the person who recognized it
- [[State Machine]] — the abstraction Lamport favors
- [[LaTeX]] — abstraction applied to typesetting
- [[First Principles]] — a related reasoning approach
- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — applied abstraction to module design
- [[Data Abstraction]] — the specific form
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Zero Overhead Abstraction]] — Stroustrup's performance reframing
- [[Simplicity]] — the design goal Cowling ties to abstraction
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
