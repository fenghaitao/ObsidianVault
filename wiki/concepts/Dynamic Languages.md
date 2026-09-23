---
title: "Dynamic Languages"
type: concept
tags: [concept, programming-languages, dynamic-typing]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

A dynamic language is characterized by the ability to create code at runtime; the hallmark is an `eval` function that executes a piece of code during execution. Dynamic languages form a superset that includes scripting languages but is not the same thing.

## Key Information

- Roberto Ierusalimschy: people often treat "dynamic language" and "scripting language" as synonymous, but they are not — scripting is about coordination, dynamism is about runtime code creation.
- `eval` is almost the definition of a dynamic language: you can create code while running code, so a compiled dynamic language must ship its compiler as a runtime library.
- This is why dynamic languages are more often interpreted than compiled; some compilers simply refuse to support `eval`.
- Lua replaces `eval` with `load`, which compiles a chunk into a function without executing it — a deliberate, library-friendly separation of compile and run.
- At runtime, a dynamic `+` must inspect operand types and decide between addition, concatenation, or another operation, in contrast to typed languages that emit one instruction at compile time.
- Dynamic typing makes it easy to define "falsy" values (nil, zero, empty string/list), but Roberto sees this as a flexibility-vs-protection trade-off.
- Type inference for dynamic languages is generally not computable: attempts either demand a rigid style or infer overly generic types.

## Related

- [[Scripting Languages]] — the subset that coordinates a host
- [[Lua]] — a dynamic language without `eval` (uses `load`)
- [[Python]] — a classic dynamic language
- [[JavaScript]] — dynamic, but not scripting
- [[Static and Dynamic Typing]] — the underlying tension
- [[Type Inference]] — the hard problem for dynamic languages
- [[Roberto Ierusalimschy]] — who draws the distinction
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
