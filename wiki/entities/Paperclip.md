---
title: "Paperclip"
type: entity
tags: [tool, open-source, agent-orchestration, ai-agents, platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Paperclip is an open-source agent orchestrator that serves as a "human control plane for AI labor." It enables users to create an org chart of AI agents — with roles like CEO, CTO, coders, and marketing — and manage them through projects, tasks, reviewer/approver gates, routines, and budgets. Released on March 4, 2026, it crossed 50,000 GitHub stars within approximately 34 days.

## Key Information
- **Tagline**: "Open-source orchestration for zero-human companies"
- **Website**: paperclip.ing
- **Installation**: `npx paperclip-ai onboard`
- **Released**: March 4, 2026
- **GitHub Stars**: Crossed 40,000 then 50,000 within ~34 days of release
- **Core Features**:
  - Org chart of AI agents with hierarchical delegation (CEO → CTO → coders, CMO → content strategist → video writer)
  - Bring-your-own-agent: supports Claude Code, Codex, Gemini, Pi, Hermes, OpenClaw, OpenRouter, Cursor, and more
  - Projects and tasks with familiar task management interface
  - Reviewer and approver workflow gates (QA review before manager approval)
  - Routines: reusable templated tasks with variables, schedulable or manual
  - Skills manager: agents can install and use skills from skills.sh
  - Plans: first-class support for agent-created plans with human feedback loops
  - Budgets: per-agent and per-project monthly spend tracking
  - Concurrency control: default one parallel task per agent, configurable
  - Experimental workspace support for isolated coding environments
- **Design Philosophy**:
  - Vendor-neutral harness: any agent model can be brought in as an employee
  - Human as CEO: the human gives instructions, the CEO breaks down tasks to the executive branch and individual contributors
  - Agentic surfaces everywhere: agents can hire, install skills, create plans, execute tasks
  - Not just a coding tool — supports marketing, sales, finance, operations
- **Roadmap**: CEO chat, maximizer mode (unlimited agent work), multi-human users, cloud/sandboxed agent deployments, desktop app, memory/knowledge base improvements
- **Dogfooding**: Dotta Bippa uses Paperclip to manage Paperclip's own development
- **Community**: Active open-source community with many pull requests; uses Greptile for first-pass code reviews on community contributions

- Kitze juggles between OpenClaw, Hermes, Paperclip, and Plenty Marks with Codex — "wasting a lot of credits"
- Described as "kind of this cool like Kanban linear like thingy for agents"

## Related
- [[DottaBippa]] — creator
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (Kitze's usage)
- [[Kitze]] — user
- [[ZeroHumanCompany]] — the vision
- [[AgentOrgChart]] — core organizational concept
- [[BringYourOwnAgent]] — vendor-neutral agent integration
- [[AgentRoutines]] — reusable templated tasks
- [[AgentBudgets]] — cost controls
- [[AgentReviewerApprover]] — QA and approval gates
- [[Skills]] — built-in skills manager
- [[Remotion]] — video creation tool used in demo
- [[Greptile]] — code review tool used in Paperclip's workflow
- [[OpenRouter]] — model router for BYO-agent
- [[ClaudeCode]] — supported agent
- [[Codex]] — supported agent
- [[aiDotEngineer]] — conference where Paperclip was presented
