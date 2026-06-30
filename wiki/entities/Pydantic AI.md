---
title: "Pydantic AI"
type: entity
tags: [tool, python, agent-framework, structured-outputs, pydantic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Pydantic AI is an agent framework built by the Pydantic company that leverages Pydantic models for structured outputs, agent definitions, and eval systems. It integrates with Pydantic Logfire for observability and supports GEPA-based prompt optimization.

## Key Information
- Agent framework from the creators of Pydantic
- Uses Pydantic models to define agent output types (structured outputs), tool schemas, and eval datasets
- Supports custom evaluators for deterministic evals against golden datasets
- Integrates with Pydantic Logfire for tracing, evals, and managed variables
- Provides an `override` functionality to swap prompts and models during evaluation
- Supports parallel eval execution with configurable max concurrency
- Has a `run_agent` function that takes HTML/text input and returns structured Pydantic model output
- The eval system includes `dataset.evaluate()` which takes a function and runs all cases
- Can be turned into a web chat interface via integration with the cell AI protocol
- Agents can be composed: one agent can call another agent as a tool
- The proposer agent pattern: a Pydantic AI agent proposes new prompts to optimize another Pydantic AI agent

## Related
- [[Pydantic]] — the validation library it's built on
- [[Pydantic Logfire]] — observability platform it integrates with
- [[Samuel Colvin]] — creator
- [[GEPA]] — optimization algorithm used with Pydantic AI
- [[Agent Optimization]] — core use case
- [[Structured Outputs]] — pattern enabled by Pydantic models
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
