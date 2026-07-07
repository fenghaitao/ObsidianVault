---
title: "Just-in-Time Planning"
type: concept
tags: [engineering-management, planning, agile, agentic-coding]
sources: ["raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md"]
last_updated: 2026-07-07
---

## Definition

Just-in-Time (JIT) Planning is a software planning methodology for AI-native engineering orgs that sizes planning effort to match the accelerated pace of AI-assisted development. Analogous to JIT compiling, it means doing just the right amount of planning at the right time — shifting away from long-range roadmaps and pre-code design docs toward discussions in PRs and prototypes.

## Key Information

- Originated on the [[ClaudeCode]] engineering team at [[Anthropic]], introduced by [[FionaFung]] after she joined the team and found a six-month roadmap was out of date by month three due to Claude Code's own acceleration of development speed.
- **Core principle:** "Building is cheap, arguing is expensive" — settle technical debates by generating competing PR versions rather than whiteboarding, comparing not just implementation approaches but downstream impact on callers.
- **Replaces design docs with PRs and prototypes:** Most discussions now happen via code rather than pre-code design documents, except where async cross-team alignment still needs one.
- **Product reviews minimized:** The process is "let's prototype, get a lot of internal users on it, and start acting on their feedback" rather than lengthy product review cycles.
- **Complements [[ExplorePlanCodeCommit|Plan Mode]]:** JIT planning sits above the individual EPCC workflow as a team-level planning philosophy — how the team decides what to build and at what level of detail, before individual engineers enter Plan Mode for implementation.
- Enables the team to stay responsive in fast-moving spaces where long-range roadmaps become stale quickly.

## Related

- [[summary-2026-06-03 - Running an AI-native engineering org]] — the blog article source
- [[summary-13 - Running an AI-native engineering org]] — the San Francisco transcript
- [[summary-03 - Running an AI-native engineering org]] — the London transcript
- [[AINativeEngineeringOrg]] — the broader organizational framework
- [[FionaFung]] — the engineering leader who introduced JIT planning
- [[ExplorePlanCodeCommit]] — the individual-level workflow whose planning phase JIT planning redefines at the team level
- [[ClaudeCode]] — the tool that enables the prototyping velocity making JIT planning viable
- [[AgenticCoding]] — the paradigm shift that necessitated new planning approaches
- [[Anthropic]] — the company
