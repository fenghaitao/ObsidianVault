---
title: "Model Airplanes"
type: concept
tags: [agents, code-generation, patterns, reference-implementations, context-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
Model airplanes are thin reference implementations — simulacra of real applications — that demonstrate the correct shape of an integration across multiple frameworks and languages. They are token-efficient because they omit non-essential production complexity while preserving the structural pattern the agent needs to replicate.

## Key Information
- Introduced by Danilo Campos and the PostHog Wizard team
- Named after model airplanes: scaled-down versions that capture the essential shape without full functionality
- Example: a login page where authentication doesn't actually work (any password is accepted), but the "auth is auth-shaped" — the structure is correct
- The agent sees the pattern and knows where to place event tracking (e.g., login events, identity tracking)
- Maintained across multiple frameworks and languages as a fleet
- Flattened into a single markdown file and included as a reference in skill files
- More token-efficient than full production applications because non-essential complexity is stripped out
- Enables the agent to complete integrations consistently every time by providing a correct pattern to follow
- Contrasts with giving the agent no reference, which leads to weird architectural decisions from models trained on diverse, uneven codebases

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — introduced the concept
- [[PostHogWizard]] — product that uses model airplanes
- [[PostHog]] — company
- [[Breadcrumbing]] — complementary technique for limiting improvisation
- [[FewShotExamples]] — related concept in prompt engineering
- [[ContextEngineering]] — broader discipline
