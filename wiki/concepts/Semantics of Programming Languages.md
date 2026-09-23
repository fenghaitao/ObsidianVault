---
title: "Semantics of Programming Languages"
type: concept
tags: [programming-languages, formal-methods, theory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

Semantics of programming languages is the field that assigns mathematical meaning to programs (what plus, assignment, and other constructs mean), providing the bridge between programs and mathematics needed for formal reasoning.

## Key Information

- A program prover propagates invariants line by line, but a prover like Lean needs to be taught the language's semantics: mathematics has no assignment (there, `x = x + 1` is just false), so programs need explicit account of successive variable states.
- The bridge between programs and their mathematical meaning is called semantics — a big topic in PL research since at least the 1960s.
- Pure functional languages have a much smaller gap between program and mathematics than imperative ones (making formal reasoning easier); residual gaps include non-termination and floating-point arithmetic versus real numbers.
- Xavier Leroy wrote CompCert in a purely functional style precisely to make it easier to reason about, and defining the semantics of C and assembly was necessary to state "the compiler preserves semantics."

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Formal Verification]] — the reasoning it enables
- [[Proof Assistants]] — the tools that must be taught semantics
- [[CompCert]] — whose correctness is stated in semantic terms
- [[Programming Language Design]] — the craft semantics belongs to
