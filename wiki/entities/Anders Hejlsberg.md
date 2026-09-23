---
title: "Anders Hejlsberg"
type: entity
tags: [person, programming-languages, Microsoft]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

Anders Hejlsberg is a programming-language designer best known as the creator of Turbo Pascal, Delphi, C#, and TypeScript, and a Technical Fellow at Microsoft.

## Key Information

- Creator of TypeScript and C#; earlier worked on Turbo Pascal (his first product) and Delphi.
- Started programming on 8-bit micros with Microsoft BASIC in ROM; his first product, Turbo Pascal, was written entirely in Z80 assembly code.
- Led the TypeScript 7 native rewrite: the compiler was ported from JavaScript to Go for a roughly 10x performance gain via native code and shared-memory concurrency.
- The language decision was "pretty structured": first decide to port rather than rewrite (to preserve semantics and backwards compatibility), then score candidates on constraints — garbage collection, first-class functions, native codegen, shared-memory concurrency — and pick the one that checks the most boxes.
- Self-taught; credits Niklaus Wirth's "Algorithms + Data Structures = Programs" for teaching him hash tables (which doubled Turbo Pascal's compile speed) and error recovery.
- Philosophy: "Don't let people tell you it can't be done. When they tell you it can't be done, it's because they can't do it."
- Career lesson: had to learn to stop being a one-man shop and become a team player as products scaled; later "let go" too much on C#, drifting into "architecture astronaut" work before the TypeScript opportunity brought him back to hands-on coding.
- Identifies as a "happy coder" who still writes code and stays involved in a corner of the project rather than only doing design and specs.

### On AI and Software Engineering

- Argues "AI will write 90% of code" is a self-fulfilling claim about output volume — AI already writes 100% of some no-code apps — not about the super-high-quality, never-before-seen code.
- Calls AI "a big stochastic machine that has memorized the entire internet": it extrapolates somewhat but struggles with novel work, which is why it cannot write the TypeScript compiler.
- "Don't hand AI the keys": someone must understand the code and take responsibility — when an app misbehaves, users sue you, not the AI.
- On junior engineers: if AI replaces them, "how do you ever get senior engineers?" The pyramid has narrowed at the bottom, with people advancing faster to supervisory roles; the craft shifts from typing code to reviewing agents' work.
- Still enjoys typing code after 40–50 years and will keep typing the parts he likes, happily delegating tests to AI; finds reviewing harder than writing, and expects AI to make code review more ergonomic.

## Related

- [[TypeScript]] — the language he created and rewrote
- [[C#]] — the language he designed
- [[Turbo Pascal]] — his first product
- [[Microsoft]] — employer
- [[Niklaus Wirth]] — author of an influential book
- [[JavaScript]] — the language TypeScript targets
- [[Go (Programming Language)]] — language chosen for the native rewrite
- [[Rust]] — the rejected alternative
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg]] — source summary
- [[AI and Software Engineering]] — his skepticism toward maximalist AI predictions
- [[Agentic AI]] — agents writing code while humans review
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
