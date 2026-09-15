---
title: "Core Data"
type: entity
tags: [technology, framework, Apple, iOS, database]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Definition

Core Data is Apple's ORM/persistence database framework for iOS and macOS applications.

## Key Information

- Adam Ernst calls it "great" for small teams (e.g., a two-engineer startup) that need a lightweight way to store data.
- "Falls over completely" at the scale Facebook's iOS team reached after the native rewrite (growing from ~15-20 to 100-200 engineers).
- Facebook's native rewrite initially launched on Core Data, but the mobile team concluded it would "fall over tomorrow" and had to replace it incrementally.
- Adam Ernst's E6 project replaced it with an immutable model system ("mem models") that made thread safety and mutations easier to reason about.
- To convince skeptical iOS engineers, his team disassembled Core Data's closed source to understand (and explain) why it was slow to initialize.

## Related

- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[Adam Ernst]] — led the replacement project
- [[Apple]] — vendor of the framework
- [[Meta]] and [[Facebook]] — the company context of the replacement
- [[ComponentKit]] — another Apple-platform technology that diverged from Apple defaults
