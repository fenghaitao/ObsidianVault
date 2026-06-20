---
title: "PRPFramework"
type: concept
tags: [concept, framework, prp, context-engineering, claude-code, rasmus]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"
last_updated: 2026-06-20
---

## Definition

The PRP Framework is [[Rasmus]]'s structured methodology for [[ContextEngineering]] in [[AICodingAssistant]] workflows. **PRP** = Product Requirements Prompt. Where a PRD (Product Requirements Document) is a spec written for human developers, a PRP is a spec written *for an AI* — including not just what to build but the curated codebase intelligence and execution runbook needed for the AI to plausibly ship working code on the first pass.

[[Rasmus]]'s own one-liner:
> *"A PRP is a PRD plus curated codebase intelligence plus agent runbook, aiming to be the minimum viable packet an AI needs to plausibly ship production-ready code on the first pass."*

[[ColeMedin]] uses it as his canonical context-engineering toolkit across his content from mid-2025 onwards.

## Key Information

### The three-step user flow

1. **Edit `initial.md`** — describe the feature you want built. Sections: feature description, examples (point at code in `examples/`), documentation (URLs, MCP servers like [[Crawl4AIRAG]]), considerations (gotchas, project-specific quirks).
2. **`/generate-prp initial.md`** — run a slash command in [[ClaudeCode]] (or paste the equivalent prompt into your IDE). The AI researches APIs, analyzes the existing codebase, looks at examples, references documentation, and produces a comprehensive PRP file in `PRPs/<feature>.md`. Takes 5-15 minutes.
3. **Validate the PRP** — read it. Check that documentation references are right, the planned file structure matches your project, [[ValidationGates]] are sensible, and the confidence score is reasonable. Iterate if needed (Cole's pro tip: ask "what would it take to get this to 10/10 confidence?").
4. **`/execute-prp <path>`** — Claude Code reads the PRP, builds an extensive task list, knocks out tasks one by one, runs validation gates (linting + tests), iterates until tests pass. Takes 25-60+ minutes for non-trivial features.

### Planning refinement: reduce assumptions via clarifying questions (2026)

Per `summary-agent-teams-live-build`, Cole's mature planning loop sharpens the "generate-prp" step into an explicit conversation before the structured plan is written:

1. **`/prime`** — run at the start of every new build to load codebase context.
2. **Unstructured brain-dump** — describe the feature; tell the agent to search the codebase *and* the web.
3. **Force clarifying questions** — *"The number one goal of planning is to reduce the number of assumptions the coding agent is making."* Cole demands **≥10 questions**. Rationale: there are two kinds of agent mistakes — writing bad code, or deviating from intent — and "technically both are your fault"; questions surface assumptions you didn't realize you were making.
4. **AskUserQuestion tool** — [[ClaudeCode]]'s multiple-choice question UI (with a recommended option and a free-form box) makes the Q&A fast. It asks a few at a time and isn't dynamic across prior answers, so you sometimes restate context.
5. **Formalize + review** — a `/plan` command writes the structured plan; then **review it carefully** because it's high-leverage ("one error in your plan → hundreds of lines of bad code; one bad line is just one line"). Then [[ContextReset|reset context]] and implement.

### What goes where

[[Rasmus]]'s heuristic for placing context, captured in `summary-context-engineering-101`:

| Layer | Role | Stability |
|---|---|---|
| `CLAUDE.md` | Things that are true forever in this codebase: naming, file structure, core utilities | Forever |
| `.claude/commands/*.md` (slash commands) | Domain-agnostic workflows: research, plan, execute | Per project type |
| `PRPs/templates/base-prp.md` | Domain-specific intelligence: framework patterns, common gotchas, doc references | Per use case |
| `PRPs/<feature>.md` (generated PRP) | Feature-specific plan with all the curated context | Per feature |

### Use-case templates

The breakthrough Cole and Rasmus shipped in mid-2025: don't just have *the* PRP framework — have a **specialized template per (language × project type)**. Each template includes a base PRP pre-loaded with that domain's patterns and a scaffold codebase the generated PRP builds on.

Templates Cole has shipped in this corpus:

| Template | Use case | Source video |
|---|---|---|
| Generic | Any project | Intro video (`summary-context-engineering-is-new-vibe-coding`) |
| **MCP servers** (TypeScript / Cloudflare Workers) | Build a [[ModelContextProtocol]] server | `summary-context-engineering-101` |
| **PydanticAI agents** (Python) | Build an AI agent with [[PydanticAI]] | `summary-context-engineering-blueprint-for-ai-agents` |

The vision (Dynamis community project): a repository of templates spanning every major framework × project type combination.

### [[ValidationGates]]

Explicit instructions baked into the PRP telling the AI to run linting, write and run unit tests, and iterate until tests pass before declaring done. Distinct from human validation (which still happens). The gates make the AI self-validate within a known correctness frame.

### Why it works

- **The AI sees the same kind of doc a developer would expect.** PRDs are familiar; this is a PRD with extra agent-specific context.
- **Two-pass design.** Plan (generate-prp) and execute (execute-prp) are separated so the human can validate the plan before letting the AI burn 30 minutes implementing.
- **Composable templates.** A new project of a known type starts ~80% pre-engineered.
- **Self-validating.** ValidationGates create a tight inner loop where the AI catches its own mistakes before reporting "done."

### Maturity caveat

Per [[Rasmus]]: the PRP framework was iterating for over a year before Claude 4 made it reliably one-shot 1000+ line PRPs. On older model generations the framework worked but was less reliable. Implication: the framework is partially a bet on continuing model capability gains making bigger, more comprehensive PRPs viable.

## Related

- [[Rasmus]] — creator
- [[ContextEngineering]] — the meta-pattern PRP framework implements
- [[ClaudeCode]] — primary execution surface
- [[ValidationGates]] — sub-pattern
- [[ColeMedin]] — primary teacher in this corpus
- [[ModelContextProtocol]], [[PydanticAI]] — domains with shipped templates
- [[summary-context-engineering-is-new-vibe-coding]] — intro
- [[summary-context-engineering-101]] — Rasmus on the framework, MCP-server template
- [[summary-context-engineering-blueprint-for-ai-agents]] — PydanticAI template
- [[summary-agent-teams-live-build]] — the clarifying-questions planning refinement
