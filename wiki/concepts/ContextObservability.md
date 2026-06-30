---
title: "ContextObservability"
type: concept
tags: [context, observability, agent-logs, feedback, production]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Observability is the practice of monitoring how AI context (prompts, skills, instructions) performs in practice by analyzing agent logs, PR review feedback, and production behavior to identify missing, incorrect, or ineffective context that should be improved.

## Key Information
- Part of the Context Development Life Cycle (CDLC) Observe phase, introduced by Patrick Debois
- Three primary feedback channels:
  - **Agent logs**: When agents consistently say "we're missing this piece," surface that pattern and create context for it. Standards like agent.md enable reading from logs.
  - **PR reviews**: Feedback on PRs that were created with certain context — if something is incorrect, improve the context rather than arguing on the PR
  - **Production instrumentation**: Code generated from context running in production — when it fails, capture the input/output and create a test case so it doesn't happen again
- At organizational scale: if many developers' agents are missing the same piece of context, create it once and distribute to everyone
- Enables a feedback flywheel: observe → adapt → regenerate → distribute → observe
- Contrasts with individual context crafting where developers improve their own markdown in isolation

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDevelopmentLifeCycle]] — the Observe phase
- [[ContextFeedbackLoop]] — the feedback flywheel enabled by observability
- [[AgentObservability]] — the broader agent observability practice
- [[Harness Engineering]] — related paradigm with similar feedback concepts
- [[ContextOptimization]] — acting on observability findings
