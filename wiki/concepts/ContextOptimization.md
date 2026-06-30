---
title: "ContextOptimization"
type: concept
tags: [context, optimization, feedback, improvement, iteration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Optimization is the practice of iteratively improving AI context (prompts, skills, instructions) based on test feedback, agent observations, and production data. It is the "Adapt" phase of the Context Development Life Cycle.

## Key Information
- Part of the Context Development Life Cycle (CDLC) Adapt phase, introduced by Patrick Debois
- Uses test feedback (from context testing) to identify what's not working and improve it
- Can be automated: run evals, get LLM feedback on what's missing or unclear, regenerate context with improvements
- Can run in CI/CD: when context changes are committed, run the test suite and optimize based on results
- The goal is to move from "copy-pasting context and hoping for the best" to "engineering context with data-driven improvement"
- Scales from individual (improving personal markdown) to organizational (cross-team context flywheel)
- LLMs are the engine; context is the fuel — you can't change the LLM, but you can optimize your context

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDevelopmentLifeCycle]] — the lifecycle containing this phase
- [[ContextTesting]] — the testing that provides optimization feedback
- [[ContextFeedbackLoop]] — the feedback mechanism driving optimization
- [[PromptOptimization]] — related practice for optimizing individual prompts
- [[EvalEngineering]] — practice of crafting evals that produce actionable optimization feedback
