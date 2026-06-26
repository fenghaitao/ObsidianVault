---
title: "Eval Platforms"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Eval platforms are systems for evaluating LLM-powered agents before and after production deployment. While the surface-level requirements seem simple — execute an agent, display outputs and scores, gather input examples — the full scope is far more complex, encompassing data infrastructure, observability integration, experimentation tooling, and multi-persona collaboration.

## Key Information

- **Core components**: execution engine, UI for outputs/scores, input example management
- **Hidden complexity**: data layer for high-velocity, large, semi-structured traces; query patterns for both low-latency viewing and aggregate analytics; full-text search across LLM outputs
- **Multi-persona**: Must serve engineers (product, AI, systems), SMEs with domain knowledge, and non-technical stakeholders
- **Systems problem**: Building eval platforms is fundamentally a data systems challenge, not just a UI/UX problem
- **Non-functional requirements**: Role-based access control, data masking, governance at scale
- **Future**: Platforms must be built for both humans and coding agents (headless evals); AI proxy/gateway for automatic tracing

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — agent quality platform
- [[EvalMaturityStages]] — progression of eval platform sophistication
- [[EvalFlywheel]] — observability-evals loop
- [[TraceDataChallenges]] — data layer challenges
- [[AgentQualityPlatform]] — platform category
