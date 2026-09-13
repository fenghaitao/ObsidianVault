---
title: "Estuary"
type: entity
tags: [project, Meta, content-moderation, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Estuary was Evan King's first substantial project at Meta, named after the point where multiple rivers come together. It was the infrastructure for detecting terrorist content on the platform.

## Key Information

- Built on Hack (Facebook's type-safe PHP) as a backend system
- Designed as a multi-staged funnel: crude quick checks on content to determine if worth further consideration, then expensive models run, photo matching, determination of actions based on scores, human review routing, and final action
- Purpose was to make it easy for the team to experiment: plugging in different models, changing thresholds, running A/B tests
- The name "Estuary" reflects the convergence of multiple detection signals into a single decision pipeline

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Evan King]] — built the project
- [[Meta]] — company where it was built
- [[Content Integrity]] — the org
- [[Realtime Integrity]] — successor team
