---
title: "Parametric Polymorphism"
type: concept
tags: [concept, type-systems, polymorphism]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md"]
last_updated: 2026-09-22
---
## Definition
Parametric polymorphism lets one piece of code work uniformly for all types (e.g., `forall A. [A] -> [A]`), in contrast to subtype polymorphism.

## Key Information
- Example: `reverse` should have type `forall A. list of A -> list of A`, so it works on both lists of integers and lists of characters while preserving the element type.
- Born in ML — the first parametrically polymorphic functional language (Robin Milner).
- Java generics and object-oriented programming more generally are "exactly the same idea" migrated into the mainstream.
- Contrasts with subtype (object-oriented) polymorphism, where code written for a supertype (vehicle) works on subtypes (car, Ford); the two interact in complex ways when combined with generics and side effects.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[ML (Programming Language)]] — where it was born
- [[Robin Milner]] — the ML creator
- [[Type System]] — the feature's home
- [[Object-Oriented Programming]] — the contrasting subtype polymorphism
