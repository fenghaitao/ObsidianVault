---
title: "Parametric Polymorphism"
type: concept
tags: [concept, type-systems, polymorphism]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---
## Definition
Parametric polymorphism lets one piece of code work uniformly for all types (e.g., `forall A. [A] -> [A]`), in contrast to subtype polymorphism.

## Key Information
- Example: `reverse` should have type `forall A. list of A -> list of A`, so it works on both lists of integers and lists of characters while preserving the element type.
- Born in ML — the first parametrically polymorphic functional language (Robin Milner).
- Java generics and object-oriented programming more generally are "exactly the same idea" migrated into the mainstream.
- Contrasts with subtype (object-oriented) polymorphism, where code written for a supertype (vehicle) works on subtypes (car, Ford); the two interact in complex ways when combined with generics and side effects.
- Xavier Leroy: polymorphism is "discovered just by running type inference" — under-constrained types have no constraints, so they generalize to "any type," Robin Milner's beautiful insight from the 1970s.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[ML (Programming Language)]] — where it was born
- [[Robin Milner]] — the ML creator
- [[Type System]] — the feature's home
- [[Object-Oriented Programming]] — the contrasting subtype polymorphism
- [[Type Inference]] — how polymorphism emerges for free
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
