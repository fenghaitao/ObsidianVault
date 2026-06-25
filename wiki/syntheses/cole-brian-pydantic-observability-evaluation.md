---
title: "cole-brian-pydantic-observability-evaluation"
type: synthesis
tags: [synthesis, comparison, observability, evaluation, cole-medin, brian-casel, pydantic]
sources: []
last_updated: 2026-06-25
---

# How Cole Medin, Brian Casel, and Pydantic Approach Observability and Evaluation

## Cole Medin: The Conceptual Framework

Cole Medin frames observability as "100% necessary for production" and evaluation as consuming "75% of agent development time" [[AgentObservability]], [[AgentEvaluation]]. His stack includes Langfuse/Helicone for general observability and Logfire for PydanticAI-native tracing. His eval methodology uses YAML test cases with custom evaluators (LLM-as-judge, task-completion testing). The key insight is the feedback loop: observability surfaces real-world failure modes → those become eval cases → eval cases drive iteration → improved agent ships → observability watches it.

Cole's emphasis is on *continuous* evaluation — run a cheap smoke test (Haiku) on every prompt or skill change. His "golden dataset" pattern (define expected behavior for known inputs, assert correctness) is the practitioner-level implementation of the eval philosophy.

## Brian Casel: The Pragmatic Solo-Builder Approach

Brian Casel approaches quality assurance through [[EndToEndTesting]] and [[VerificationCriteria]] rather than continuous observability infrastructure. His pattern: define what "done" means before the agent starts (verification criteria in the spec), then review at milestone boundaries. He uses Kain AI for browser-based QA — clicking through the app like a real user to verify critical flows [[summary-20260414 - We build fast. But does it work]].

The Night Shift model's "shared interface" (markdown with checkboxes) serves as a lightweight evaluation surface: did the agent do what was expected? Human review is baked into every cycle — 2-20 minute sessions checking agent output. This is lower-fidelity than Cole's systematic eval framework but sufficient for a solo builder shipping internal tools.

## Pydantic: The Production Infrastructure

Pydantic's approach is the most infrastructure-heavy. [[Logfire]] provides OpenTelemetry-based distributed tracing with AI-specific features: token counting, cost tracking, MCP cross-process tracing, and real-time trace viewing (modified OTel to stream before trace completion). Samuel Colvin emphasizes that Logfire is general-purpose, not AI-only — "AI doesn't exist in a vacuum" — capturing database queries, API calls, and application errors alongside LLM traces [[Logfire]].

PydanticAI ships a built-in eval framework. Pamela Fox's PyAI Conf research [[summary-20260330 - Pamela Fox Improving MCP tool schemas to increase agent reliability - PyAI Conf 2026]] demonstrates systematic evals across models and schema variants, finding that modern LLMs are good enough that schema strictness matters less than expected — but you can only know that by running the evals. DBOS integration adds durable execution tracing [[DBOS]]. Shifra Williams' Render demo [[summary-20260508 - Shifra Williams - What your AI pipeline does when you're not looking - PyAI London at AIE 2026]] shows cost tracking per pipeline stage using Pydantic GenAI prices.

## The Convergence

All three agree: you can't improve what you don't measure. Cole provides the conceptual framework and practitioner heuristics. Brian provides the lightweight, solo-builder-friendly pattern. Pydantic provides the production-grade infrastructure. They're complementary layers — Cole tells you *why* and *what* to measure, Brian shows you *how* to keep it simple, and Pydantic gives you the *tools* to do it at scale.

## Related

- [[AgentObservability]] — Cole's framing
- [[AgentEvaluation]] — Cole's methodology
- [[Logfire]] — Pydantic's observability platform
- [[EndToEndTesting]] — Brian's QA approach
- [[VerificationCriteria]] — Brian's done-is-done pattern
- [[PydanticAI]] — framework with built-in evals
- [[DBOS]] — durable execution observability
- [[ColeMedin]] — conceptual framework
- [[BrianCasel]] — pragmatic approach
- [[SamuelColvin]] — Logfire creator
