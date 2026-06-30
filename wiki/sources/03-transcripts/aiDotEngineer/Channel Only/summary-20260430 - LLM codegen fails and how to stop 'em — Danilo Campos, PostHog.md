---
title: "summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog"
type: source
tags: [source, transcript, ai, agentic-engineering, autonomous-agents, code-generation, posthog, context-engineering, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Core Summary
Danilo Campos, creator of the PostHog Wizard at PostHog, presents six hard-won lessons from building an autonomous coding agent that performs 15,000 successful integrations per month. The Wizard skips "2 hours of misery" and delivers working PostHog integrations in 8 minutes. Campos covers six failure modes and their solutions: model rot (solved by injecting fresh documentation), weird architecture (solved by model airplanes), improvisation at scale (solved by breadcrumbing), human error (solved by inference-time interrogation), security shenanigans (solved by fine-grained tool permissions), and the fundamental insight that code is a depreciating asset while prose gains value with better models.

## Key Points
- **Model Rot**: Models are snapshots of the web from 6-18 months ago. Fast-moving projects become invisible to them. Solution: inject fresh, up-to-date markdown documentation into the agent's context. With large context windows, "you can't beat just shoving a bunch of markdown files into the context and patching the holes."
- **Model Airplanes**: Thin reference implementations (simulacra of real applications) across frameworks and languages that show the correct shape of a PostHog integration. They are token-efficient because they omit non-essential production complexity. The agent references them as patterns to complete integrations consistently.
- **Breadcrumbing**: Progressive task disclosure to limit improvisation. Start by barely mentioning the goal. First: find files with business value (login, Stripe, churn indicators). Then: identify interesting events in those files. Then: list event names and descriptions. Only then: implement PostHog using documentation. This prevents 15,000 different integration styles.
- **Inference-Time Interrogation**: At the stop hook of every run, ask the agent "What could we have done better to set you up for success?" This revealed contradictory MCP tool instructions, missing tools, and language mismatches (JavaScript instructions for Python projects). "If we didn't ask, we wouldn't know."
- **Fine-Grained Tool Permissions**: Early versions read entire .env files, sending secrets to cloud logs. Solution: lock down file access and build a dedicated tool that only checks key presence and writes new values. "You have fine-grained control over tool usage."
- **Code as Depreciating Asset**: Code written today has the same value tomorrow when a better model drops. Prose (markdown, documentation) gains value with better models. The Wizard is 90% markdown files, 8% tools for processing markdown, and 2% agent harness. "Plain text prose is where so much of our value now lives."
- **Agent as Octopus**: Agents are flexible and can maneuver around problems. Don't over-constrain them. Instead, step back, give enough information, and sequence it so the agent does what you want.
- **Implementation**: The Wizard uses the Claude Agent SDK wrapped in a CLI. PostHog covers inference costs via an LLM gateway. Users get free inference by logging into PostHog.

## Related
- [[DaniloCampos]] — speaker, PostHog
- [[PostHog]] — his employer
- [[PostHogWizard]] — the autonomous coding agent product
- [[aiDotEngineer]] — conference
- [[ClaudeAgentSDK]] — SDK used to build the Wizard
- [[Model Rot]] — concept: models become outdated
- [[Model Airplanes]] — concept: thin reference implementations
- [[Breadcrumbing]] — concept: progressive task disclosure
- [[Inference-Time Interrogation]] — concept: asking agents what went wrong
- [[Code as Depreciating Asset]] — concept: code loses value, prose gains it
- [[Agent as Octopus]] — concept: agents are flexible, don't over-constrain
- [[Fine-Grained Tool Permissions]] — concept: security through tool access control
- [[ProgressiveContextDisclosure]] — related context management pattern
- [[ContextEngineering]] — related discipline
- [[Autonomous Coding Agents]] — broader category
- [[AgenticEngineering]] — related paradigm
