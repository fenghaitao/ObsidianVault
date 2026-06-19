---
title: "ModularRulesArchitecture"
type: concept
tags: [concept, agentic-engineering, claude-md, context-management, rules, technique]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
last_updated: 2026-06-19
---

## Definition

Modular Rules Architecture is the practice of keeping the global rules file (`CLAUDE.md` / `AGENTS.md`) **short and focused** — only constraints that apply to every task — and pushing task-specific rules into separate reference markdown files that are loaded conditionally. Defends against [[ContextRot]] by avoiding upfront-loading of irrelevant context.

## Key Information

### The structure

```
project/
├── CLAUDE.md                       # < 200 lines, applies to every session
└── .claude/reference/
    ├── api-rules.md                # ~1000 lines, loaded only on API work
    ├── frontend-rules.md           # ~500 lines, loaded only on frontend work
    ├── deployment-rules.md
    └── auth-flow.md
```

The `CLAUDE.md` ends with a **Reference** section listing each task-type's reference file with a one-line trigger condition. The agent reads `CLAUDE.md` at session start, sees the references, and loads the relevant one(s) only when the current task warrants.

### What stays in `CLAUDE.md` (forever-true)

- Tech stack
- Project structure
- Commands to run frontend/backend (`npm run dev`, `pytest`, etc.)
- MCP servers configured
- Universal code conventions
- Logging standards
- Testing strategy at the highest level

If a rule applies to literally every task, it's here. Otherwise it's a candidate for a reference doc.

### What goes in a reference doc (per-task-type)

- Auth flow specifics (loaded only when working on auth)
- API endpoint patterns (loaded only when working on the backend)
- Component conventions (loaded only when working on the frontend)
- Deployment-specific gotchas (loaded only when shipping)
- Database schema patterns (loaded only when touching the data layer)

These can be 500-1000 lines each. They're allowed to be long *because* they're conditionally loaded.

### Why this matters

The naïve alternative — one giant `CLAUDE.md` with every rule — looks tidy but fails:

- Burns thousands of tokens of irrelevant context per session.
- Makes it harder for the agent to attend to what actually matters now.
- Compounds with [[ContextRot]] in long sessions.

Modular rules turn the problem into a tree: load the trunk every time, branches only when needed.

### Implementation in commands too

Reference docs can also be loaded by specific slash commands. E.g. `/build-api-endpoint` might be a command that explicitly references `api-rules.md`. The reference is then implicit in the command rather than the global rules.

### Cole's habit-tracker example

His public template:
- `CLAUDE.md` ~180 lines
- `.claude/reference/api-endpoints.md` ~900 lines
- `.claude/reference/frontend-components.md` ~600 lines
- `.claude/reference/database-patterns.md` ~400 lines

Most sessions only load `CLAUDE.md` + maybe one reference. Rare to load multiple.

## Related

- [[AgenticEngineering]] — technique 2 of 5
- [[ContextRot]] — central failure mode this avoids
- [[ContextEngineering]] — broader discipline
- [[ClaudeCode]] — primary surface
- [[PRDFirstDevelopment]], [[Commandification]], [[ContextReset]], [[SystemEvolution]] — companion techniques
- [[ColeMedin]] — author
- [[summary-5-techniques-top-agentic-engineers]] — primary source
