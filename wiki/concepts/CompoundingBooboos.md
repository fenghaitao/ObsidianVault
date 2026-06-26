---
title: "CompoundingBooboos"
type: concept
tags: [agents, errors, code-quality, technical-debt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
"Compounding booboos" is Mario Zechner's term for how AI agents accumulate errors in a codebase. Unlike humans who feel pain and act on it (quit, blame, refactor), agents happily keep dumping garbage into the codebase with zero learning, no bottlenecks, and delayed pain for the humans who must eventually deal with it.

## Key Information
- Mario Zechner: "Agents are actually compounding booboos, which is my word for errors, with zero learning and no bottlenecks and delayed pain. The delayed pain is for you."
- Agents have no learning mechanism — they repeat the same mistakes
- No bottlenecks: agents can generate far more code than humans can review
- Delayed pain: the consequences of agent-generated complexity are not felt immediately
- Humans feel pain and have options: quit, blame someone else, or band together to refactor — agents don't
- "Agents will happily keep [dumping garbage] into your code base"
- The "ouroboros" problem: review agents reviewing agent code doesn't work — it catches some issues but not enough
- Models learn complexity from internet garbage (90% of code on the internet is old garbage)
- Every agent decision is local, especially when the codebase doesn't fit in context
- Result: enterprise-grade complexity within 2 weeks with just 2 humans and 10 agents

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[MarioZechner]] — originator of the term
- [[SlowingDownWithAgents]] — the prescription
- [[AgentCodeReviewLimitations]] — the ouroboros problem
- [[GoodAgentTasks]] — what tasks are suitable for agents
- [[Slop]] — related concept of low-quality generated code
- [[CodeSlop]] — related
