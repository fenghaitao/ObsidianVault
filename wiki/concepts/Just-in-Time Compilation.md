---
title: "Just-in-Time Compilation"
type: concept
tags: [concept, compilers, performance]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Just-in-time (JIT) compilation translates code to machine instructions at runtime, typically for frequently executed paths, rather than ahead of time.

## Key Information

- Roberto Ierusalimschy: any kind of compilation can be roughly 10x faster than interpreting (up to 100x depending on workload); 10x is a good working figure.
- Between ahead-of-time and trace compilation there is no clear general winner — it depends on the problem; trace compilers shine on uniform, repetitive loops.
- JITs are machine-dependent and unproductive to write by hand; LuaJIT's Mike Pall used a pseudo-assembler translated per-architecture to reduce that burden.
- A JIT is easier to build well on top of a simple, regular language like Lua (few exceptions and indirections).
- Ahead-of-time compilers for Lua exist too (mostly research), including a student's "ridiculously simple" compiler that expands bytecode opcodes into C and reuses a C compiler for a ~3–5x speedup.
- The compiled-vs-interpreted split is a property of the toolchain, not the language; dynamic languages stay interpreted mainly because of `eval`.

## Related

- [[Trace Compilation]] — a major JIT technique
- [[LuaJIT]] — Lua's JIT
- [[Lua]] — the language it compiles
- [[Mike Pall]] — LuaJIT's author
- [[Programming Language Design]] — simplicity that enables JITs
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
