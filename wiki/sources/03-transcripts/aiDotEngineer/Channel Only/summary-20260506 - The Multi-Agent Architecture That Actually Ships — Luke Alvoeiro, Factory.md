---
title: "summary-20260506 - The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory"
type: source
tags: [source, transcript, multi-agent, missions, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory.md"]
last_updated: 2026-06-29
---

## Core Summary

Luke Alvoeiro from Factory presents a multi-agent architecture that ships. He proposes a five-framework taxonomy of multi-agent systems (delegation, creator-verifier, direct communication, negotiation, broadcast) and introduces "missions" — a system combining four of these into a single workflow that runs for hours or days. Missions use a three-role architecture: orchestrators (planning and validation contracts), workers (clean-context implementation), and validators (behavioral verification, not just linting/tests). The key claim: the bottleneck is no longer intelligence but human attention.

## Key Points

- Five frontier multi-agent frameworks: delegation, creator-verifier, direct communication, negotiation, broadcast.
- Missions combine delegation, creator-verifier, broadcast, and negotiation into a single long-running workflow.
- Three-role architecture: orchestrators (planning + validation contracts), workers (clean context per feature), validators (end-to-end behavioral verification).
- Validation contracts define "done" before any coding starts, preventing drift over long runs.
- Workers commit by Git, allowing the next worker to inherit a clean slate and working codebase.
- Luke previously created Goose at Block (now donated to the Agentic AI Foundation) and now leads agent harness at Factory.

## Related

- [[LukeAlvoeiro]] — speaker, creator of Goose, Factory agent harness lead
- [[FactoryAI]] — company, mission to bring autonomy to the SDLC
- [[Goose]] — open-source coding agent created by Luke
- [[AgentOrchestration]] — multi-agent orchestration
- [[MultiAgentArchitecture]] — multi-agent systems
- [[ValidationContracts]] — defining "done" before coding
