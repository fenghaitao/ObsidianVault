---
title: "Executable Specifications"
type: concept
tags: [bdd, testing, cucumber, specification, validation, agent-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

Executable specifications are human-readable descriptions of product behavior that can also be executed as automated tests. They close the validation gap in spec-driven development by providing a verifiable link between what the spec says should happen and what the code actually does.

## Key Information

- Spec-driven development describes how something should work, but does not validate that it actually does — executable specifications fill this gap
- Implemented via BDD tools like Cucumber: feature files are written in human language (Gherkin), parsed by step definitions, and executed as code
- "One thing harder than reading AI code is reading AI tests" — executable specifications are easier to review than traditional test code
- They are both readable and executable, making them suitable for human review and automated validation
- Scenarios connect directly to PRDs and critical user journeys, providing end-to-end traceability
- The language is flexible — teams choose how to write features
- Features can reference all governing documents (ADRs, PRDs) about why things exist
- In the Decision Capture Loop, executable specifications are part of the automated enforcement: for example, BDD end-to-end tests are constrained to only use browser features (no database access)

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[BehaviorDriven Development (BDD)]] — the practice that produces executable specifications
- [[Cucumber]] — the tool for creating executable specifications
- [[SpecificationDrivenDevelopment]] — the paradigm that executable specifications validate
- [[Decision Capture Loop]] — the enforcement loop that runs executable specifications
- [[Architecture Enforcement]] — how executable specification suites are constrained
