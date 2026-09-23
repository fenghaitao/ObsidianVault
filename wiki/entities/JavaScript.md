---
title: "JavaScript"
type: entity
tags: [programming-language, dynamic-typing, web]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

JavaScript is a dynamic, high-level programming language that Xavier Leroy calls "the ultimate dynamic language," contrasting it with OCaml's static typing and static binding.

## Key Information

- Type checking is entirely dynamic, and nearly everything can be redefined at runtime, including the semantics of method invocation.
- Leroy sees this flexibility as a weakness: it produces fragile programs and security issues (e.g., a method can introspect its own call stack and callers' code).
- Designed by Brendan Eich, a former Lisp person, so JavaScript contains a decent functional core that is "basically Lisp" — but a very dynamic kind of Lisp.
- Leroy is "not a big fan" mostly because of these dynamics, which he finds "easily abused."
- Roberto Ierusalimschy jokes JavaScript is even more complex than C++, and that "JavaScript: The Good Parts" is a very thin book compared to official JavaScript books; its value is that it discusses the bad parts and explains why they exist.
- He classifies JavaScript as a dynamic language, not a scripting language — scripting means coordinating a host program, while JavaScript's dynamism comes from runtime code creation.
- On truthiness, Roberto considers JavaScript "even worse" than Python's truthy/falsy coercion for implicit behavior.

### Anders Hejlsberg on JavaScript

- Hejlsberg defends JavaScript: in the ~3–4 weeks Brendan Eich had to create it in the mid-90s he "did a lot of things right" — especially first-class functions (functions within functions, closures, passing functions as values).
- Its quirks (automatic conversions, `==` vs `===` differences) are exactly what a type checker is good at tracking; with TypeScript, "we've managed to sort of capture all the badness and park it."
- JavaScript's edge over Java: it truly runs everywhere, including the browser.
- Why replacement attempts failed: CoffeeScript was only a different syntax (no new semantics or tooling), while Dart tried to fix/replace JavaScript; fixing a language in place serves the ecosystem far better.
- JavaScript was engineered single-threaded — hence callbacks/async rather than threads — and that lack of shared-memory concurrency is why the native TypeScript rewrite left it for Go.
- JavaScript costs a 2–3x performance penalty versus native code and was never optimized for compute-intensive workloads like compilers (built for browser UI, originally maybe ~100 lines); its web workers can share data only by remoting/serializing it (JSON).

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Static and Dynamic Typing]] — the OCaml-vs-JavaScript divide
- [[OCaml]] — its static contrast
- [[Lisp]] — the heritage in JavaScript's functional core
- [[Brendan Eich]] — its designer
- [[Anders Hejlsberg]] — defends JS and builds TypeScript on it
- [[TypeScript]] — the typed superset he created
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
