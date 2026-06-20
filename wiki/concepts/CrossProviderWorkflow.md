---
title: "CrossProviderWorkflow"
type: concept
tags: [concept, multi-model, workflow, harness, handoff, cost]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends.md"
last_updated: 2026-06-21
---

## Definition

A cross-provider (multi-model) workflow chains **separate coding-agent sessions from different model providers**, each playing to its strength, communicating via **handoff markdown documents**. [[ColeMedin]]'s canonical example: Gemini 3.5 Flash designs the UI, Opus 4.8 plans/writes copy/handles integrations, Sonnet does cheap exploration/validation. It's a concrete [[AgentHarness]] pattern that turns model *specialization* into a single pipeline.

## Key Information

### Why separate sessions + handoff docs

1. **You can't mix providers in one context window** — there's no way to continue an Opus conversation as Gemini, so each provider gets its own session.
2. **One focused task per session** — even the best models get overwhelmed doing explore→plan→UI→integrate→deploy at once ([[ContextRot]]). Each node does one thing and writes a markdown doc the next node reads.

This makes the workflow **easy to experiment with**: swap a provider per node in minutes to find the best mix.

### Match the model to the task

| Task | Model (example) | Why |
|---|---|---|
| Exploration / validation | Sonnet | cheap, fast, low reasoning need |
| Planning / copy / integrations | Opus 4.8 | best reasoning; avoids hallucinated content |
| UI design | Gemini 3.5 Flash | human-looking UIs, cheap (~$1.50/M in) |

### Let each model own its strength (don't over-specify)

A key lesson: the **plan deliberately omits UI structure**. When the planner (Opus) described layouts, it "steamrolled" the UI model (Gemini) and the result looked *worse*. Hand the UI model intent and copy, not grids/columns. (Plan sections: content & intent / integration scope / deployment — no structure.)

### Secondary benefit: cost

Spend lots of tokens where they're cheap (UI on Gemini Flash) and reserve the expensive reasoning model (Opus) for the parts that need it.

### Relationship to other patterns

- A specific [[AgentHarness]] / orchestrated workflow; can be bundled into a one-shot run by [[Archon]].
- Related to cross-model [[AdversarialDev]] (different models, different blind spots) — here the diversity is exploited for *specialization*, not just critique.
- Run the steps as [[ClaudeSkills|skills]] across hosts ([[ClaudeCode]] for Claude steps, [[Pi]] / [[Antigravity]] for Gemini steps).

## Related

- [[AgentHarness]] — the family
- [[Pi]], [[Antigravity]] — hosts for the non-Claude (Gemini) steps
- [[ClaudeCode]] — host for the Claude/Opus/Sonnet steps
- [[Archon]] — one-shot orchestration
- [[AdversarialDev]] — cross-model critique (sibling use of model diversity)
- [[ContextRot]] — why one focused task per session
- [[ColeMedin]] — articulator
- [[summary-claude-plans-gemini-designs]] — primary source
