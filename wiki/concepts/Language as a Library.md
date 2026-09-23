---
title: "Language as a Library"
type: concept
tags: [concept, programming-languages, Lua]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

"Language as a library" is Lua's foundational design stance: the language itself is implemented as a reusable library rather than as a standalone runtime with fixed global state.

## Key Information

- Roberto Ierusalimschy: from the beginning, Lua was thought about and written as a library; its standalone console program is just a client of that library using the same API any other program can use.
- He considers this idea "not very common" and "very particular in Lua."
- A key consequence is the absence of global state: C first creates a new Lua state, all operations run on that state, and states are completely independent of each other.
- Because a state encapsulates everything, C can close a state and release all the memory Lua was using, then create another state later.
- The library stance shapes small and big design details — variable scoping, exception handling (raising in Lua, catching in C), and using `load` instead of `eval` so compilation is a clean, callable step.

## Related

- [[Lua]] — the language that embodies this idea
- [[Embedding and Extending]] — what the library stance enables
- [[Scripting Languages]] — the category it serves
- [[Sandboxing]] — a downstream benefit of isolated states
- [[Roberto Ierusalimschy]] — the designer
- [[Programming Language Design]] — the craft
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
