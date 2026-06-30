---
title: "Behavior-Driven Development (BDD)"
type: concept
tags: [testing, specification, cucumber, executable-specifications, agent-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

Behavior-Driven Development (BDD) is a development practice where product behavior is described in human-readable, executable specifications. It provides an intermediate layer between spec-driven development and validation, producing specifications that are both readable by humans and executable as tests.

## Key Information

- Spec-driven development describes how something should work, but does not validate that the product actually adheres to the spec
- BDD fills this gap: specifications are written in a human language (Gherkin syntax with Cucumber) and are both readable and executable
- "One thing harder than reading AI code is reading AI tests" — BDD scenarios are easier to review than average test code
- Scenarios connect directly to PRDs and critical user journeys, providing traceability from requirements to validation
- Cucumber is the primary tool: almost forgotten but suddenly useful again in the AI era
- The language is flexible — there are multiple ways to write features, but they all describe how to go through the application, why things exist, and how they run
- BDD closes the loop that spec-driven development leaves open: you have a spec (what should happen) and executable validation (does it actually happen)
- For agents: BDD features can refer back to all governing documents (ADRs, PRDs) about why things exist

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[Cucumber]] — the tool used to implement BDD
- [[Executable Specifications]] — the output of BDD
- [[SpecificationDrivenDevelopment]] — the paradigm BDD complements by closing the validation loop
- [[PRD (Product Requirements Document)]] — BDD scenarios connect to PRDs
- [[Architecture Decision Record (ADR)]] — BDD features can reference ADRs
- [[Decision Capture Loop]] — BDD is part of the broader reinforcement loop
