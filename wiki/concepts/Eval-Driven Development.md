---
title: "Eval-Driven Development"
type: concept
tags: [eval, tdd, development, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Eval-driven development is the practice of writing evaluation tests for an AI agent before building the feature itself, analogous to test-driven development (TDD) in traditional software engineering. The eval serves as a capability eval and a "hill to climb" for the agent.

## Key Information
- Direct analog to test-driven development: write the test first, then build the feature to pass it
- Example: if you want an agent to always verify customer identity before processing a refund, write an eval that checks for that first
- The eval becomes a capability eval — a measurable target for the agent to reach
- In practice, Anthropic used this approach with Claude Code: built capability evals for desired features, gave Claude Code targets to hit
- When new models dropped, they'd run the eval suite and immediately see which bets paid off
- Like TDD, widely acknowledged as good practice but less commonly implemented
- Key benefit: forces explicit definition of what "good" looks like before development begins
- Requires stakeholder involvement to define success criteria upfront

## Related
- [[Capability Evals]] — the eval type used in eval-driven development
- [[Code Evals]] — can be used for eval-driven development
- [[LLM-as-Judge]] — can be used for eval-driven development
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
