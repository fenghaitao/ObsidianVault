---
title: "Trace Compilation"
type: concept
tags: [concept, compilers, just-in-time]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Trace compilation is a just-in-time technique that records a frequently executed path (a "trace"), inlining called functions, and compiles that specific loop specialized to the observed types instead of compiling whole functions.

## Key Information

- Roberto Ierusalimschy: it detects code executed frequently, starts a trace recording everything the code does (including function calls) until the loop closes, then compiles that loop inlined and specialized.
- It specializes to observed runtime types — e.g., if a number happened to be an integer, it compiles for integers and emits guards to check that assumptions still hold.
- When a guard fails (e.g., a float arrives after repeated integers), execution must return to the interpreter.
- The hard part of that fallback: translating state compressed into registers and recreating a call stack that was never built because calls were inlined — a source of significant complexity.
- Trace compilers perform best on uniform, repetitive workloads such as benchmarks.

## Related

- [[Just-in-Time Compilation]] — the parent technique
- [[LuaJIT]] — the trace compiler described
- [[Mike Pall]] — its author
- [[Lua]] — the language it targets
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
