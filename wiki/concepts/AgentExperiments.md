---
title: "Agent Experiments"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-29
---

# Agent Experiments

## Definition

Agent experiments are production A/B tests that compare signal rates (refusals, user frustration, task failure, etc.) between a control group and a group receiving a change (new prompt, model, tool, or agent harness). Introduced by Zubin Koticha of Raindrop, they enable a continuous improvement flywheel where every change is validated against real production behavior rather than just offline evals.

## Key Information

### How They Work

1. Ship a change (new prompt version, model, tool, agent harness modification) to a percentage of users
2. Keep a control group on the existing version
3. Compare implicit and explicit signal rates between groups
4. If issue rates go up, the change is likely a regression; if they go down, it's an improvement

### Example

Shipping "prompt 2.4" reduced user frustration from 37% to 9%, decreased complaints about aesthetics and deployment issues, and increased the average number of tools used — an interesting data point that doesn't necessarily indicate a problem but is valuable context.

### Statistical Relevance

- Starts being useful at a few hundred events — when you can no longer manually read every input and output
- Not always scientifically statistically significant, but practically useful: if user frustration rate goes up, it's worth investigating
- Multiple experiments can run in parallel; compounding effects can be observed

### Implementation Approaches

- **Within Raindrop**: Send metadata flags (experiment version) with traces; Raindrop automatically sets up experiment comparison
- **External**: Use Raindrop's query API to export signal-tagged data to Statsig, BigQuery, or Snowflake for custom experiment analysis
- **PII handling**: Customers run experiments in their own infrastructure, sending only trace data to Raindrop for signal tagging

### Relationship to Evals

The old paradigm (still useful) is evals — ship a change and see how it affects evaluation scores. But nothing replaces seeing what happens in real production. Agent experiments bridge the gap between offline testing and production reality.

## Related

- [[AgentObservability]] — parent concept
- [[ImplicitSignals]] — signals used for comparison
- [[ExplicitSignals]] — signals used for comparison
- [[UserFrustration]] — key signal tracked in experiments
- [[Raindrop]] — platform with built-in experiment support
- [[ZubinKoticha]] — introduced the concept
- [[Statsig]] — experiment analysis integration
- [[BigQuery]] — data export for custom experiment analysis
- [[Snowflake]] — data export for custom experiment analysis
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
