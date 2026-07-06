---
title: "StaticVsDynamicContext"
type: concept
tags: [concept, context-management, google, progressive-disclosure, context-rot]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good).md"
last_updated: 2026-07-06
---

## Definition

Static vs. dynamic context is [[Google]]'s delineation (via its agentic-engineering masterclass, per [[ColeMedin]]) between the two ways context reaches a coding agent's window: **static context** is guaranteed-loaded every session (system prompt, core rules/guardrails), and **dynamic context** is fetched on demand only when the agent decides it's relevant (skills, per-area conventions, retrieved docs).

## Key Information

### The tradeoff

| | Static context | Dynamic context |
|---|---|---|
| When loaded | Every session, up front | Only when the agent seeks it out |
| Reliability | High — guaranteed present | Lower — depends on the agent choosing to load it |
| Cost | Expensive — fills the context window before any work starts | Efficient — scales to far more total context than would ever fit statically |
| Failure mode | None (it's always there) | Agent doesn't load the skill/doc/RAG result when it should have |

Context is the scarcest resource in an AI coding assistant session, both for cost and for avoiding [[ContextRot]] (LLMs get overwhelmed with irrelevant information just like people do). The practical rule: keep static context lean (just enough rules/guardrails to be safe), and push everything else into dynamic context that's fetched only when needed.

### Why this matters now

Models are getting steadily better at reliably reaching for dynamic context (loading the right skill, running the right retrieval) when it should. This is why [[ClaudeSkills|agent skills]] are becoming central to harness design: rather than cramming every piece of specialized knowledge into the system prompt, skills let an agent stay a lightweight generalist that "flexes into specialist roles on demand" via [[ProgressiveDisclosure]]. Cole connects this directly to why heavy, pre-built multi-agent systems with many narrow specialists are falling out of favor — one generalist agent plus well-designed dynamic context (skills) covers most of what those systems were built to solve.

## Related

- [[ProgressiveDisclosure]] — the mechanism dynamic context relies on
- [[ContextRot]] — the failure mode static-context bloat causes
- [[ClaudeSkills]] — the primary dynamic-context vehicle
- [[AILayer]] — where static rules and dynamic skills both live in a coding-agent harness
- [[AIDrivenSDLC]] — the broader framework this concept comes from
- [[Google]] — source of this framing
- [[ColeMedin]] — narrator/analyst
- [[summary-20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)]] — primary source
