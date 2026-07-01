---
title: "Explicit Signals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"]
last_updated: 2026-06-29
---

# Explicit Signals

## Definition

Explicit signals are objective, verifiable indicators of agent health that deal with measurable, true/false metrics. Introduced by Zubin Koticha of Raindrop, they complement implicit signals (semantic, harder-to-detect) and form the foundation of agent production monitoring.

## Key Information

### Core Explicit Signals

- **Error rate**: Especially tool error rate — if it spikes, something is likely wrong. A flat error rate can also be informative.
- **Latency**: Response time trends; spikes indicate performance degradation.
- **User regenerations**: How often users regenerate agent responses — a proxy for dissatisfaction.
- **Cost**: Token usage and compute spend; spikes may indicate runaway agents or inefficient tool use.

### Characteristics

- Objective and verifiable — true or false, no ambiguity
- Easier to track than implicit signals
- Form the baseline of any agent observability setup
- Can be tracked by traditional monitoring tools (Sentry, LogRocket, DataDog)
- Raindrop also captures explicit signals from telemetry data (tool errors, exceptions in traces)

### Relationship to Implicit Signals

Explicit signals tell you *that* something is wrong; implicit signals tell you *what* is wrong. A spike in error rate might be caused by a specific tool failing, but user frustration signals can reveal that the real problem is the agent's response quality, not just the error itself.

## Related

- [[ImplicitSignals]] — complementary semantic signal category
- [[AgentObservability]] — parent concept
- [[AgentExperiments]] — using signals for production A/B testing
- [[Raindrop]] — platform providing both explicit and implicit signals
- [[ZubinKoticha]] — introduced the concept
- [[Sentry]] — traditional monitoring for explicit signals
- [[LogRocket]] — traditional monitoring for explicit signals
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
