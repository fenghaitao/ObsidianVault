---
title: "NoHiddenMagic"
type: concept
tags: [agent-engineering, codebase-design, abstractions, transparency]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
"No hidden magic" is a principle of agent-legible codebase design that advocates against abstractions which hide intent from AI coding agents. Examples include ORMs (which hide SQL queries) and React server actions (which hide network behavior). The rule is: if the agent can't see something, it can surely not respect it.

## Key Information
- Proposed by Cristina Poncela Cubeiro as a key principle for agent-legible codebases
- ORMs hide SQL queries from the agent — the agent can't reason about query performance, locking, or data integrity
- React server actions hide the client-server boundary from the agent — it can't reason about what runs where
- The principle extends to any abstraction that obscures the actual behavior of the system from the agent's context window
- Contrasts with traditional software engineering advice that favors abstraction — in the agent era, transparency to the agent is a new design constraint
- Complements mechanical enforcement: make the codebase's behavior explicit so both linting rules and agents can operate on it

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[AgentLegibleCodebase]] — the broader design philosophy
- [[MechanicalEnforcement]] — complementary technique
- [[ErasableSyntax]] — related transparency technique
- [[CristinaPoncelaCubeiro]] — key proponent
