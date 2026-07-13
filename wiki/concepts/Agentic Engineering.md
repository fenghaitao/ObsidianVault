---
title: "Agentic Engineering"
type: concept
tags: [ai, software-engineering, terminology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s term for the professional discipline of using coding agents (which write, run, debug, and test code themselves) to build production-ready software — distinct from casual "[[Vibe Coding]]," where the user doesn't look at, review, or understand the generated code.

## Key Information

- Coined to preserve a useful distinction: "vibe coding" (per Andrej Karpathy's original definition) means not looking at the code at all — fine for personal prototypes where only the author is harmed by bugs, but irresponsible for code that reaches other users. Once "vibe coding" started being used for all AI-assisted programming including reviewed, production code, Willison felt the term had been devalued, so coined "agentic engineering" for the professional version.
- Considered a genuinely deep discipline in its own right — getting excellent, deployable-to-a-million-users results from coding agents requires real expertise, not just prompting; Willison is writing a chapter-at-a-time book about its patterns.
- Component techniques Willison associates with doing this well: "[[Hoarding Things You Know How To Do]]," "[[Red-Green TDD]]," and the "[[Thin Template Pattern]]" for new projects.
- Distinguished further from the "[[Dark Factory Pattern]]," which goes a step beyond agentic engineering — not just writing code via agents, but not reading the resulting code at all while still maintaining professional quality standards.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — coins and describes this term
- [[Vibe Coding]] — the casual counterpart this term is distinguished from
- [[Andrej Karpathy]] — originated "vibe coding," the term this concept is contrasted with
- [[Dark Factory Pattern]] — the further stage beyond agentic engineering
- [[Hoarding Things You Know How To Do]] / [[Red-Green TDD]] / [[Thin Template Pattern]] — component techniques
