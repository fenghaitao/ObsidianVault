---
title: "Hoarding Things You Know How To Do"
type: concept
tags: [career-advice, software-engineering, knowledge-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s long-standing career-advice principle, newly supercharged by AI: build value by accumulating a large personal backlog of small techniques, tools, and verified experiments you've tried, so that when a new problem appears you can recognize and combine relevant prior solutions others wouldn't think to connect.

## Key Information

- Pre-AI version: over a career, Willison collected small bits of experience (e.g., "used Redis for an activity inbox in 2015," "did rate limiting with node.js in 2017") which he could later combine in novel ways nobody else would think to, since nobody else had that exact combination of prior experience.
- AI makes this dramatically cheaper: a quick prototype of an unfamiliar library/technique now costs almost nothing to produce, so the backlog can grow much faster.
- Concretely implemented via two public GitHub repositories: `simonw/tools` (~193 small HTML/JavaScript tools, each capturing one proven capability) and `simonw/research` (AI-driven research write-ups — always with actual code that was run and verified, not just unverified "deep research" text, since that's what makes them reusable rather than "LLM vomit").
- Usage pattern: point a coding agent directly at the accumulated backlog ("check out simonw/research and look at the WebAssembly/Rust examples, then use that to solve this new problem") — modern coding agents are very good at searching large stores of prior context to find just the relevant pieces, removing the old constraint of limited context windows.
- Willison defaults to making this backlog public (better for findability, career credibility, and free permanent backup via GitHub) but also maintains private repos and ~10,000 Apple Notes for things that don't fit the public pattern.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — originates and practices this principle
- [[Agentic Engineering]] — broader discipline this technique supports
