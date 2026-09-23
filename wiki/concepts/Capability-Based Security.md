---
title: "Capability-Based Security"
type: concept
tags: [concept, security, type-systems, agentic-ai]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Capability-based security gives a program or agent fine-grained, unforgeable permissions (capabilities), which a type system can enforce so that the capability cannot escape its allowed scope.

## Key Information

- The idea is borrowed from operating systems, where capabilities grant very fine-grained permissions to users, programs, and entities; Odersky proposes reusing it for AI agents.
- Goal: remain confident about what an agent will *not* be able to do — e.g., it "will not be able to leak my API keys or my email."
- Scala is "halfway there" with an experimental feature: if a returned value (say a stream) secretly holds onto a file, its type must declare the file as a capability; capabilities cannot be hidden or omitted from a type.
- Two properties to enforce beyond memory safety: agents must not *forget* (drop) capabilities they hold, and must not *forge* capabilities they were never given.
- Memory safety is a prerequisite but insufficient: "without memory safety you have nothing, because you can fake everything."
- Odersky sees AI as well-suited to rewriting legacy C/C++ software toward capability-safe languages once the target is known.

## Related

- [[Scala]]
- [[Martin Odersky]]
- [[Memory Safety]]
- [[Type System]]
- [[Agentic AI]]
- [[Sandboxing]]
