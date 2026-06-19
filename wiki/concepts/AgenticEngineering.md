---
title: "AgenticEngineering"
type: concept
tags: [concept, discipline, ai-coding, claude-code, methodology]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
last_updated: 2026-06-19
---

## Definition

Agentic Engineering is [[ColeMedin]]'s umbrella term for the discipline of working effectively with AI coding agents — particularly [[ClaudeCode]] in long-running, autonomous configurations. It's the practitioner-level superset of [[ContextEngineering]], adding the workflow, rules, command, and self-improvement disciplines that distinguish "people who use AI to code" from "people who get production results from AI coding agents."

## Key Information

### The 5 techniques (per `summary-5-techniques-top-agentic-engineers`)

Cole's checklist of what separates top agentic engineers:

1. **[[PRDFirstDevelopment]]** — North-star markdown doc capturing project scope; everything else flows from it.
2. **[[ModularRulesArchitecture]]** — Lightweight global rules with per-task-type reference docs loaded conditionally.
3. **[[Commandification]]** — If you've prompted it twice, package it as a slash command.
4. **[[ContextReset]]** — `/clear` between planning and execution to keep context lean for the actual work.
5. **[[SystemEvolution]]** — Fix the system, not the bug. Compounds over time.

These aren't tools — they're disciplines around using existing tools.

### How Agentic Engineering relates to other concepts

```
       VibeCoding (no discipline)
            ↓
    PromptEngineering (single-call discipline)
            ↓
    ContextEngineering (single-session discipline)
            ↓
   AgenticEngineering (multi-session, workflow-level discipline)
            ↓
    AgentHarness (multi-session orchestration infrastructure)
```

Each layer subsumes and extends the prior. AgenticEngineering is the human-discipline layer; [[AgentHarness]] is the system-architecture layer. They're complementary — agentic engineers build harnesses, harnesses encode agentic engineering practices.

### The "no new tools needed" claim

A key feature of [[ColeMedin]]'s framing: every technique runs on **markdown files** in a project. PRDs are markdown. Rules are markdown. Commands are markdown. Reference docs are markdown. The substrate is the filesystem; the tools are whatever AI coding assistant you have.

This makes the discipline portable across [[ClaudeCode]], [[Cursor]], [[Windsurf]], Kiro AI, and others — the markdown artifacts come with you.

### Markers of an agentic-engineered project

What you'd see if you cloned the repo of someone practicing this:

```
project/
├── CLAUDE.md                       # short, focused global rules
├── PRD.md                          # north-star scope doc
├── .claude/
│   ├── commands/                   # slash command definitions
│   │   ├── prime.md
│   │   ├── create-prd.md
│   │   ├── plan-feature.md
│   │   ├── execute-plan.md
│   │   ├── review.md
│   │   └── system-evolution.md
│   └── reference/                  # per-task-type rules, loaded conditionally
│       ├── api-rules.md
│       ├── frontend-rules.md
│       ├── deployment-rules.md
│       └── auth-flow.md
├── plans/                          # generated structured plans
│   └── feature-XYZ.md
└── examples/                       # code patterns the agent matches against
    └── example-pydantic-agent.py
```

Compare to a vibe-coded project: nothing here, just `git init` and a series of prompts.

### The mental model shift

Agentic Engineering asks practitioners to think like a system designer, not a prompter. The questions change:

| Vibe coding question | Agentic engineering question |
|---|---|
| "What prompt should I write?" | "What rule should govern this class of work?" |
| "How do I get the AI to do X?" | "How does my workflow ensure X is always done?" |
| "Why did this fail?" | "What in my system allowed this failure?" |
| "What new tool should I try?" | "Which capability am I missing that any tool would solve?" |

### Connection to [[CapabilitiesOverTools]]

These are the same idea at different scales. CapabilitiesOverTools says: focus on transferable skills. Agentic Engineering says: capture those skills as **explicit, file-based artifacts** so they compound and transfer.

A skill in your head is fragile. A workflow committed to `.claude/commands/` is durable, shareable, and self-improving via [[SystemEvolution]].

## Related

- [[ContextEngineering]] — single-session predecessor
- [[AgentHarness]] — multi-session companion
- [[PRDFirstDevelopment]], [[ModularRulesArchitecture]], [[Commandification]], [[ContextReset]], [[SystemEvolution]] — the five techniques
- [[ClaudeCode]] — primary execution surface
- [[CapabilitiesOverTools]] — companion principle
- [[ColeMedin]] — articulator
- [[summary-5-techniques-top-agentic-engineers]] — primary source
