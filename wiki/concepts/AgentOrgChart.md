---
title: "AgentOrgChart"
type: concept
tags: [ai, agents, organization, hierarchy, paperclip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
An agent org chart is a hierarchical organizational structure of AI agents where a human acts as CEO, delegating work through an executive branch (CTO, CMO, etc.) down to individual contributor agents (coders, content strategists, video writers). Each agent has a defined role, can be configured with different models and skills, and communicates within the organization to complete work.

## Key Information
- Core concept in Paperclip: the human is the CEO who gives instructions to their CEO agent
- The CEO agent breaks down tasks to the executive branch (CTO, CMO, etc.) and then to individual contributors
- Example org chart from Paperclip's own development: CEO → CTO → coders (Claude coder, Codex coder), CMO → content strategist → video writer
- Agents can hire other agents — the CEO agent knows how to hire new employees and install skills
- Each agent can use a different model (Claude, Codex, Gemini, Pi, Hermes, OpenClaw, etc.)
- Agents negotiate, communicate, and have their memory stored within the organization
- Practical advice: start with only the agents you need, build agent by agent, ensure quality before fanning out
- Templates exist for importing large organizations, but Dotta Bippa recommends starting small and crafting agent instructions carefully
- Meta-agents can be created to improve other agents (e.g., a "skill consultant" that diagnoses whether agents are using skills correctly)
- Organizational learning: feedback given to agents accumulates into improved skills and preferences over time

## Related
- [[Paperclip]] — the orchestrator implementing agent org charts
- [[DottaBippa]] — creator of Paperclip
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[ZeroHumanCompany]] — the vision enabled by agent org charts
- [[BringYourOwnAgent]] — each node in the org chart can use different models
- [[AgentRoutines]] — reusable tasks within the org chart
- [[AgentReviewerApprover]] — QA and approval gates between org chart levels
- [[MultiAgentArchitecture]] — broader multi-agent architecture pattern
- [[AgentCompanyPattern]] — related business application pattern
