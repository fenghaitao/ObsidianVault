---
title: "Side Effects"
type: concept
tags: [concept, functional-programming, purity]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
A side effect is an observable interaction with state (I/O, reading the time, mutation); pure functional programming excludes side effects by default.

## Key Information
- Imperative programming has side effects by default; functional programming excludes them by default to make programs easier to write, maintain, and reason about.
- Reading/writing shared (global) variables is a form of invisible coupling between code; functional programming forces such coupling "into the open."
- Purity's inconvenience: even reading the time of day is a side effect that invalidates the same-input-same-output assumption.
- Haskell's escape hatch is `unsafePerformIO` — deliberately spelled "unsafe" so the programmer accepts the obligation.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Functional Programming]] — the paradigm that excludes them
- [[Monads]] — how Haskell sequences them safely
- [[Haskell]] — the pure language
