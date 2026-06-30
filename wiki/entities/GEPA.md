---
title: "GEPA"
type: entity
tags: [tool, optimization, genetic-algorithm, prompt-engineering, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
GEPA (Genetic Evolutionary Pareto Algorithm) is an optimization library created by Lakshya, a first-year PhD student at Berkeley. It uses genetic algorithms to optimize strings (prompts or JSON data) by selecting candidates from the Pareto frontier of best performers, mixing them, and using a proposer agent to generate new candidates.

## Key Information
- Name derives from "genetic" (genetic algorithm) + "Pareto" (Pareto frontier selection)
- Optimizes a string — can be a text prompt or JSON data containing arbitrary configuration
- **Genetic algorithm approach**: Takes the best candidates (Pareto frontier), mixes them, and produces new candidates — analogous to breeding the best race horses
- **Proposer agent**: An LLM-based agent that generates new prompt candidates based on context about what has worked and failed
- **Pareto frontier**: Only the best-performing candidates are selected for breeding; poor performers are excluded
- **Adapter pattern**: Users define adapters that specify how the proposer agent works and how evaluation is performed
- Sync-only (not async), requiring workarounds for async HTTP connections
- Created by Lakshya at Berkeley; Colvin notes the code is not very type-safe or polished but is state-of-the-art
- Used by Shopify to reduce costs from $5M/year to $73K/year by optimizing prompts for a Qwen-based agent
- Can optimize multiple keys in a dict simultaneously (e.g., model + system prompt, or different lines of a prompt)
- Operates on batches of test cases; can dynamically adjust batch size based on performance
- Progress can be tracked via instrumented print output fed into Logfire
- Colvin is "itching to either fix it or fork it" due to code quality concerns

## Related
- [[GEA]] — DSPy's related evolutionary optimizer
- [[Jeba]] — related prompt optimization technique
- [[Agent Optimization]] — core use case
- [[Pareto Frontier]] — the selection strategy it uses
- [[PromptOptimization]] — the broader category
- [[Pydantic AI]] — agent framework used with GEPA
- [[Shopify]] — notable case study
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
