---
title: "Hyrum's Law"
type: concept
tags: [API, software-engineering, compatibility, law]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Hyrum's Law states that with enough users, every observable behavior of a system — even unintended implementation details — will be relied on by somebody and therefore effectively part of the API. The transcript garbles it as "Hyram's law".

## Key Information
- Charlie's paraphrase: "any implementation detail in your software... someone eventually becomes to rely on that," so even things not encoded as behavior become part of your API whether you like it or not.
- Practical consequence for automated rewrites: even if your whole test suite passes, implicit behaviors may have changed, and those regressions get pushed onto users to discover and report.
- This is Charlie's main concern with agent-driven, whole-codebase rewrites (like Bun's Zig-to-Rust transplant), distinct from whether one "trusts the models" to produce correct code.

## Related
- [[Bun]] — the rewrite example where the risk shows up
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
