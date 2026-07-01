---
title: "Autonomous QA Agent"
type: concept
tags: [concept, qa, testing, agent-automation, ci-cd]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md"]
last_updated: 2026-06-30
---

## Definition
An Autonomous QA Agent is an AI agent that automatically validates merged pull requests against their acceptance criteria. When a PR is merged and deployed to staging, the QA agent inspects all associated tickets, checks the acceptance criteria, and either passes the deployment or flags specific failures — with a future goal of auto-creating fix PRs for failed criteria (self-healing).

## Key Information
- **Origin**: Presented by [[MikeSpitz]] as part of the [[PostEngineer Engineering Org]] model at [[PFF]]
- **Trigger**: Automatically runs when a PR is merged and deployed to staging
- **Process**: Inspects all tickets in the merged PR → checks against acceptance criteria → passes or flags failures
- **Current State (May 2026)**: Pass/fail with flagged items; engineers handle failures
- **Future Goal**: Agent identifies where acceptance criteria aren't met and automatically creates fix PRs — enabling [[SelfHealing Agents]]
- **Benefits**: Enables parallel work by building trust in agent QA; removes human QA bottleneck; catches regressions immediately
- **Context**: Part of a fully autonomous pipeline from spec → LDD → tickets → PRs → code review → QA
- **Contrast with Traditional QA**: No manual test plans; QA is acceptance-criteria-driven and fully automated

## Related
- [[MikeSpitz]] — presented the concept
- [[PFF]] — company implementing autonomous QA
- [[PostEngineer Engineering Org]] — organizational model
- [[SelfHealing Agents]] — next evolution: agents auto-fix QA failures
- [[Lightweight Design Document]] — upstream document that defines acceptance criteria
- [[Huddles]] — where QA results inform rapid iteration
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]]
