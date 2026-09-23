---
title: "Sandboxing"
type: concept
tags: [concept, security, scripting]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Sandboxing is restricting a script's capabilities to only what the host explicitly exposes, isolating it from the rest of the program or hardware — a capability Roberto Ierusalimschy describes as an exact fit for the word.

## Key Information

- A fresh Lua state has no functions at all; standard libraries (even file and math functions) must be registered explicitly, so the host controls exactly what a script can call.
- Scripts can only call C functions whose pointers the host has registered, giving strict control over what user code can do.
- Example: a Python financial program exposed a Lua command line for end-user scripting because running arbitrary Python would let users break invariants and mutate internal files; Lua let them limit user code to specific operations.
- Hardware example: a fan-speed port that controls CPU temperature should not be reachable directly from C; only Lua (with access-checked values) can call it, preventing an end-user script from setting the fan too low and overheating the CPU.
- This control is a direct consequence of Lua's isolated, framework-free state model.

## Related

- [[Lua]] — the language whose state model enables it
- [[Language as a Library]] — where isolated states come from
- [[Scripting Languages]] — the context where sandboxing is used
- [[Embedding and Extending]] — registering only chosen C functions
- [[Roberto Ierusalimschy]] — who describes it
- [[Python]] — the language that needed Lua for sandboxing
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
