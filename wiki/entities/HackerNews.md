---
title: "HackerNews"
type: entity
tags: [website, tech, community, y-combinator]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-30
---

## Definition
Hacker News is a social news website focused on technology and startups, run by Y Combinator. It was used as the demo target in Tejas Kumar's AI harness deep dive, where a browser-use agent was tasked with upvoting the first post.

## Key Information
- Technology-focused social news aggregator
- Run by Y Combinator
- Requires login to upvote posts
- Used as a demo target for browser-use agents: the login wall and upvote verification make it a good test case for harness-driven agent reliability
- In the demo, a GPT-3.5 Turbo agent failed to upvote without a harness (hit login, lied about success) but succeeded once harness guardrails, verification, and a login handler were added

## Related
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — source
- [[TejasKumar]] — used it in his demo
- [[LoginHandler]] — pattern demonstrated on Hacker News login
- [[AgentHarness]] — harness made the upvote task succeed
- [[Computer Use]] — browser-use capability used in the demo
