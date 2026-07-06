---
title: "DeterministicVsAgenticNodes"
type: concept
tags: [concept, dark-factory, workflow-design, reliability]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why).md"
last_updated: 2026-07-06
---

## Definition

Deterministic vs. agentic nodes is a workflow-design principle, cited by [[ColeMedin]] in the context of [[DarkFactory]] design: not every step in an autonomous pipeline needs an LLM call. Steps that have one clearly-correct outcome (formatting code, running a linter, triggering a deployment) should be handled by plain deterministic code; steps that genuinely require reasoning or judgment should be handled by an LLM-driven agent.

## Key Information

### Why it matters

Using an agent (an LLM call) for a step that has a single correct, mechanically-derivable answer adds unnecessary cost, latency, and failure surface (the LLM could get it wrong) compared to just running the deterministic code. Reserving agentic nodes for steps that genuinely need reasoning keeps a multi-stage pipeline (like a [[DarkFactory]]) both cheaper and more reliable.

### Example

[[Stripe]]'s internal "Stripe Minions" system is cited as an example of a pipeline that deliberately mixes both: some steps run as deterministic code, others as LLM-driven agentic steps, chosen per-step based on whether reasoning is actually required.

## Related

- [[DarkFactory]] — the context this principle was raised in
- [[Stripe]] — cited example ("Stripe Minions")
- [[HarnessEngineering]] — the broader discipline of designing reliable agent workflows
- [[ColeMedin]] — articulator in this context
- [[summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)]] — primary source
