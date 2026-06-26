---
title: "MechanicalEnforcement"
type: concept
tags: [agent-engineering, linting, code-quality, automation]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Mechanical enforcement is the use of automated linting rules and static analysis to catch the types of mistakes AI coding agents commonly make. It is a key technique for building agent-legible codebases, providing guardrails that compensate for the agent's lack of emotional judgment about code quality.

## Key Information
- Developed at Earendil as a practical technique for working with AI coding agents
- Specific enforcement rules used:
  - **No bare catch**: Prevents agents from silently swallowing errors
  - **Single SQL query interface**: All database queries go through one interface so the agent doesn't miss query locations
  - **One primitives component library**: No raw input boxes — consistent styling and behavior
  - **No dynamic imports**: Improves predictability and legibility
  - **Unique function names**: Improves grep-ability and token efficiency — if the agent searches for a function and gets one result, it's much more effective
  - **Erasable syntax-only TypeScript**: Type annotations are not transpiled, eliminating confusion between source and compiled code
- The goal is to "feel the pain that the agent doesn't feel" — mechanical enforcement catches what the agent optimizes away
- These rules create a feedback loop: the agent produces better code because the codebase is more constrained and predictable

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[AgentLegibleCodebase]] — the broader design philosophy
- [[ErasableSyntax]] — specific enforcement technique
- [[NoHiddenMagic]] — complementary principle
- [[HumanCallouts]] — the review counterpart to mechanical enforcement
- [[Earendil]] — company that developed these practices
- [[CristinaPoncelaCubeiro]] — key proponent
