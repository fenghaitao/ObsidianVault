---
title: "Code as Depreciating Asset"
type: concept
tags: [ai, software-engineering, paradigm, prose, documentation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
"Code as a depreciating asset" is the observation that code written today has the same or declining value when a better model drops tomorrow, while prose (markdown, documentation, instructions) gains value because better models can do more with well-written text. This inverts the traditional engineering value hierarchy where writing code was the primary value-generating activity.

## Key Information
- Articulated by Danilo Campos (PostHog) based on experience building the PostHog Wizard
- Code has always been a depreciating asset: it ships with tech debt and requires ongoing maintenance
- With AI models improving rapidly, code's value is further diminished because tomorrow's model could generate better code from the same prose
- Prose gains value: when a better model drops, it can take well-written documentation and produce even better results
- The PostHog Wizard is 90% markdown files, 8% tools for processing markdown, and 2% agent harness — demonstrating that prose is the primary value carrier
- "Our whole careers, we have been rewarded by writing the code... That is not the world that we live in anymore"
- Implication: invest in writing great prose (documentation, instructions, guardrails) rather than over-engineering agent scaffolding
- Related to but distinct from "Code is Free" (Ryan Lopopolo) — Campos focuses on the relative value trajectory of code vs. prose over time

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — articulated the concept
- [[PostHogWizard]] — product demonstrating this principle
- [[Code is Free]] — related concept by Ryan Lopopolo
- [[Code as Disposable Build Artifact]] — related paradigm
- [[Harness Engineering]] — discipline built on this premise
- [[AgentHarnessSeparation]] — related architectural principle
