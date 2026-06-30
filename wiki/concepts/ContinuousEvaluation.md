---
title: "Continuous Evaluation"
type: concept
tags: [evaluations, observability, agents, monitoring, devops]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Continuous evaluation is the practice of running evaluations throughout the entire agent lifecycle — from early development through production — rather than treating evaluation as a one-time gate before deployment. It ensures agents don't drift from requirements as models, prompts, environments, and customer behavior change over time.

## Key Information

### Why Continuous Evaluation
- Agents are non-deterministic and drift over time
- Models change (updates, swaps for cost optimization)
- Prompts evolve
- Customer behavior shifts
- New edge cases emerge
- Requirements change

### Three Observability Phases (Microsoft Foundry)

**Phase 1: Early Build Stage**
- Build observability in from the very start, not as an afterthought
- Evaluate at multiple points: intent resolution → tool calls → overall response
- Start with portal for quick prototyping with built-in metrics
- Use tracing to understand agent behavior during development

**Phase 2: Debug and Optimize in Production**
- Continuous evaluations triggered by code changes
- Scheduled evaluations running on regular cadences
- Red teaming for ongoing security assessment
- Pull in cloud monitoring data (Azure Monitor) for correlation
- Trace-linked evaluations for rapid issue diagnosis

**Phase 3: Fleet-Wide Management (Future)**
- Centralized observability across many agents and multi-agent systems
- Understanding the full fleet within a business
- Agents built anywhere, observed centrally in Foundry

### Types of Continuous Evaluation
- **Code-triggered**: Run evals automatically when agent code changes
- **Scheduled**: Regular eval runs on production traffic
- **Adversarial**: Ongoing red teaming to catch new vulnerabilities
- **Operational**: Pull in infrastructure and data monitoring alongside agent metrics

### The Optimize Loop
- Evaluate → detect gap → diagnose (trace-linked) → fix → re-evaluate → compare
- Every change (model swap, prompt update, tool change) should trigger immediate re-evaluation
- Check for regressions: did cost drop but accuracy also drop?
- The Observe Skill automates this loop with a coding agent

## Related
- [[AgentObservability]] — broader framework
- [[EvalEngineering]] — evaluation methodology
- [[EvalFlywheel]] — production-to-offline eval feedback loop
- [[TraceLinkedEvaluations]] — linking evals to traces for diagnosis
- [[ObserveSkill]] — automated continuous evaluation loop
- [[OnlineEvals]] — evaluation of production traffic
- [[OfflineEvals]] — evaluation during development
- [[Microsoft Foundry]] — platform with built-in continuous evaluation
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
