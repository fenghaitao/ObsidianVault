---
title: "Liskov Substitution Principle"
type: concept
tags: [programming-languages, object-oriented, type-systems, design]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov.md"]
last_updated: 2026-09-14
---

## Definition

The Liskov substitution principle states that a subclass must behave like its superclass when used in an environment where the superclass is expected — a behavioral relationship between types, not an implementation one.

## Key Information

- Origin: Liskov's 1986 OOPSLA keynote, after reading the West Coast Smalltalk-based literature (inheritance, "type hierarchy") and thinking about modules through their specifications rather than their implementations.
- The West Coast papers described a class's behavior by how its implementation differed from its superclass; Liskov saw it "has to do with the behavior," producing the substitution principle.
- Formalized with Jeannette Wing as behavioral subtyping.
- It was named later, in the 1990s, when someone emailed Liskov asking whether their interpretation was correct — she had not coined the name herself.

## Related

- [[summary-20260427 - Turing Award Winner： Data Abstraction, Dijkstra, Distributed Systems ｜ Barbara Liskov]] — source summary
- [[Barbara Liskov]] — the person it's named for
- [[Jeannette Wing]] — co-author of behavioral subtyping
- [[Data Abstraction]] — the East-Coast idea that shaped it
- [[Alan Kay]] — the Smalltalk stream she contrasted
- [[Abstraction]] — the broader idea of meaning over implementation
