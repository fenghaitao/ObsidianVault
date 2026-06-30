---
title: "Breadcrumbing"
type: concept
tags: [agents, context-engineering, prompt-engineering, task-decomposition, progressive-disclosure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
Breadcrumbing is a progressive task disclosure technique for autonomous coding agents where the agent is guided step by step through a task without being told the full goal upfront. Each step reveals just enough information to reach the next step, preventing improvisation and ensuring consistent outcomes at scale.

## Key Information
- Introduced by Danilo Campos (PostHog) for the PostHog Wizard
- Motivation: with 15,000 integrations per month, an agent might find 15,000 different ways to integrate, creating an unmanageable support burden ("sorcerer's apprentice stuff")
- The technique avoids telling the agent the full plan upfront, which can cause it to rush through early steps and get "rock polishy" on later ones
- PostHog's breadcrumbing sequence for integration:
  1. Find files with business value (login, Stripe, churn indicators) — don't mention PostHog
  2. Identify interesting events in those files — don't write code yet
  3. List event names and descriptions — save to a file
  4. Now implement PostHog using documentation loaded by framework/language
- Business logic "casts a huge shadow in code," making it reliably detectable
- By the time the agent reaches implementation, it has carefully thought about what events matter and has the right documentation loaded
- Results in modifications that are "not stupid" and users are "not mad about it"
- Related to progressive disclosure and incremental disclosure patterns but specifically applied to task sequencing for autonomous agents

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — introduced the concept
- [[PostHogWizard]] — product that uses breadcrumbing
- [[ProgressiveContextDisclosure]] — related context management pattern
- [[IncrementalDisclosure]] — related pattern
- [[ProgressiveDisclosure]] — related server-side pattern
- [[Task Decomposition]] — broader concept
- [[Model Airplanes]] — complementary technique
- [[ContextEngineering]] — broader discipline
