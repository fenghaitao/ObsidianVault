---
title: "ErasableSyntax"
type: concept
tags: [typescript, agent-engineering, tooling, type-safety]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Erasable syntax-only TypeScript is a mode where TypeScript type annotations are purely annotations — they are not transpiled and there is a single source of truth between the code and the compiler. This eliminates the confusion AI coding agents experience when navigating between source TypeScript and compiled JavaScript.

## Key Information
- Explored at Earendil as a technique for improving agent-legible codebases
- In standard TypeScript, there is a transpilation step that creates a separation between source and compiled code
- Agents get confused navigating between the two representations when looking for errors
- Erasable syntax means types are annotations only — no transpilation, one source of truth
- This makes agents "much better at finding errors" because there's no ambiguity about where to look
- Part of the broader mechanical enforcement strategy for agent-legible codebases

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[MechanicalEnforcement]] — broader strategy this fits into
- [[AgentLegibleCodebase]] — the design philosophy
- [[NoHiddenMagic]] — complementary principle
- [[Earendil]] — company exploring this technique
