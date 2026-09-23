---
title: "Object-Oriented Programming"
type: concept
tags: [concept, programming-paradigm, object-oriented]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
Object-oriented programming organizes code around objects that combine data and behavior, with inheritance and (often) runtime polymorphism.

## Key Information
- Bjarne "never called C++ an object-oriented programming language."
- The first edition of "The C++ Programming Language" used "object-based"; he calls C++ type-oriented / class-oriented.
- C++ supports object orientation well (following Simula's model of types, classes, and class hierarchies), but Bjarne deliberately wanted non-OO constructs too: complex arithmetic written `z = a + b`, with no dots/arrows/inheritance/runtime resolution where unnecessary.
- He wanted to reuse existing code (FORTRAN, C, Simula) rather than force everything into object orientation; mathematics' ~300-year-old notation discouraged making everything object-oriented.
- Odersky built Scala on the idea that FP and OOP can be fused in a real synthesis, not side-by-side; OOP's contribution is components, modules, and encapsulation, where FP historically has no strong story (except ML/OCaml module systems).
- He cites Simon Peyton Jones's "power of the dot": an object followed by `.` immediately lists its methods/fields, focusing the mind — versus FP's "sea of functions" applied to arguments.
- He regrets adapting Java's notion of an object (universal methods `toString`/`equals`/`hashCode`) rather than the more discriminating type classes.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — supports it but is not defined by it
- [[Simula]] — the paradigm's source
- [[Bjarne Stroustrup]] — the designer clarifying the distinction
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Martin Odersky]] — fused FP with OOP in Scala
- [[Scala]] — the FP+OOP synthesis
- [[Type Classes]] — the mechanism he preferred over universal methods
- [[Simon Peyton Jones]] — "the power of the dot"
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
