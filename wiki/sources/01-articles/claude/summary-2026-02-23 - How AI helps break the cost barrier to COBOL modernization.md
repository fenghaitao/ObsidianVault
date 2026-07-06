---
title: "summary-2026-02-23 - How AI helps break the cost barrier to COBOL modernization"
type: source
tags: [source, cobol, legacy-modernization, claude-code]
sources: ["raw/01-articles/claude/2026-02-23 - How AI helps break the cost barrier to COBOL modernization.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic argues AI flips the economics of COBOL modernization — historically stalled because understanding decades-old legacy code cost more than rewriting it — by automating the exploration/discovery and documentation phases that used to require armies of consultants over years, compressing timelines to quarters.

## Key Points

- **Scale of the problem**: COBOL handles an estimated 95% of US ATM transactions; hundreds of billions of lines run daily in finance, airlines, and government, while the engineers who understand it retire faster than they're replaced (taught at only a handful of universities).
- **Why COBOL modernization differs from typical refactoring**: it's reverse-engineering business logic from decades-old systems and untangling dependencies that now exist only in the code itself, with institutional knowledge long departed.
- **What Claude Code automates**: reads the entire codebase to map program entry points, execution paths, data flows across modules, and hidden dependencies (shared data structures, file-based coupling, initialization sequences) that don't surface in static analysis — the exact dependencies that make migration risky if missed.
- **Risk assessment from the mapping**: highly-coupled modules flagged as risky; isolated components surfaced as early/independent migration candidates; duplicated logic flagged for refactoring; accumulated technical debt documented before it becomes a migration surprise.
- **Human judgment stays essential**: COBOL engineers bring regulatory, business-priority, and risk-tolerance context AI cannot supply — used for planning and validation-criteria decisions before any code changes.
- **Execution approach**: one component at a time with validation at each step — AI translates COBOL logic to modern languages, wraps legacy components staying in place with API shims, and runs old/new code side-by-side during transition, so failures stay small and correctable rather than risking a mass rollback.
- **Recommended starting point**: a single component/workflow with clear boundaries and moderate complexity, analyzed and documented thoroughly, planned with engineers, implemented incrementally, and validated carefully.

## Related

- [[ClaudeCode]] — the tool automating COBOL exploration and analysis
- [[AgenticCoding]] — the broader agentic-coding practice this modernization approach exemplifies
