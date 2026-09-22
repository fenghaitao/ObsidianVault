---
title: "GHC"
type: entity
tags: [compiler, Haskell, tool, GHC]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
GHC (Glasgow Haskell Compiler) is the principal compiler for Haskell, itself written in Haskell and over 35 years old.

## Key Information
- Pipeline: parse → rename → type check → desugar into a small typed intermediate language (Core), run core-to-core optimization passes, then lower to C-- (portable assembly), then to native code or via LLVM.
- Core is a statically typed lambda calculus — essentially System F (Girard's typed lambda calculus) — that has stayed very stable over 35 years; most Haskell innovation lives in the front end.
- Uniquely among production compilers, Core can be re-type-checked; this is used to pinpoint GHC's own bugs (an optimizer producing ill-typed Core would otherwise surface as a distant segfault).
- Supports programmer-sparked parallelism (`E1 \`par\` E2`) rather than automatic fine-grained parallelism.
- Historic anecdote: an old Windows bug made GHC delete a mis-typed file after reporting the error; users were more forgiving back then.
- Now invests heavily in backward compatibility (e.g., a package compiling under GHC 10.0 should compile unchanged under 10.2) — a property GHC historically lacked.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — the language it compiles
- [[Simon Peyton Jones]] — key designer
- [[C--]] — its portable assembly stage
- [[Lambda Calculus]] — its Core is a typed lambda calculus
- [[LLVM]] — an alternative backend
