---
title: "Self-healing Agents"
type: concept
tags: [concept, agent-automation, qa, self-healing, ci-cd]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md"]
last_updated: 2026-06-30
---

## Definition
Self-healing Agents are AI agents that can automatically detect failures in their own output (e.g., acceptance criteria not met after deployment) and autonomously create fix pull requests to resolve the issues, forming a closed-loop development pipeline where agents can correct their own mistakes without human intervention.

## Key Information
- **Origin**: Presented by [[MikeSpitz]] as the next evolution of the [[Post-Engineer Engineering Org]] at [[PFF]]
- **Current State (May 2026)**: Not yet implemented — planned for the coming months
- **Target Flow**: [[Autonomous QA Agent]] identifies failed acceptance criteria → self-healing agent inspects the failing tickets → agent determines what needs to change → agent auto-creates fix PRs
- **Enabling Factor**: Trust in agents — once QA is agent-driven and reliable, the next step is agent-driven fixes
- **Parallelization Benefit**: Self-healing enables multiple features to be developed in parallel because the system can resolve issues without serial human intervention
- **Relationship to QA**: Builds on the Autonomous QA Agent; QA identifies failures, self-healing resolves them
- **Full Pipeline**: Spec → LDD → tickets → PRs → code review → QA → self-healing fix PRs → re-QA → merge

## Related
- [[MikeSpitz]] — presented the concept
- [[PFF]] — company planning to implement self-healing
- [[Post-Engineer Engineering Org]] — organizational model
- [[Autonomous QA Agent]] — prerequisite: QA must identify failures before self-healing can fix them
- [[Composable Skills]] — mechanism for encoding the self-healing workflow
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]]
