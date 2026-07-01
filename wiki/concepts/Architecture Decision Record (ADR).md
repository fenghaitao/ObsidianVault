---
title: "Architecture Decision Record (ADR)"
type: concept
tags: [architecture, documentation, decision-capture, enforcement, agent-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

An Architecture Decision Record (ADR) is a text document that records why an architectural decision was made and how it is enforced in the codebase. It captures the reasoning behind structural choices and links to the enforcement mechanisms that prevent violations.

## Key Information

- ADRs are a concept, not a single format — they are text documents with no specific required structure
- Each ADR covers: why a decision was made, how it is enforced, and which files/modules it concerns
- Examples include reference docs and code snippets to illustrate the rule
- Example: split code in layers to prevent N+1 queries; enforce by linting imports in modules; also enforce that database reads return plain shapes instead of ORM objects to prevent duplication
- ADRs require a tool to enforce the rule — the tool flags violations and links back to the ADR so the agent can understand why the rule exists and how to fix the issue
- For AI agents: when a commit is rejected by a lint rule, the agent follows the link to the ADR, reads why the rule exists, and learns how to fix the violation
- A mature codebase may have 50+ ADRs defining the architecture of the product

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[PRD (Product Requirements Document)]] — complementary decision record for product features
- [[BehaviorDriven Development (BDD)]] — complementary approach for executable specifications
- [[Architecture Enforcement]] — the enforcement mechanism ADRs describe
- [[Decision Capture Loop]] — the reinforcement loop that uses ADRs
- [[Enforce Dont Instruct]] — related principle
- [[SpecificationDrivenDevelopment]] — related paradigm
