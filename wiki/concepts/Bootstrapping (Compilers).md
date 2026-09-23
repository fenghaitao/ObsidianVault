---
title: "Bootstrapping (Compilers)"
type: concept
tags: [concept, compilers, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---
## Definition
Bootstrapping is writing a language's compiler in the language itself, by first building a minimal version in another language and repeatedly writing each next version in the previous one.

## Key Information
- Bjarne started with C, writing a preprocessor for "C with Classes" (classes, simple inheritance, overloading), then a simple compiler in that subset.
- Then he could use operator overloading and classes to build a scope class for lookup/naming — "just writing the next version in the previous version."
- After a couple of years this became what the world knows as C++.
- He notes he didn't invent bootstrapping — he learned it as an undergrad; it "was not an unusual thing."

### Anders Hejlsberg on self-hosting
- Hejlsberg on why TypeScript self-hosts: "if you can self-host in the ecosystem that you want to be a part of, that is dramatically better" — the team were daily users of their own tooling, so bugs and performance issues were felt immediately.
- Self-hosting also made it far easier for the community to contribute, in contrast to Flow, which was written in OCaml and required learning a different language.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — built this way
- [[C (Programming Language)]] — the starting language
- [[TypeScript]] — a self-hosting compiler
- [[Anders Hejlsberg]] — on self-hosting TypeScript
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
