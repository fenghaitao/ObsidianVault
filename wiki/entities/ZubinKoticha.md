---
title: "Zubin Koticha"
type: entity
tags: [person, ceo, founder, agent-observability, raindrop]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"
last_updated: 2026-06-29
---

## Definition
Zubin Koticha is the CEO and co-founder of Raindrop, an agent observability platform. He presented the framework for agent observability at aiDotEngineer, covering explicit and implicit signals, production experiments, and the monitoring paradigm shift from evals to production observability.

## Key Information
- **Role**: CEO and co-founder of Raindrop
- **Core thesis**: Agent failures are fundamentally different from traditional software failures — non-deterministic, unbounded, with infinite input/output spaces. Traditional evals are insufficient; production monitoring is essential.
- **"Humanity's last problem"**: When humans can no longer monitor agents and find issues, agent observability becomes the most important problem of our time.
- **Key concepts introduced**:
  - **Explicit signals**: Error rate, latency, regenerations, cost — objective and verifiable
  - **Implicit signals**: Regex patterns, classifiers, self-diagnostics — semantic and harder to detect
  - **Production experiments**: Ship changes to percentage of users, compare signal rates against control group
  - **Feedback loop**: Improve prompting → change models → modify agent harness → measure impact on signals
- **On experiments**: Statistical relevance starts at a few hundred events; not always scientifically significant but practically useful
- **On Claude Code**: Referenced the leaked `keywords.ts` regex approach for frustration detection as an example of cheap, effective implicit signals
- **On pricing**: Free trial is 2 weeks, likely extending; open to DMs for longer access
- **Hiring**: Actively expanding the team

## Related
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
- [[Raindrop]] — company
- [[DannyGollapalli]] — co-presenter, back-end engineer
- [[AgentObservability]] — core concept
- [[ImplicitSignals]] — concept introduced
- [[ExplicitSignals]] — concept introduced
- [[AgentExperiments]] — concept introduced
- [[ClaudeCode]] — referenced for regex frustration detection
- [[aiDotEngineer]] — event host
