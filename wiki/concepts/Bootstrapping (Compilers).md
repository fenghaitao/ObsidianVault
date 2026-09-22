---
title: "Bootstrapping (Compilers)"
type: concept
tags: [concept, compilers, programming-languages]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Bootstrapping is writing a language's compiler in the language itself, by first building a minimal version in another language and repeatedly writing each next version in the previous one.

## Key Information
- Bjarne started with C, writing a preprocessor for "C with Classes" (classes, simple inheritance, overloading), then a simple compiler in that subset.
- Then he could use operator overloading and classes to build a scope class for lookup/naming — "just writing the next version in the previous version."
- After a couple of years this became what the world knows as C++.
- He notes he didn't invent bootstrapping — he learned it as an undergrad; it "was not an unusual thing."

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — built this way
- [[C (Programming Language)]] — the starting language
