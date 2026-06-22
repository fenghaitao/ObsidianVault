---
title: "ComprehensionDebt"
type: concept
tags: [code-quality, maintenance, arvid-kahl]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260119 - Arvid Kahl's SaaS is 98% Coded by Claude.md]
last_updated: 2026-06-22
---

## Definition

Comprehension debt is the gap that grows between a developer's mental model of their codebase and the actual code when AI writes the vast majority of it. Coined by Arvid Kahl, it describes the risk of losing understanding of your own product when you stop writing code yourself.

## Key Information

- When 98% of code is AI-written, your understanding drifts away from the actual codebase.
- Arvid's mitigation: steps through every Git change manually to maintain his mental model.
- "The agentic coding system does not retain the theory" — Claude builds a temporary theory, does its work, then moves on. The human must maintain the permanent theory.
- Even for one-line fixes, Arvid prefers asking Claude rather than editing manually — Claude knows all locations where a change applies.
- "Super delayed TDD": writes tests days after deploying to catch comprehension gaps.
- Related to the "theory of coding": don't interfere manually mid-session; let Claude finish with its internal representation intact.

## Related

- [[ArvidKahl]] — originator
- [[Podscan]] — the product
- [[ClaudeCode]] — the coding agent
- [[SpecDrivenDevelopment]] — the methodology
- [[ContextRot]] — related concept from Cole Medin
