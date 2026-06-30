---
title: "Progressive Autonomy"
type: concept
tags: [agents, deployment, trust, safety, enterprise, governance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture.md"]
last_updated: 2026-06-30
---

## Definition
Progressive autonomy is a deployment approach for AI agents that gradually increases an agent's independence and authority based on evidence of trustworthy outcomes. It follows an exposure ladder: shadow mode → advisory mode → controlled autonomy → full autonomy, with each step gated by demonstrated confidence rather than project plan milestones.

## Key Information
- Articulated by Jess Grogan-Avignon and Jack Wang of Accenture
- Designed to address the trust gap between AI capability and enterprise stakeholder confidence
- The four stages of the exposure ladder:
  1. **Shadow mode**: Agent runs alongside human processes but cannot affect outcomes. Compare human decisions to agent outputs as a signal for iteration.
  2. **Advisory mode**: Agent runs live but only recommends. Humans play an active role, approving or rejecting outcomes. Provides another signal for iteration.
  3. **Controlled autonomy**: Agent triggers actions in narrow, low-risk scenarios with clear limits and kill switches.
  4. **Full autonomy**: Extended autonomy based on achieving the right level of confidence in target behaviors.
- Each step is gated by evidence in outcomes — not completion of activities in a project plan or pass-fail testing
- The approach recognizes that agent behavior is emergent and cannot be fully specified or tested upfront
- Builds trust with stakeholders, leadership, and end customers progressively
- Contrasts with the common enterprise mistake of treating agents like traditional automation (build, deploy, run)
- The eval suite is important but must be paired with progressive deployment into production

## Related
- [[summary-20260528 - Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture]] — source talk
- [[Enterprise Scaffolding]] — the governance context requiring progressive autonomy
- [[Governance as Engineering Problem]] — related reframing of governance
- [[Bounded Autonomy]] — related concept
- [[Autonomy Slider]] — related concept
- [[CrawlWalkRun]] — related progressive approach
- [[AgenticEvaluations]] — the eval component that pairs with progressive deployment
