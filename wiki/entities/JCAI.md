---
title: "JCAI"
type: entity
category: product
tags: [ai, agent, web-agent, browser-automation, predecessor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
JCAI was a web agent built in 2023 by the Viktor founding team as their first attempt at building AI employees. It was state-of-the-art on the WebArena benchmark and operated by taking DOM snapshots, minifying them in a lossless way, and deciding on the next action (type, click, etc.) based on the snapshot and goal.

## Key Information

- **Created**: 2023, after ChatGPT launched, before tool calling and code-generating models were available
- **Approach**: Browser-based web agent — browsers as universal interfaces since most apps have browser versions
- **Architecture**: Took DOM snapshots → lossless minification → decision on next step (type in search bar, click login button, etc.)
- **Reliability**: Worked for 3-5 steps at ~60% reliability; compounding errors with each step made it impractical as a product
- **State of the art**: Top-performing web agent on the WebArena benchmark at the time
- **Limitations**: Speed issues (waiting a minute only to fail) and reliability prevented it from becoming a useful product
- **Legacy**: The team's learnings from JCAI informed the evolution to Jace (email agent) and ultimately Viktor (AI employee)
- **The team still believes web agents are amazing**: "they're finally working much better than in the past"

## Related

- [[Viktor]] — successor AI employee platform
- [[Jace]] — successor email agent
- [[Fryderyk Wiatrowski]] — co-founder who built JCAI
- [[Web Agent]] — category of browser-based AI agents
- [[WebArena]] — benchmark where JCAI was state-of-the-art
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
