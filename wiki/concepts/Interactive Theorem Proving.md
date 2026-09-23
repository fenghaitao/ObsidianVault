---
title: "Interactive Theorem Proving"
type: concept
tags: [formal-methods, theorem-proving, logic, tools]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Interactive theorem proving is the practice of writing a proof in an assistant where the human (or AI) guides step-by-step transformations and the machine checks each step, in contrast to fully automatic provers.

## Key Information

- Lean's "tactic mode" is a domain-specific language for proofs: each step ("simplify my goal," "apply this rewriting step") transforms the proof state shown in the Info View until "no goals left" means the proof is complete.
- The live proof state gives constant feedback; de Moura reports users describe the process as a game ("You built my favorite computer game").
- Contrasts with automatic SMT solving (Z3), which is a single opaque "solve" step the user cannot influence; interactivity lets you break a proof into small, individually justifiable steps.
- Proof checking in Lean is type checking: the kernel verifies that the type of a proof term matches the theorem's claimed type.
- AI plays this same "game" via reinforcement learning (analogous to Go), driving the proof state toward "no goals left" — the mechanism behind IMO-verifying math systems.

## Related

- [[Proof Assistants]] — the tools used
- [[Dependent Type Theory]] — the underlying logic (proofs as typed terms)
- [[Lean]] — a leading interactive prover
- [[Coq]] — another interactive prover
- [[Formal Verification]] — the program-reasoning use case
- [[Z3]] — the automatic contrast
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
