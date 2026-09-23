---
title: "Zero-Based Indexing"
type: concept
tags: [concept, programming-languages, indexing]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Zero-based indexing counts the first element of a sequence as index 0; one-based indexing (chosen by Lua) counts it as index 1.

## Key Information

- Roberto Ierusalimschy: everything in the real world is one-indexed — book chapters, mathematical sequences (`A1, A2, ...`), and matrix elements (`A11, A12, ...`); only programmers use zero.
- Historically, many languages were one-based or flexible: Fortran indexed from 1, and Pascal let you declare array bounds from any value to any value (e.g., -5 to 5).
- Zero-based indexing spread because of C, but C has no real indexing — indexing is pointer arithmetic (an offset from an address), so the first element is naturally at offset 0.
- Languages without pointer arithmetic still copied C's zero-based convention, keeping the surface syntax without the underlying reason.
- Lua chose one-based indexing to be friendlier to end users and non-programmers, who intuitively number the first element 1, not 0.
- Zero has small advantages for some operations (e.g., circular buffers), but Roberto considers the confusion far more costly.
- Off-by-one bugs he attributes to insufficient testing — a simple test on any array or list would catch a zero-vs-one mistake immediately.

## Related

- [[Lua]] — the one-based language
- [[C (Programming Language)]] — the zero-based source of the convention
- [[SNOBOL]] — old languages worth studying for divergent ideas
- [[Programming Language Design]] — indexing as a design choice
- [[Roberto Ierusalimschy]] — who defends one-based indexing
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
- [[summary-20260904 - Creator of Lua： Top 3 Languages Every Engineer Should Learn in 2026 ｜ Roberto Ierusalimschy]] — source summary
