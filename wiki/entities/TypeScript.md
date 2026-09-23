---
title: "TypeScript"
type: entity
tags: [programming-language, tool, Microsoft]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

TypeScript is the programming language whose development Fiona Fung worked on at the end of her Microsoft career.

## Key Information

- Fiona's last Microsoft project was JavaScript and TypeScript
- She stayed at Microsoft longer than she otherwise might have specifically to help ship TypeScript 1.0
- She supported the manager of the TypeScript team as one of her first manager-of-managers reports, describing him as one of the best compiler engineers she has worked with
- James Cowling: Convex is a transactional database whose transactions are written in TypeScript and run as serializable stored procedures.
- Roberto Ierusalimschy: TypeScript-style types "do not guarantee" that values match what was declared, so they cannot be used to compile — a value might not fit the assumed type or register.

### Anders Hejlsberg on TypeScript

- Hejlsberg is the creator; TypeScript began as the internal "Strata" project, first prototyped in C (adapting the JavaScript parser from IE) before moving to a self-hosted JavaScript codebase.
- JavaScript was chosen so the team could self-host inside the ecosystem they served — they were daily users of their own tooling, and JavaScript ran everywhere, including the browser (before WebAssembly existed).
- The compiler targets JavaScript rather than machine code (a "transpiler"): it mostly erases type annotations and downlevels newer syntax (e.g., classes into constructor functions), plus performs type checking — the types have no runtime effect and exist purely for tooling.
- TypeScript uses a gradual type system: part of the code can be typed while the rest is `any`.
- TypeScript 7 (the "native port") reimplemented the compiler in Go for a ~10x speedup, motivated by JavaScript's 2–3x performance penalty and its lack of shared-memory concurrency.
- The port (not a rewrite) was chosen to preserve the compiler's semantics, algorithms, and exact behavior for backwards compatibility; the codebase already assumed garbage collection and first-class functions, which shaped the Go decision.
- TypeScript recently became the #1 most-used language on GitHub — now larger than JavaScript (and Python). Its adoption "knee" coincides with AI: AI tools write TypeScript, not JavaScript, because type annotations guide the model and the compiler can statically validate output.
- Visual Studio Code is ~2.3 million lines of code, and Microsoft has in-house projects over 10 million lines — scale far beyond what was imagined when TypeScript started in 2012.
- The TypeScript compiler is so unlike code the models have seen that Hejlsberg says AI simply cannot write it — his concrete example of AI's limits on genuinely novel, high-quality code.

## Related

- [[summary-20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung]] — source summary
- [[Fiona Fung]] — worked on TypeScript
- [[Microsoft]] — where TypeScript was developed
- [[Visual Studio]] — the environment she earlier worked on
- [[Convex]] — uses TypeScript for its transactional stored procedures
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Anders Hejlsberg]] — creator
- [[JavaScript]] — the language TypeScript targets
- [[Go (Programming Language)]] — the native-rewrite target
- [[Bootstrapping (Compilers)]] — self-hosting compiler
- [[Static and Dynamic Typing]] — gradual type system
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[summary-20260909 - Creator of TypeScript & C#： AI Software Engineering Predictions ｜ Anders Hejlsberg]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
