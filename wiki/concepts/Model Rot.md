---
title: "Model Rot"
type: concept
tags: [ai, models, context-engineering, knowledge-cutoff, documentation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Model rot is the degradation of a model's usefulness for fast-moving software projects because the model was trained on a snapshot of the web from 6-18 months ago and no longer represents current reality. APIs change, patterns evolve, and the model invents keys, patterns, and APIs that don't exist.

## Key Information
- Articulated by Danilo Campos (PostHog) in the context of building the PostHog Wizard
- Models are expensive to train, so they sit frozen in time while software projects evolve
- Fast-moving software projects are especially vulnerable: the model "doesn't know what the hell is going on anymore"
- Before PostHog addressed this, agents would make up keys, invent patterns, and create non-existent APIs when asked to integrate PostHog
- Primary solution: inject fresh, up-to-date markdown documentation into the agent's context
- With large context windows, "you can't beat just shoving a bunch of markdown files into the context and patching the holes"
- PostHog's implementation: documentation on posthog.com is always fresh; the agent uses tools to select and load relevant markdown into its context
- RAG (Retrieval-Augmented Generation) is also a valid approach, but direct context injection with large windows is highly effective
- Related to but distinct from Context Rot (degradation during extended interactions) and Doc Rot (outdated documentation)

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (model rot drives need for continuous re-optimization)
- [[DaniloCampos]] — articulated the concept
- [[PostHogWizard]] — product that solves this problem
- [[KnowledgeCutoff]] — related concept
- [[ContextRot]] — distinct but related: degradation during interactions
- [[RAG]] — alternative solution approach
- [[ContextEngineering]] — broader discipline
- [[Agent Optimization]] — optimization must be re-run as models change
