---
title: "Monads"
type: concept
tags: [concept, functional-programming, type-systems, Haskell]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
A monad is the structure that lets a pure language sequence effectful computations; in Haskell, do notation combines I/O-performing computations while keeping the language pure.

## Key Information
- Types distinguish pure from effectful values: `Int -> Int` is pure, while `Int -> IO Int` does arbitrary I/O; `IO Int` is a first-class value that performs I/O and returns an Int.
- do notation sequences computations (e.g., `x <- getChar; putChar x`) and produces an `IO` value; these I/O computations can be passed, stored, and reused like any value.
- Purity is signaled through the type system — "the dirty stuff is signaled through the type system."
- Effect systems generalize monads by enumerating specific effects (exceptions, threads, file reads) rather than all-or-nothing I/O; a starting point in Haskell is the Bluefin library (Tom Ellis).
- Monads have "infected" many other languages (F#, Scala, and others), becoming a unifying concept.
- Odersky: pure FP "tries to express as much as possible in pure functions and ... wrap them up in monads or whatnot, and that can get very inconvenient very quickly" — his answer is side effects in moderation.
- He notes Haskell-side libraries are "essentially monadic frameworks" that require expressing a whole program as a monad; he has reservations and wouldn't do that in his Scala programs, but prominent libraries made it feel normative to some teams.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — where do notation lives
- [[Functional Programming]] — the paradigm
- [[Effect Systems]] — the finer-grained generalization
- [[Type System]] — how effects are signaled
- [[Side Effects]] — what monads sequence safely
- [[Martin Odersky]] — moderation over full monadic style
- [[Scala]] — the language where Haskell-style monadic frameworks caused friction
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
