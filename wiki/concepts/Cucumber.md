---
title: "Cucumber"
type: concept
tags: [testing, bdd, tool, executable-specifications, agent-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

Cucumber is a Behavior-Driven Development (BDD) tool that parses human-readable feature specifications (written in Gherkin syntax) and executes them as automated tests through step definitions mapped to code. Almost forgotten, it has become suddenly useful again in the AI era.

## Key Information

- Cucumber enables executable specifications: feature files describe behavior in human language, step definitions map those descriptions to code
- "Almost forgotten, suddenly useful again" — the AI coding era has revived interest because BDD scenarios are easier to review than AI-generated test code
- Scenarios can be connected directly to PRDs and critical user journeys for traceability
- The language (Gherkin) is flexible — there are multiple ways to write features, giving teams freedom in how they describe behavior
- Features describe: how to go through the application, why things exist, and how they run
- Features can refer back to all governing documents (ADRs, PRDs) about why things exist
- In the Decision Capture Loop, Cucumber-based BDD tests are enforced via architecture linting — for example, end-to-end BDD test suites cannot access database modules, ensuring tests only use browser features

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[Behavior-Driven Development (BDD)]] — the practice Cucumber implements
- [[Executable Specifications]] — what Cucumber produces
- [[Decision Capture Loop]] — the reinforcement loop Cucumber tests participate in
- [[Architecture Enforcement]] — how Cucumber test suites are constrained (e.g., no database access)
- [[SpecificationDrivenDevelopment]] — paradigm that BDD/Cucumber validates
