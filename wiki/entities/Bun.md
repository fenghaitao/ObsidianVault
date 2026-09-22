---
title: "Bun"
type: entity
tags: [tool, runtime, JavaScript, Zig, Rust]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Bun is a JavaScript/TypeScript runtime and toolkit (originally written in Zig) whose agent-driven rewrite to Rust is discussed at length in the episode.

## Key Information
- The episode references an attempt to "transpile" Bun from Zig to Rust "all in one go" using agents, discussed as a test of the envelope of what's possible.
- At recording time, founder Jared Sumner had not yet published the accompanying blog post (Charlie jokes the post is taking longer than the rewrite).
- From the PR, the rewrite appeared to have distinct phases per file with validation, but Charlie doubts a human read significant amounts of the resulting code.
- Charlie's concern: an automated rewrite trades known issues for new unknown ones; even a passing test suite hides implicit behavior (Hyrum's Law), so bugs get pushed onto users.
- Astral has no plans to do the same for its own projects; Charlie is "glad they're experimenting" but notes they are criticized for it.

## Related
- [[Zig]] — the language Bun is being rewritten from
- [[Rust]] — the language it is being rewritten to
- [[Hyrum's Law]] — why a green test suite isn't enough
- [[Contributor Poker]] — the contributor dynamic agent PRs upset
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
