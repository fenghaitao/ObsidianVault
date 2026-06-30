---
title: "Capability Evals"
type: concept
tags: [eval, testing, improvement, regression]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Capability evals and regression evals are two complementary categories of evaluation. A capability eval gives an agent a "hill to climb" — a task it's currently bad at with room to improve. Once it reaches 100%, the capability eval becomes a regression eval, ensuring the agent maintains that capability going forward.

## Key Information
- **Capability eval**: Tests something the agent is known to be bad at. Provides a measurable target for improvement. Designed to be failed initially and passed over time through iteration
- **Regression eval**: A previously-passed capability eval. Ensures the agent can always do what it used to do. Prevents regressions when prompts or models change
- Lifecycle: constantly turn capability evals into regression evals while adding new capability evals for new functionality
- Example from workshop: the actionability eval was a capability eval (6/13 passes initially). After prompt improvements, it became a regression eval (6/6 on previously failing tests)
- In the eval suite lifecycle, most evals become regression evals — running cheaply and quickly to catch regressions
- Capability evals are where you invest the most in terms of judge model quality and rubric detail — they drive improvement
- Regression evals can often be downgraded or compressed — you don't need all 100 regression evals; a representative sample of 20 may suffice
- On live production traces, only run regression evals (capability evals don't change)
- Anthropic used this pattern with Claude Code: built capability evals for desired features, gave Claude Code a hill to climb, and when new models dropped, ran the suite to see which bets paid off

## Related
- [[Code Evals]] — can serve as either capability or regression evals
- [[LLM-as-Judge]] — can serve as either capability or regression evals
- [[Actionability Eval]] — example of a capability eval that became a regression eval
- [[Eval-Driven Development]] — writing capability evals before building features
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
