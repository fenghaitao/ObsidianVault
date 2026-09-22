---
title: "C--"
type: entity
tags: [language, compiler, intermediate-representation]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
C-- (C minus minus) is a portable assembly language / intermediate representation used by GHC between its Core language and native code generation.

## Key Information
- SPJ describes it as "a prototypical imperative language" and "portable assembly code," meant to be platform independent.
- Sits in GHC's pipeline: Core → C-- → (native code backend or LLVM).
- Rationale: avoid duplicating the lambda-calculus-to-machine-code lowering for each CPU; keep the platform-specific part as small as possible.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[GHC]] — the compiler that uses it
- [[Lambda Calculus]] — what gets lowered through it
