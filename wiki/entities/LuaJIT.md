---
title: "LuaJIT"
type: entity
tags: [tool, just-in-time-compiler, Lua]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

LuaJIT is a just-in-time (JIT) compiler for Lua, an independent project by Mike Pall (transcribed "Mike Paul") and unaffiliated with the official Lua project.

## Key Information

- Completely separate from the Lua authors' own project, but Roberto calls it "an incredible piece of software."
- Works so well on top of Lua precisely because Lua is simple and regular — few exceptions, few indirections, and not very dynamic.
- Uses a trace compiler: it detects frequently executed code, records a trace (including function calls) until the loop closes, and compiles that loop inlined and specialized to observed types, with many guards.
- When a guard fails (e.g., a float arrives where an integer was assumed), it must exit back to the interpreter and reconstruct state that had been compressed into registers — including rebuilding a call stack that was never created because calls were inlined.
- Writing a JIT is hard because it is machine-dependent; Mike Pall addressed this with a pseudo-assembler that he translates to the real machine code of different architectures.
- Performs strikingly well on uniform, repetitive benchmarks, which is where trace compilers shine.

## Related

- [[Lua]] — the language it compiles
- [[Mike Pall]] — its author
- [[Roberto Ierusalimschy]] — Lua's creator, who praises it
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
- [[Just-in-Time Compilation]] — the category it belongs to
- [[Trace Compilation]] — its compilation technique
- [[Programming Language Design]] — simplicity that enables it
