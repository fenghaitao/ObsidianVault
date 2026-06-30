---
title: "ContextFeedbackLoop"
type: concept
tags: [context, feedback, observability, optimization, flywheel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
The Context Feedback Loop is the mechanism by which context (prompts, skills, instructions) is continuously improved based on observations from agent logs, PR reviews, and production behavior. It forms the Observe → Adapt → Regenerate portion of the Context Development Life Cycle.

## Key Information
- Part of the Context Development Life Cycle (CDLC), introduced by Patrick Debois
- Three levels of feedback loops:
  - **Individual**: Developer improves their own context based on personal experience
  - **Team**: Team makes context improvement a reflex — if something is missing, add context
  - **Organizational**: Cross-team flywheel — fix context once, all teams benefit
- Feedback sources: agent logs (agents saying "we're missing X"), PR reviews (feedback on agent-generated code), production instrumentation (failures in deployed code)
- Enables context optimization: use test failures and feedback to iteratively improve context quality
- The flywheel effect: better context → better agent output → fewer issues → more trust → more context investment

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDevelopmentLifeCycle]] — the lifecycle containing this loop
- [[ContextObservability]] — the observation that feeds the loop
- [[ContextOptimization]] — the action taken based on feedback
- [[Feedback Loops as AI Speed Limit]] — related concept
