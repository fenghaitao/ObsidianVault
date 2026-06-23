---
title: "IntentEngineering"
type: concept
tags: [concept, ai-coding, paradigm, context-engineering, intent]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260305 - Is Software Engineering Finally Dead.md"
last_updated: 2026-06-20
---

## Definition

Intent Engineering is the evolution *beyond* [[ContextEngineering]]: not just giving an agent all the context about the codebase, but being explicit about **what success looks like** — clear success criteria, how the agent should validate its own work, and tight alignment on *what* is being built — so that the result is not only code-correct but is the *right thing*. The term is popularized by **Nate B. Jones**; [[ColeMedin]] frames it as the stage where working with coding agents becomes, in substance, senior software engineering.

## Key Information

### The evolution

```
Prompt Engineering   → word a single prompt for a single good output
Context Engineering  → build a whole context ecosystem (rules, docs, examples, plans)
Intent Engineering   → + success criteria, self-validation strategy, alignment on intent
```

Each stage looks *more* like software engineering and less like "prompting." By the intent-engineering stage, the human owns everything except the keystrokes of code: architecture, tech stack, requirements translation, success criteria, validation design, and review.

### What it adds over context engineering

- **Success criteria up front** — define "done" explicitly so the agent (and you) can tell when the feature is actually complete.
- **Self-validation strategy** — specify how the agent verifies its own work (tests, e2e, review passes) — overlaps with [[ValidationGates]] and the [[PIVLoop]]'s validate step.
- **Alignment on intent** — reduce assumptions so the build matches what you actually want, not just something that compiles (connects to the "ask clarifying questions to reduce assumptions" planning practice in [[PRPFramework]]).

### Why it matters (the "SWE isn't dead" argument)

Per `summary-is-software-engineering-dead`, the prompt→context→intent progression is [[ColeMedin]]'s evidence that software engineering endures: as coding gets automated, the *engineering* (deciding what to build, defining correctness, validating, coordinating) becomes the job. "Great engineers are more important than ever" (Boris Cherny).

## Related

- [[ContextEngineering]] — the predecessor stage
- [[AgenticEngineering]] — the practitioner discipline this fits within
- [[PIVLoop]] — the plan/validate workflow that operationalizes intent
- [[ValidationGates]] — the self-validation half of intent
- [[PRPFramework]] — clarifying-questions planning serves intent alignment
- [[VibeCoding]] — the opposite end of the spectrum
- [[ColeMedin]] — articulator in this corpus
- [[summary-20260305 - Is Software Engineering Finally Dead]] — primary source
