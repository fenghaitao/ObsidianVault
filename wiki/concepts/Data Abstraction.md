---
title: "Data Abstraction"
type: concept
tags: [programming-languages, abstraction, software-design, modularity]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Definition

Data abstraction is the idea that a software module provides an interface of operations while its implementation and the data it uses stay hidden; Barbara Liskov invented it as an answer to the 1970s software crisis and realized it in the CLU language.

## Key Information

- Before it, the only modularity mechanism in programming languages was the procedure, which doesn't match modules like a file system or database.
- Liskov's Mitre notion was "a bunch of code providing you with an access through operations," with the inside and its data inaccessible; she then saw it as a data abstraction (a set, a sequence, etc.) — a new type of module.
- She wrote an impactful paper with Steve Zilles sketching abstract data types; CLU came next, and the idea reached industry through Ada and, in the 1990s, Java.
- Rationale for encapsulation: when many programmers build big programs, "your team is really only as strong as your weakest programmer," so the compiler should make bad behavior impossible (Python, e.g., lets outside code muck with a module's internals).

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — the inventor
- [[Abstraction]] — the broader concept
- [[Modularity]] — what data abstraction enables
- [[Liskov Substitution Principle]] — the related formal principle
- [[Steve Zilles]] — co-author of the paper
- [[Java]] — a language that popularized it
