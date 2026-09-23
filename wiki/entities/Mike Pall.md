---
title: "Mike Pall"
type: entity
tags: [person, compiler, LuaJIT]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Mike Pall (transcribed as "Mike Paul") is the software developer who created LuaJIT, the just-in-time compiler for Lua.

## Key Information

- Roberto Ierusalimschy describes his work as "unbelievable" and says he thinks Pall is still working on LuaJIT.
- Addressed the machine-dependence of a JIT by creating a pseudo-assembler that he then translates into the real machine code of different architectures, unifying several targets.
- Built LuaJIT around a trace compiler that records hot execution paths and compiles them inline.
- Kept LuaJIT a wholly separate project from official Lua.

## Related

- [[LuaJIT]] — the compiler he created
- [[Lua]] — the language it targets
- [[Roberto Ierusalimschy]] — Lua's creator
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
- [[Just-in-Time Compilation]] — the category of his work
- [[Trace Compilation]] — his compilation technique
