---
title: "summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Core Summary

Anders Hejlsberg, creator of TypeScript and C#, explains why TypeScript's compiler was originally written in JavaScript (self-hosting inside its own ecosystem) and why TypeScript 7 was ported — not rewritten — from JavaScript to Go, a native language with garbage collection and shared-memory concurrency, to achieve a roughly 10x speedup while preserving backwards compatibility. He walks through the structured language decision (Go over Rust because the borrow checker disallows the circular data structures the compiler is full of) and the porting process, including a deterministic TypeScript-to-Go translation tool with only occasional AI help. On AI, he argues incumbent languages will grow stronger because AI is trained on and writes TypeScript/JavaScript/Python, and that AI will not replace software engineers — the craft shifts from typing code to reviewing agents, and someone must always understand and take responsibility for what AI produces. He closes with career lessons from Turbo Pascal, C#, and TypeScript: port rather than rewrite, master language design's long game, and never let people tell you it can't be done.

## Key Points

- TypeScript's compiler was originally written in JavaScript for self-hosting: to live inside its own ecosystem, be daily users of its own tooling, and run everywhere (including the browser, before WebAssembly existed).
- The TypeScript compiler is unusual — it targets JavaScript (a "transpiler"), erases types with zero runtime impact, downlevels newer JS features (e.g., classes into constructor functions), and exists mainly for tooling: statement completion, refactoring, and code navigation — not machine-code generation.
- TypeScript has a gradual type system: half the code can be typed while the rest is `any` (unchecked) — "very few languages have anything like that."
- The TypeScript 7 native rewrite's goal was simple: performance and scalability. JavaScript costs a 2–3x performance penalty and offers no shared-memory concurrency (single-threaded; web workers can only exchange data via remoting/JSON).
- Go was chosen over Rust and Zig: the team *ported* rather than rewrote to preserve semantics and backwards compatibility, and the codebase already assumed garbage collection and first-class functions. Rust lacks GC and its borrow checker disallows the circular data structures (parent pointers, recursive types) the compiler is full of.
- The port used a custom tool that syntactically translated TypeScript into Go (syntactically valid but not compiling), plus manual refactoring and occasional AI. Hejlsberg says AI wasn't good enough two years ago, and a deterministic translation program beats stochastic AI for this work.
- On AI coding: LLMs are not deterministic, so you should ask AI to write *a program* that computes/transforms the answer (a spreadsheet, a translation tool) rather than the answer itself.
- Incumbent languages (JavaScript, TypeScript, Python) flourish under AI because AI is trained on and best at exactly those; TypeScript recently became the #1 most-used language on GitHub (more than JavaScript), with an adoption "knee" coinciding with AI.
- Why TypeScript beat CoffeeScript, Dart, and Flow: fixing JavaScript in place beats replacing it; TypeScript's self-hosting and IDE-centric language service beat Flow (written in OCaml, with little IDE tooling).
- On designing languages: every new language is "only 10% new and 90% the same drudgery"; people overindex on one idea and underindex on mundane machinery; it's a long game (10+ years per language, only good by version three).
- On AI replacing engineers: AI can't write the TypeScript compiler (it's nowhere in its training set); "don't hand AI the keys" because you still carry responsibility; the craft shifts from typing code to reviewing agents, and juniors are still needed to grow into seniors.
- Recommended book: "Algorithms + Data Structures = Programs" by Niklaus Wirth — taught Hejlsberg hash tables and compiler error recovery.
- Career advice: learn to become a team player, and "don't let people tell you it can't be done — when they tell you it can't be done, it's because they can't do it."

## Related

- [[Anders Hejlsberg]] — guest
- [[TypeScript]] — the language and native rewrite discussed
- [[C#]] — the language he designed
- [[Turbo Pascal]] — his first product
- [[Niklaus Wirth]] — the book author he credits
- [[JavaScript]] — the language TypeScript improves
- [[Go (Programming Language)]] — the native-rewrite target
- [[Rust]] — the rejected alternative
- [[Microsoft]] — where these languages were built
- [[Type System]] — gradual typing
- [[Static and Dynamic Typing]] — gradual typing and erased types
- [[Type Inference]] — Flow's approach
- [[Programming Language Design]] — his craft and philosophy
- [[Functional Programming]] — JS's first-class functions and the compiler's functional style
- [[Garbage Collection]] — a deciding constraint for Go
- [[Concurrency]] — shared-memory concurrency motivation
- [[Moore's Law]] — more cores, not faster CPUs
- [[Bootstrapping (Compilers)]] — self-hosting
- [[AI and Software Engineering]] — why AI won't replace SWEs
- [[Porting vs Rewriting]] — the core methodology
- [[Ryan L. Peterman]] — host
