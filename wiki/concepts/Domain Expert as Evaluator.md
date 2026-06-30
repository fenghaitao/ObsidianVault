---
title: "Domain Expert as Evaluator"
type: concept
tags: [domain-expertise, ai-quality, organizational-design, evaluator, metrics, data-science]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs.md"]
last_updated: 2026-06-30
---

## Definition
The Domain Expert as Evaluator is the second of three models in Chris Lovejoy's framework for incorporating domain expertise into AI organizations. In this model, the domain expert defines how to measure quality — what metrics matter, what you're optimizing for — and builds a measurement system, while engineers make the actual improvements based on that data.

## Key Information
- **Split responsibility**: The domain expert defines quality and builds measurement systems; engineers make the improvements
- **Assessment complexity**: More sophisticated than Oracle — involves defining metrics, building review dashboards, setting up evaluation pipelines
- **Measurement approaches**: User metrics (customer feedback as north star), hired reviewer teams (clinicians reviewing subsets of outputs), [[LLM-as-Judge]], or combinations
- **Best when**: Quality can be measured objectively, and manual iteration by engineers is fast enough
- **When not to use**: When quality is subjective (taste-based), or when manual iteration is too slow for the scale
- **Required skills**: Domain expertise + data science intuition, statistical skills, industry connections (for hiring review teams), leadership, product management experience
- **Progression path**: Typically evolves from Oracle when the organization outgrows one person's review capacity and objective metrics exist

### Case Study
- **[[Anterior]]**: Evolved from Oracle to Evaluator when one person couldn't review all outputs. [[ChrisLovejoy]] defined metrics and failure modes, built a review dashboard, hired clinicians for reviews, and collaborated with engineering using the resulting performance data.

## Related
- [[Domain Expert as Oracle]] — previous model (direct embedding)
- [[Domain Expert as Architect]] — next model (self-improving systems)
- [[Domain Expertise]] — the core capability
- [[Domain Native AI Organization]] — the organizational philosophy
- [[Principal Domain Expert]] — recommended organizational role
- [[AI Quality]] — what the Evaluator defines and measures
- [[LLM-as-Judge]] — one measurement approach
- [[EvalEngineering]] — related discipline
- [[Anterior]] — Evaluator model case study
- [[ChrisLovejoy]] — framework creator
- [[summary-20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs]] — source talk
