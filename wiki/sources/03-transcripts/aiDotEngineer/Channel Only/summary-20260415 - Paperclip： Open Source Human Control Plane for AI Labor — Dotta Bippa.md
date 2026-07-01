---
title: "summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa"
type: source
tags: [source, transcript, ai, agent-orchestration, paperclip, open-source, agent-organization, human-in-the-loop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Core Summary
Dotta Bippa (Doda), creator of Paperclip, presents an open-source agent orchestrator designed as a "human control plane for AI labor." Paperclip lets users create an org chart of AI agents — CEO, CTO, coders, marketing — where each agent can be configured with different models (BYO-agent), skills, budgets, and workflows. The system provides reviewer/approver gates, routines (reusable templated tasks), and plans to ensure agents complete work reliably. Paperclip is positioned as a vendor-neutral harness for building zero-human companies, not just a coding tool — it supports marketing, sales, finance, and operations workflows. Released March 4, 2026, it had already crossed 50,000 GitHub stars by the recording date (~34 days later).

## Key Points
- Paperclip tagline: "open-source orchestration for zero-human companies" — hire employees, set goals, automate jobs
- Core concept: org chart of AI agents where the human acts as CEO, delegating to an executive branch and individual contributors
- Bring-your-own-agent: supports Claude Code, Codex, Gemini, Pi, Hermes, OpenClaw, OpenRouter (including free models like Qwen 3.6+), Cursor, and more
- Every piece of the Paperclip app has an "agentic surface" — agents can hire other agents, install skills, create plans, execute tasks
- First-class support for plans: agents create plans, humans review and give feedback, then agents execute
- Reviewer and approver roles: tasks can require a QA reviewer (agent browser skill for testing) and a manager approver before completion
- Routines: reusable templated tasks with variables, can run on a schedule or manually — like a prompt folder with parameterization
- Skills manager built in: agents can install skills from skills.sh; Paperclip-specific skills accumulate branding guides, preferences, and style over time
- Budgets: per-agent and per-project monthly spend tracking, supports subscription-based models
- Concurrency: agents default to one parallel task; configurable for more
- Agent instructions: users are encouraged to iteratively refine agent instructions when agents make mistakes
- Meta-agents: e.g., a "skill consultant" agent that diagnoses whether other agents are using skills correctly
- Roadmap items: CEO chat, maximizer mode (unlimited agent work), multi-human users, cloud/sandboxed agent deployments, desktop app, memory/knowledge base improvements
- Practical advice: start small with agents you need, build agent by agent, ensure quality before fanning out; not every agent needs frontier model pricing
- Not just a coding tool — designed for marketing, sales leads, finance operations, running entire businesses
- Released March 4, 2026; crossed 40,000 then 50,000 GitHub stars within ~34 days
- Demo: used Paperclip to create a Remotion video celebrating 40,000 stars by having the CEO hire a video writer agent with the Remotion skill

## Related
- [[DottaBippa]] — speaker, creator of Paperclip
- [[Paperclip]] — the open-source agent orchestrator
- [[Remotion]] — video creation tool used in demo
- [[Greptile]] — code review tool used in Paperclip's open-source workflow
- [[OpenRouter]] — model router for BYO-agent
- [[ZeroHumanCompany]] — the vision of AI-run businesses
- [[AgentOrgChart]] — organizational hierarchy for AI agents
- [[BringYourOwnAgent]] — vendor-neutral agent integration
- [[AgentRoutines]] — reusable templated agent tasks
- [[AgentBudgets]] — per-agent and per-project cost controls
- [[AgentReviewerApprover]] — QA and approval workflow gates
- [[Agent Orchestration]] — broader orchestration context
- [[Skills]] — reusable agent playbooks, built into Paperclip
- [[HumanInTheLoopWorkflows]] — reviewer/approver pattern
- [[MultiAgentArchitecture]] — org chart as multi-agent architecture
- [[AgentCompanyPattern]] — related business application pattern
- [[aiDotEngineer]] — conference/channel hosting the talk
