---
title: "Observability and Evals Unified"
type: concept
category: methodology
tags: [observability, evals, systems-design, agent-quality, braintrust]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Observability and evals are the same problem from a systems perspective. The only difference is that evals run in batch with known inputs ahead of time, while observability runs in real time with unknown inputs. Both are solved by the same underlying infrastructure — the same database, same query patterns, same scoring functions. Braintrust treats them as a unified system, not separate concerns.

## Key Information

- **Evals**: Run in batch, inputs known ahead of time, used for pre-production experimentation and confidence-building
- **Observability**: Runs in real time, inputs unknown, used for post-production monitoring and confidence maintenance
- **Unified system**: Same database, same trace storage, same scoring functions, same query patterns
- **The flywheel**: Production traces captured via observability can be added to offline datasets for experimentation via evals — closing the loop
- This unification is a key architectural insight: you don't build separate eval and observability systems; you build one system that handles both batch and real-time workloads
- The practical implication: when a trace comes in via observability, you've already traced it — you can immediately add it to an offline dataset for experimentation
- This perspective contrasts with organizations that treat evals (pre-production) and observability (post-production) as separate tools, teams, and workflows

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[AgentObservability]] — the production side of the unified system
- [[EvalFlywheel]] — the continuous loop enabled by this unification
- [[Braintrust]] — platform that implements this unified approach
- [[AgentQualityPlatform]] — the platform category built on this unification
- [[EvalPlatforms]] — closely related platform category
- [[OnlineEvals]] — scoring functions running on observability traffic
- [[OfflineEvals]] — scoring functions running in batch
