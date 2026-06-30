---
title: "Non-Deterministic Agents"
type: concept
category: methodology
tags: [agents, non-determinism, observability, llm, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Non-deterministic agents are AI agents powered by LLMs whose behavior cannot be predicted through fixed code paths. Unlike traditional deterministic applications with known control flow, LLM-based agents exhibit high variety and abstracted reasoning, taking different paths to accomplish tasks based on context, model behavior, and tool interactions. This non-determinism is the fundamental reason agent observability must be broader than traditional observability and why traditional unit tests must be replaced with statistical evals.

## Key Information

- Traditional applications have deterministic code paths with known control flow — they behave predictably on purpose
- LLM-based agents are non-deterministic by design: the same input can produce different reasoning paths, tool calls, and outputs
- This non-determinism is a feature, not a bug — it's why LLMs are powerful (high variety, abstracted reasoning)
- Because agents can take unpredictable paths, observability must measure qualitative aspects beyond uptime and latency:
  - **Groundedness**: Was the response grounded in the retrieved context?
  - **Tool usage**: Were expected tools used during reasoning?
  - **Brand alignment**: Does the response match the system prompt standards?
- Traditional observability metrics (latency, error rate) are insufficient for evaluating non-deterministic agent behavior
- Non-determinism requires different personas in the observability loop: non-technical domain experts who can assess whether the agent's unpredictable path led to a correct or acceptable outcome
- **Philipp Schmid's framing**: Because agents are non-deterministic, we must move from unit tests (assert `input A → output C`) to statistical evals (measure how often the agent succeeds). A customer agent that works 1/10 times is useless. We need to find the right balance of reliability

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker who connected non-determinism to the evals shift
- [[AgentObservability]] — the broader observability paradigm driven by non-determinism
- [[TraditionalObservability]] — the narrower paradigm designed for deterministic applications
- [[AgentTraceData]] — the semi-structured, voluminous data produced by non-deterministic agents
- [[CrossFunctionalAgentTeams]] — diverse teams needed to evaluate non-deterministic agent behavior
- [[PhilHetzel]] — presenter who framed non-determinism as Problem 1 of agent observability
- [[Evaluate Dont Just Assert]] — the testing paradigm shift required by non-determinism
- [[Handing Over Control]] — related concept: trusting non-deterministic LLM decisions
