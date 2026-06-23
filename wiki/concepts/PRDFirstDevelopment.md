---
title: "PRDFirstDevelopment"
type: concept
tags: [concept, agentic-engineering, prd, planning, claude-code, technique]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260430 - FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI).md"
last_updated: 2026-06-20
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

### How the PRD is created (the conversation → questions → command flow)

Per `summary-complete-agentic-coding-workflow`, Cole builds the PRD from an *unstructured* brain-dump conversation (often via speech-to-text), spins up research [[SubAgent]]s (web + codebase), then forces the agent to **ask a flood of clarifying questions** (Claude Code's AskUserQuestion multiple-choice tool) to reduce assumptions before `/create-prd` writes the structured doc. The output includes **MVP scope, out-of-scope, directory structure, and phases of work** — and each phase becomes one [[PIVLoop]]. The conversation is throwaway context; only the PRD survives, so everything important must land in it.

### PRD → stories → tickets (and the PM role)

Per `summary-principled-agentic-engineer`, project-level planning is often a **product-manager** touchpoint, not just a developer one. The flow: brain-dump → clarifying questions → `/create-prd` (structured doc) → **review it** → `/create-stories` splits the PRD into individual tickets and pushes them to **Jira via the Atlassian/Jira MCP** (it can even add research as ticket comments and map dependencies between stories). `create-prd` and `create-stories` are kept *separate* so you validate the PRD before generating stories. Then a developer picks a ticket — the **issue is the spec** — and runs the [[PIVLoop]]. Works identically with GitHub issues (gh CLI) or Linear (MCP).

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
- [[PIVLoop]] — each PRD phase is executed as one PIV loop
- [[cole-vs-brian-planning-methodologies]] — synthesis comparing Cole's and Brian's planning approaches
- [[summary-5-techniques-top-agentic-engineers]] — primary source
- [[summary-complete-agentic-coding-workflow]] — the PRD creation flow in practice
- [[summary-principled-agentic-engineer]] — PRD→stories→Jira; the PM planning role
