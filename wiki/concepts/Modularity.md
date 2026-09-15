---
title: "Modularity"
type: concept
tags: [software-design, programming-languages, correctness, encapsulation]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Definition

Modularity is decomposing a program into small pieces, each with an interface that completely describes the service it provides and a hidden implementation, so correctness can be reasoned about one module at a time.

## Key Information

- The 1970s software crisis: companies spent millions of dollars and hundreds of man-years on big programs that had to be thrown away because no one knew how to build modular systems.
- People proposed modularity but couldn't define a module ("just a chunk of code"); data abstraction supplied the missing notion of a module that matches things like file systems and databases.
- Encapsulation is crucial: making a module's internals inaccessible lets the compiler enforce rules, because "your team is really only as strong as your weakest programmer."
- Dijkstra's "Go To Statement Considered Harmful" argued that reasoning about the correctness of code is genuinely hard — part of the same push toward principled, modular program construction.

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — the contributor
- [[Data Abstraction]] — the concept that enabled it
- [[Abstraction]] — the related reasoning skill
- [[Edsger Dijkstra]] — championed reasoning about correctness
- [[John Guttag]] — taught a class centered on it
