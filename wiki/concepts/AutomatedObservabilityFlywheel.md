---
title: "AutomatedObservabilityFlywheel"
type: concept
tags: [observability, evals, experimentation, automation, arize, flywheel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Definition
The Automated Observability Flywheel is Arize's vision for fully automating the AI quality lifecycle: observability (understanding what agents do), evals (deriving signal), and experimentation/improvement (making changes). The goal is for AI to handle all three stages — creating evals on the fly, detecting changes that need new evals, and continuously monitoring — so that users can "pull the ecosystem down and it just works."

## Key Information

### The Three-Stage Flywheel
1. **Observability**: Traces, spans, sessions, and distributional views to understand what agents are doing
2. **Evals**: Deriving signal through LLM-as-judge, human feedback, golden datasets, deterministic evals, and business metrics
3. **Experimentation & Improvement**: Datasets from failing traces → controlled experiments → prompt/model/orchestration/config changes → repeat

### Automation Vision
- Arize's ultimate goal is to automate users out of the process entirely
- "It's not magic, but it should feel like magic"
- **Alex** (Arize's AI assistant): Can be invoked to analyze issues — "Hey, do you see any issues with my application?" — and then plans and runs tasks autonomously
- Alex can detect high latency, errors, and other issues from trace data
- AI should create evals on the fly based on context of traces and what's happening
- When something changes, the AI should know it needs a new eval and create one
- All primitives are exposed via CLI and tools/skills so external coding agents (Claude Code, Codex) can drive the system programmatically
- "Software will compress" — building and customizing will get easier, and dashboards/buttons will give way to programmatic and agentic interfaces

### Why Automate?
- Most people don't want to live in dashboards or do manual things
- People are comfortable with their coding agents (Claude Code, Codex)
- The whole flywheel is "very much automatable" — observability data feeds evals, eval results feed experiments, experiments produce improvements
- Continuous monitoring and automated response is the end state

## Related
- [[DatNgo]] — speaker who described this vision
- [[Arize]] — company building this flywheel
- [[AlexArizeAgent]] — Arize's AI assistant that automates the flywheel
- [[AgentObservability]] — stage 1 of the flywheel
- [[AgentExperiments]] — stage 3 of the flywheel
- [[LLMAsJudge]] — key eval technique in the flywheel
- [[EvalScopes]] — eval taxonomy used in the flywheel
- [[AgentDistributionalView]] — observability technique feeding the flywheel
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
