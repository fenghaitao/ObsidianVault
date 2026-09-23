---
title: "JavaScript"
type: entity
tags: [programming-language, dynamic-typing, web]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

JavaScript is a dynamic, high-level programming language that Xavier Leroy calls "the ultimate dynamic language," contrasting it with OCaml's static typing and static binding.

## Key Information

- Type checking is entirely dynamic, and nearly everything can be redefined at runtime, including the semantics of method invocation.
- Leroy sees this flexibility as a weakness: it produces fragile programs and security issues (e.g., a method can introspect its own call stack and callers' code).
- Designed by Brendan Eich, a former Lisp person, so JavaScript contains a decent functional core that is "basically Lisp" — but a very dynamic kind of Lisp.
- Leroy is "not a big fan" mostly because of these dynamics, which he finds "easily abused."

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Static and Dynamic Typing]] — the OCaml-vs-JavaScript divide
- [[OCaml]] — its static contrast
- [[Lisp]] — the heritage in JavaScript's functional core
- [[Brendan Eich]] — its designer
