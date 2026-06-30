---
title: "ContextDevelopmentLifeCycle"
type: concept
tags: [context, context-engineering, devops, methodology, lifecycle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
The Context Development Life Cycle (CDLC) is a paradigm introduced by Patrick Debois that applies software engineering rigor to context management. Modeled after the DevOps infinity loop, it consists of five phases: Generate → Test → Distribute → Observe → Adapt. The CDLC treats context (prompts, skills, instructions, documentation) as the primary artifact of AI-assisted software development, with code as a generated output.

## Key Information
- Introduced by Patrick Debois (DevOps pioneer) at the AI Engineer conference
- Draws a direct parallel to the DevOps movement: "In 2009, I asked what if ops looked more like dev? Now I ask: what if context is the code?"
- Five phases:
  - **Generate**: Creating context through prompting, reusable instructions, library documentation, MCP sources, and spec-driven development
  - **Test**: Validating context through linting, comprehension checks, LLM-as-judge evaluations, and end-to-end agent tests
  - **Distribute**: Sharing context via repo check-ins, packages, registries, and dependency management
  - **Observe**: Getting feedback from agent logs, PR reviews, and production instrumentation
  - **Adapt**: Using feedback to optimize and regenerate context, running evals in CI/CD with error budgets
- The CDLC recognizes that LLM outputs are non-deterministic, requiring statistical approaches to testing (run N times, measure success rate)
- Scales across three levels: individual (solo crafting), team (shared reflex), and organizational (cross-team flywheel)

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[PatrickDebois]] — introduced the concept
- [[ContextAsCode]] — the core paradigm shift
- [[ContextTesting]] — the Test phase
- [[ContextDistribution]] — the Distribute phase
- [[ContextObservability]] — the Observe phase
- [[ContextFeedbackLoop]] — the Adapt phase
- [[NonDeterministicTesting]] — key testing consideration
- [[ErrorBudgetsForContext]] — CI/CD approach for non-deterministic tests
- [[Harness Engineering]] — related paradigm from Ryan Lopopolo
- [[ContextEngineering]] — related discipline from Andrej Karpathy
- [[Software Development Life Cycle]] — the code equivalent the CDLC parallels
