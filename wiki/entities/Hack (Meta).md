---
title: "Hack (Meta)"
type: entity
tags: [tool, programming-language, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250725 - Tech Lead for Meta's Most-Used Programming Language (Promotion Story).md"]
last_updated: 2026-09-14
---

## Definition

Hack is Meta's gradual, statically-typed evolution of PHP, run on the HHVM runtime; Dwayne Reeves tech-led its adoption across nearly all of Meta's code.

## Key Information

- Facebook evolved PHP in-language (a compiler, then the customized HHVM runtime and the Hack language) rather than rewriting in Java or Python
- Hack offers a "strict mode" (full type annotations) versus a "partial" mode
- By Dwayne's IC7 promotion, nearly all Hack files had moved from ~5-10% strict mode to essentially 100% strict
- Static typing acts as an information/communication tool: it encodes intent, powers autocomplete/search/tooling, and lets the compiler prove certain error classes absent

## Related

- [[summary-20250725 - Tech Lead for Meta's Most-Used Programming Language (Promotion Story)]] — source summary
- [[Dwayne Reeves]] — its tech lead
- [[Meta]] — the company that built it
- [[Uncanny Valley of Type Systems]] — the transitional problem it faced
