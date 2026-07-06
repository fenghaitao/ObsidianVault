---
title: "AIDrivenSDLC"
type: concept
tags: [concept, sdlc, google, harness-engineering, bottleneck]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good).md"
last_updated: 2026-07-06
---

## Definition

The AI-driven SDLC is [[Google]]'s reframing of the traditional software development life cycle (requirement gathering → design → implementation → testing/review → deployment/maintenance) for an era where AI coding assistants have collapsed the implementation stage from weeks to minutes or hours, while the human-bottlenecked stages at the start and end (requirements, validation) haven't sped up nearly as much. Per [[ColeMedin]], the headline claim is: **specification quality is the new bottleneck.**

## Key Information

### Why the bottleneck moved

In a traditional SDLC, implementation (the engineer writing code) is usually the largest time sink — days to weeks. AI coding assistants compress that to minutes/hours, dozens of times faster, because agents can iterate against their own tests and evals. But requirement-gathering (stakeholder meetings, PRD writing) and the final review/deployment/maintenance stage are still mostly human-paced. The result: **the overall SDLC isn't proportionally faster**, even though the middle stage exploded in speed — explaining why AI coding assistants can 10x an individual engineer's output without 10x-ing the business's overall output.

### The spectrum: vibe coding → structured AI-assisted → agentic engineering

Google frames AI coding as a spectrum (not binary vibe-coding-vs-not), differing along three dimensions:

| Dimension | [[VibeCoding]] | Structured AI-assisted | [[AgenticEngineering]] |
|---|---|---|---|
| Intent specification | Casual natural-language prompt | More detail, no formal spec process | Repeatable process; specs engineered like code |
| Verification | "Does it seem to work?" | Manual testing / spot-checks | Agent self-iterates with tests, evals, CI/CD gates, LLM judges, separate code review |
| Risk profile | High (fine for disposable code) | Medium | Low (systematic verification at every stage) |

Cole's take: it's not that you always want the rightmost end — vibe coding is genuinely fine for prototypes/MVPs — but agentic engineering is where you want to be for reliable, production code.

### Implication

Because implementation is no longer the bottleneck, the next wave of high-value tooling/companies is likely to target speeding up *requirements gathering* and *validation* — the stages AI hasn't compressed yet.

## Related

- [[HarnessEngineering]] — the "90% of the system" that Google's masterclass argues you should invest in
- [[AgenticEngineering]] — the rightmost end of the spectrum
- [[VibeCoding]] — the leftmost end of the spectrum
- [[TokenEconomics]] — the CapEx/OpEx tradeoff across this same spectrum
- [[Google]] — source of this framing
- [[ColeMedin]] — narrator/analyst
- [[summary-20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)]] — primary source
