---
title: "Scaffolding Pattern"
type: concept
tags: [refactoring, migration, patterns, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
The scaffolding pattern is a migration strategy where temporary code allows old and new systems to coexist during a large-scale refactor, enabling incremental validation of each migrated component before the scaffolding is removed at the end.

## Key Information
- Used when migrating between frameworks, state management systems, or API versions where a big-bang cutover is impractical.
- Scaffolding is intentionally ugly and temporary — not something you would want in production long-term.
- Enables testing the full application as each individual component gets migrated.
- Parallel agents can work on different components simultaneously, each validating their work against the running application.
- Once all components are migrated, all scaffolding is ripped out, leaving only the new system.
- Example: OpenHands migrated from Redux to Zustand by having an agent set up scaffolding allowing both state managers to coexist, then dispatching parallel agents for each component, and finally removing all Redux references.
- Provides human feedback at each step: as each agent finishes a component, the human can validate the application still works.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Task Decomposition]] — related decomposition strategy
- [[Agent Orchestration]] — broader practice
- [[Redux]] — example source system
- [[Zustand]] — example target system
- [[OpenHands]] — platform using this pattern
