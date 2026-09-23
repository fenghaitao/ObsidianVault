---
title: "Type Classes"
type: concept
tags: [concept, type-systems, functional-programming, polymorphism]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Type classes are a form of ad-hoc polymorphism in which operations such as equality and hashing are declared at compile time for specific types, rather than being universal methods inherited by every object.

## Key Information

- Martin Odersky wishes Scala had used type classes (as Rust and Haskell do) instead of adapting Java's notion of an object with universal methods like `toString`, `equals`, and `hashCode` defined for everything.
- Type classes are more discriminating: at compile time you state exactly where equality and hash code exist; it is "a bit more tedious to set up" but ultimately safer.
- Java's universal-method approach was very convenient but, in retrospect, "caused friction."

## Related

- [[Scala]]
- [[Type System]]
- [[Parametric Polymorphism]]
- [[Haskell]]
- [[Rust]]
- [[Java]]
- [[Martin Odersky]]
