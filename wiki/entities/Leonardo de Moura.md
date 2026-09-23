---
title: "Leonardo de Moura"
type: entity
tags: [person, computer-scientist, automated-reasoning, proof-assistant]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Leonardo de Moura is a computer scientist in automated reasoning, best known as the creator of the Z3 SMT solver and the Lean proof assistant / programming language.

## Key Information

- Created Lean (a dependently typed functional programming language and interactive theorem prover) and, earlier, the Z3 SMT solver during his time at Microsoft Research.
- Built Z3 for software test-case generation and verification; Z3 is fully automatic ("push button"), strong at finding bugs but "never super successful" at proving the absence of bugs — so Lean was born to fill that gap.
- Chose dependent type theory over higher-order logic for Lean after Jeremy Avigad convinced him that higher-order logic would never attract fields-medal-level mathematicians; dependent types are harder to implement but far more expressive for abstract math.
- Co-built Lean with Sebastian Ullrich; the C++ → Lean self-host was "extremely painful" — he said he "literally wanted to cry" when Lean first compiled itself, describing the required bare-bones proofs as "almost like programming in assembly."
- Co-founded the Lean nonprofit (established 2023) with Sebastian Ullrich; Lean is 13 years old, the first 10 spent as a research project.
- Now at AWS/Amazon (he references "a colleague of mine here at Amazon"); AWS has used formal verification for a decade, has a ~half-million-line Lean compiler for AI accelerators, and made the largest donation to date to the Lean nonprofit.
- His background is automated reasoning, not programming-language design; he considers Lean an order of magnitude harder than Z3 partly because of its human interface and diverse user community (math people first, then programmers).
- Views AI as the unlock that makes formal verification mainstream: it drafts and maintains proofs; he now writes properties (not tests) and has AI prove most of them for him.
- Self-described introvert; his one piece of retrospective advice to himself is to develop "people skills," which were essential to growing a community and hard for him to learn.

## Related

- [[Lean]] — the proof assistant / language he created
- [[Z3]] — the SMT solver he created earlier
- [[mathlib]] — Lean's mathematical library
- [[Sebastian Ullrich]] — co-creator and co-founder
- [[Dependent Type Theory]] — the design choice behind Lean
- [[Formal Verification]] — the field he aims to mainstream
- [[Proof Assistants]] — the category Lean belongs to
- [[Microsoft]] — where he started Z3
- [[AWS]] — his current employer and Lean's largest donor
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
