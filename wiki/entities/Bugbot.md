---
title: "Bugbot"
type: entity
tags: [tool, cursor, code-review, automation, pr]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md"]
last_updated: 2026-06-26
---

## Definition
Bugbot is Cursor's internal automated code review tool that examines PRs on GitHub, applies rules (such as database constraints), and provides automated review feedback.

## Key Information
- Used internally at Cursor as part of the software factory pipeline
- Reviews PRs and flags violations of team-specific rules
- Example rule: Cursor does not use foreign keys on databases for performance reasons, but models default to adding them — Bugbot catches and flags this
- Part of a multi-stage factory pipeline: plan → produce → review → merge
- Represents the "review" stage of the automated SDLC within Cursor's factory

## Related
- [[Cursor]] — the company using Bugbot internally
- [[SoftwareFactory]] — the factory pipeline Bugbot is part of
- [[Guardrails]] — the category of tool Bugbot represents
- [[AgenticCodeOwners]] — related automated review system at Cursor
- [[EricZakariasson]] — discussed Bugbot in his presentation
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — source
