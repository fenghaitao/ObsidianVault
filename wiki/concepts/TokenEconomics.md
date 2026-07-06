---
title: "TokenEconomics"
type: concept
tags: [concept, google, cost, vibe-coding, agentic-engineering]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good).md"
last_updated: 2026-07-06
---

## Definition

Token economics is [[Google]]'s CapEx-vs-OpEx framing (via its agentic-engineering masterclass, per [[ColeMedin]]) for the cost tradeoff between [[VibeCoding]] and [[AgenticEngineering]]. Vibe coding is cheap to start but expensive to run; agentic engineering is expensive to start but cheap to run.

## Key Information

### The tradeoff

| | Capital expenditure (upfront) | Operational expenditure (ongoing) |
|---|---|---|
| [[VibeCoding]] | Low — no harness/spec design needed | High — burns large volumes of tokens iterating on unreliable ("slop") code because there's no system enforcing conventions |
| [[AgenticEngineering]] | High — time invested designing specs, guardrails, and the [[AILayer]]; larger orgs often stand up a small forward-deployed team to build it | Low — output quality compounds, so token spend per feature drops over time |

### The crossover

Cole's read: the crossover point (where agentic engineering's upfront cost pays for itself) comes fast. Once the harness exists, agentic engineering becomes roughly 3–10x more reliable and cheaper than continuing to vibe-code, because you stop burning millions of tokens re-iterating on code the agent produced without conventions or a validation strategy. The practical advice: invest in the harness early rather than letting vibe-coding operational costs compound.

## Related

- [[AIDrivenSDLC]] — the broader framework this cost model belongs to
- [[VibeCoding]] — the low-CapEx/high-OpEx end
- [[AgenticEngineering]] — the high-CapEx/low-OpEx end
- [[HarnessEngineering]] — what the upfront capital expenditure buys
- [[Google]] — source of this framing
- [[ColeMedin]] — narrator/analyst
- [[summary-20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)]] — primary source
