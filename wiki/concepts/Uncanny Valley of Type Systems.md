---
title: "Uncanny Valley of Type Systems"
type: concept
tags: [engineering, programming-languages, types]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250725 - Tech Lead for Meta's Most-Used Programming Language (Promotion Story).md"]
last_updated: 2026-09-14
---

## Definition

The "uncanny valley of type systems" (Dwayne Reeves) is the transitional discomfort of a partly-typed codebase: as more types are added, the places where types do not quite behave as a sound static language would feel increasingly off-putting, until the checker is made fully sound.

## Key Information

- Borrowed from computer graphics' uncanny valley, where a near-human-but-subtly-wrong figure feels worse than an obviously fake one
- Engineers used to fully dynamic or fully static languages lack a mental model for a partially-typed system
- The fix is not just more types: you must remove language behaviors incompatible with soundness (e.g., PHP's runtime quirks) rather than paper over them
- Motivated Facebook/Hack's push to eliminate unsound legacy behaviors and reach ~100% strict mode

## Related

- [[summary-20250725 - Tech Lead for Meta's Most-Used Programming Language (Promotion Story)]] — source summary
- [[Dwayne Reeves]] — who coined it
- [[Hack (Meta)]] — the language this applied to
