---
title: "summary-20260501 - Shipping complex AI applications — Braintrust & Trainline"
type: source
tags: [source, transcript, evals, observability, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Shipping complex AI applications — Braintrust & Trainline.md"]
last_updated: 2026-06-29
---

## Core Summary

A hands-on workshop by Braintrust and Trainline on shipping quality AI applications at scale. Duran (Braintrust) and Osama/Mayank (Trainline) demonstrate how to build a multi-stage agentic AI system with tool calling, instrument it with Braintrust for observability, identify failure modes using golden tests, and complete the feedback loop with production data. Trainline shares their real-world experience running a multi-agent travel assistant serving 27 million users and processing 6.3 billion ticket bookings annually.

## Key Points

- The workshop builds a multi-stage agentic system with tool calling, then instruments it with Braintrust for evaluation and observability.
- The core flywheel: start with an evaluation set, identify failure modes, remediate, ship, monitor, and repeat.
- Braintrust is a Series B company ($80M raised at $800M valuation) building AI observability and evaluation infrastructure with a custom database called Brainstorm.
- Trainline runs both classic ML models (train disruption prediction) and generative AI multi-agent systems (travel assistant handling refunds and ticket changes).
- The gap between prototype and production is not model intelligence but operational rigor: deterministic software engineering practices don't directly apply to non-deterministic LLM systems.
- Braintrust is tool-agnostic, working with any agent framework or LLM provider.

## Related

- [[Braintrust]] — AI observability and evaluation platform
- [[Trainline]] — train ticketing platform with AI-powered travel assistant
- [[EvalEngineering]] — evaluation engineering practice
- [[AgentObservability]] — monitoring and evaluating AI agents
- [[EvalFlywheel]] — iterative evaluation and improvement cycle
