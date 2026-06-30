---
title: "EvalFlywheel"
type: concept
tags: [evals, observability, ai-engineering, continuous-improvement]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Shipping complex AI applications — Braintrust & Trainline.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-29
---

## Definition

The eval flywheel is an iterative AI development pattern: start with an evaluation set (even for new applications), identify failure modes from production traces, remediate the issues, ship improvements, monitor the results, and repeat. It applies Agile principles to AI system development.

## Key Information

- Inspired by Agile development philosophy: "perfection is the enemy of good"
- Cycle: instrument application → collect traces → identify failure modes → remediate → ship → monitor → repeat
- Can start with a manually created evaluation set for new applications
- For existing applications, production traces provide real-world failure modes
- Golden tests help verify specific failure modes are fixed before deployment

## Related

- [[summary-20260501 - Shipping complex AI applications — Braintrust & Trainline]] — source
- [[EvalEngineering]] — evaluation engineering
- [[Braintrust]] — platform implementing this pattern
- [[AgentObservability]] — observability component of the flywheel
- [[ContinuousImprovement]] — related philosophy
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source (practitioner angle)
- [[EvalDataCapture]] — capturing production traces to feed the flywheel
- [[EvalPracticePhases]] — Phase 2 where the flywheel begins
