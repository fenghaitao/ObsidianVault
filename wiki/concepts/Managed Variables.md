---
title: "Managed Variables"
type: concept
tags: [observability, deployment, ab-testing, configuration, logfire]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Managed Variables are a Pydantic Logfire feature that extends prompt management to any Pydantic model, enabling runtime updates to agent configuration (prompts, models, temperature, etc.) without redeployment, with A/B testing via the OpenFeature standard.

## Key Information
- Evolution beyond simple prompt management: any Pydantic model can be managed inside Logfire
- Variables can be structured objects with multiple fields (instructions, model name, max tokens, temperature)
- **A/B testing**: Via targeting, define what percentage of calls use which variable values — built on the OpenFeature open standard
- **No redeployment**: Changing a variable in Logfire updates agent behavior on the next function call without restarting servers
- **Version history**: Logfire tracks the history of variable updates
- **Code default**: Variables have a default value defined in code; the platform value overrides it
- **Permissions**: Requires a separate API key with variable read/write permissions
- **Self-driving vision**: The goal is to wire GEPA optimization directly into managed variables so the platform autonomously adjusts variables to improve agent performance
- Demonstrated by switching an agent's reply language (English → French → German) and model (Anthropic → OpenAI) without redeployment
- Enables experimentation in production: test new prompts or models on a percentage of traffic

## Related
- [[Pydantic Logfire]] — the platform providing managed variables
- [[Agent Optimization]] — the optimization loop managed variables enable
- [[GEPA]] — the optimization algorithm
- [[Pydantic AI]] — agent framework using managed variables
- [[AI Observability]] — broader category
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
