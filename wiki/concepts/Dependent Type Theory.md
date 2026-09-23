---
title: "Dependent Type Theory"
type: concept
tags: [type-theory, logic, programming-languages, formal-methods]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Dependent type theory is a type theory in which types can depend on values, allowing a type to express a proof obligation — for example, a structure field whose type is "a proof that x > y."

## Key Information

- Chosen for Lean over higher-order logic even though it is "way harder" to implement, because serious mathematicians strongly prefer its expressiveness for abstract objects.
- Example: a structure with integer fields x and y can have a third field whose type is a proof that x > y; that field's type *depends on the values* of the previous fields.
- Embedding proofs into types acts as a built-in invariant: you cannot construct an element of the type without supplying the required evidence — a function taking "a proof that y ≠ 0" cannot be called without that proof.
- Structures can be treated as first-class citizens and transformed (a function that takes a group and returns a new group), which higher-order logic handles only with "encoding tricks" that mathematicians dislike.
- Historically, supplying these proofs by hand was "annoying," but AI now synthesizes them — which de Moura argues makes dependent types practical for the mainstream.
- Lean and Rocq (Coq) are dependently typed proof assistants that are also programming languages, in the functional-programming family (Lean is close to Haskell).

## Related

- [[Lean]] — a dependently typed proof assistant / language
- [[Coq]] — another dependently typed proof assistant (Rocq)
- [[Proof Assistants]] — the category such languages belong to
- [[Interactive Theorem Proving]] — how proofs are written in such systems
- [[Formal Verification]] — the program-reasoning use case
- [[Type System]] — the broader concept
- [[Semantics of Programming Languages]] — closely related to type meanings
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
