---
title: "Bot Looping"
type: concept
tags: [ai, agents, workflow, engineering, loops]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition
Bot looping is Vincent Koc's term for a more opinionated and structured approach to agent loops, contrasted with Ralph looping. While Ralph looping involves burning massive tokens in long-running agent sessions and hoping something useful emerges, bot looping applies engineering discipline: structured reward mechanisms, smarter loop design, and intentional human oversight. The name was suggested by another OpenClaw maintainer as a potential new term for the approach.

## Key Information

- **Origin**: Coined during Vincent Koc's 2026 talk, inspired by a suggestion from another OpenClaw maintainer
- **Contrast with Ralph looping**: Ralph looping = "burn tokens for 8 to 9 hours, hoping something happens"; Bot looping = "let's run loops, but let's be a bit more smart about how we do this"
- **Key questions**: "Do we need more than just tokens? What does that reward mechanism look like? How do we get a bit more opinionated?"
- **Implementation context**: Used within Vincent's swim lanes — low-touch lanes run bot loops autonomously; high-touch lanes involve conversation and guidance
- **Philosophy**: 2026 is about "not wasting tokens" — bot looping represents the shift from brute force to structured engineering
- **Not yet formalized**: Presented as an emerging concept — "Maybe we'll coin it"

## Related
- [[summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator
- [[Ralph Loop]] — the approach bot looping improves upon
- [[Swim Lanes]] — the parallel workstream pattern where bot loops run
- [[Dark Factory]] — the overarching concept
- [[Token Efficiency]] — the 2026 shift bot looping represents
- [[Token Maxing]] — the 2025 approach bot looping moves beyond
- [[AgentLoop]] — the general concept of agent loops
- [[OpenClaw]] — the project context
