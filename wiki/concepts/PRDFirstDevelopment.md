---
title: "PRDFirstDevelopment"
type: concept
tags: [concept, agentic-engineering, prd, planning, claude-code, technique]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
last_updated: 2026-06-19
---

## Definition

PRD-First Development is [[ColeMedin]]'s practice of writing a **Product Requirements Document** (a single markdown file capturing project scope) *before* any feature work, then using it as the persistent north star for every coding session. Distinguishes from [[Rasmus]]'s [[PRPFramework]]: PRDs are project-level scope; PRPs are per-feature implementation prompts. **PRDs spawn PRPs.**

## Key Information

### What goes in a PRD

For greenfield projects:
- Target users
- Mission / problem statement
- In scope / out of scope (the latter is usually more important)
- Architecture overview
- Feature list (high-level — granular features generate PRPs)

For brownfield projects:
- Documentation of what exists
- What's coming next + why

### How it's used in practice

[[ColeMedin]]'s daily pattern:

```
1. /prime                                    ← loads codebase + PRD as context
2. "Based on the PRD, what should we build next?"   ← agent picks priority
3. (planning conversation)
4. /create-plan                              ← generates structured-plan markdown
5. /clear                                    ← context reset
6. /execute-plan plans/feature-XYZ.md        ← agent builds with clean context
```

The PRD is the through-line. Every plan derives from it; every feature ladders into it.

### Why it works

- **One source of truth** — no scope drift across sessions.
- **Consistent prioritization** — when the agent picks "what's next," it's against a fixed scope.
- **Onboarding artifact** — a new engineer (human or AI) can read the PRD and orient.
- **Self-correcting scope** — if you find yourself building something not in the PRD, that's a flag to either update the PRD or stop.

### Slash command

Cole's `/create-prd` command in `.claude/commands/`: kicks off after a planning conversation, asks targeted questions about target users, scope, mission, architecture, then writes a structured PRD to a path the user specifies. Template-driven (the command markdown contains the section list).

### Relationship to PRPs

| Layer | What it specs | Cardinality | Source |
|---|---|---|---|
| **PRD** | Project scope and architecture | One per project | [[PRDFirstDevelopment]] |
| **PRP** | Implementation plan for one feature | Many per project (one per feature) | [[PRPFramework]] |

A typical project has one PRD that survives the project's lifetime, and dozens of PRPs that are generated, executed, and discarded.

## Related

- [[AgenticEngineering]] — technique 1 of 5
- [[PRPFramework]] — feature-level companion ([[Rasmus]]'s framework)
- [[ContextEngineering]] — broader discipline
- [[ClaudeCode]] — primary surface
- [[ModularRulesArchitecture]], [[Commandification]], [[ContextReset]], [[SystemEvolution]] — companion techniques
- [[ColeMedin]] — author
- [[summary-5-techniques-top-agentic-engineers]] — primary source
