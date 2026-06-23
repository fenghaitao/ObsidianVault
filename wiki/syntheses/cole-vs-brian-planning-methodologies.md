---
title: "Cole vs Brian: Planning Methodologies"
type: synthesis
tags: [synthesis, comparison, planning, cole-medin, brian-casel, methodology]
sources: []
last_updated: 2026-06-23
---

## Question

How do Cole Medin's and Brian Casel's planning methodologies compare — PRD-First + PIV Loop vs Spec-Driven Development + Milestone-Based Building — and what does each approach optimize for?

## Answer

Cole Medin and Brian Casel independently arrived at remarkably similar planning philosophies — front-load decisions into a written artifact, break work into bounded chunks, reset context between chunks — but their implementations diverge in tooling, granularity, and the role of the human in the loop.

### The shared foundation

Both reject [[VibeCoding]] outright. Both insist on a written north-star document (PRD for Cole, spec/PRD for Brian) that survives the planning conversation. Both break that document into sequenced, self-contained chunks. Both reset context between chunks to fight [[ContextRot]]. Both treat the human as the architect who shapes the plan, not the implementer who writes the code.

This convergence is striking because they come from different backgrounds: Cole is an AI/agent engineer building frameworks and tools; Brian is a 20-year software developer turned AI-assisted builder. They arrived at the same pattern from opposite directions.

### Where they differ

| Dimension | Cole Medin ([[PRDFirstDevelopment]] + [[PIVLoop]]) | Brian Casel ([[SpecDrivenDevelopment]] + [[MilestoneBasedBuilding]]) |
|---|---|---|
| **Planning artifact** | PRD (project-level) → PRP (feature-level, via [[PRPFramework]]) | PRD/spec (project-level) → milestone `prompt.md` (per chunk) |
| **Chunk granularity** | PRD phases → each is one PIV loop; PRPs are per-feature | 3-7 milestones per project; each is a meaningful buildable unit |
| **Planning process** | Brain-dump → research sub-agents → 10+ clarifying questions → `/create-prd` → `/create-stories` → Jira/Linear | [[PRDCreator]] skill walks through planning Q&A → produces PRD with ~5 milestones |
| **Implementation unit** | PIV loop: Plan (human-led) → Implement (agent-led, fresh context) → Validate (agent + human) | Milestone: hand `prompt.md` to agent → agent builds → agent writes milestone log → human reviews |
| **Context handoff** | [[ContextReset]] between plan and implement; PRD + codebase as persistent memory | Milestone log as baton pass; each milestone starts with clean context |
| **Validation** | Validation pyramid (type-check → lint → unit → integration → e2e with [[VercelAgentBrowser]]) + human code review | Human review at milestone boundaries; verification criteria defined in spec |
| **Tooling depth** | Deep: `/create-prd`, `/create-stories`, `/plan-feature`, `/execute-prp`, Jira/Linear MCP integration | Lighter: [[PRDCreator]] skill, manual milestone prompt creation |
| **Target audience** | Agentic engineers building production systems | Solo builders creating internal business tools |

### The PIV Loop vs Milestone-Based Building

This is the most instructive comparison. Both are bounded units of work with context resets, but they differ in who drives each phase:

- **PIV Loop**: The human leads planning, the agent leads implementation, and validation is shared. The human's leverage is in the plan — get it right and the agent executes reliably. Cole's insight: "one error in your plan → hundreds of lines of bad code; one bad line is just one line."

- **Milestone-Based Building**: The human writes the milestone prompt (derived from the spec), the agent builds everything, the human reviews. Brian's insight: the milestone log is the critical handoff artifact — it tells the next milestone's agent what exists without carrying forward stale conversation.

Cole's approach is more structured and tooling-heavy; Brian's is more pragmatic and accessible to non-engineers. Cole optimizes for reliability at scale (many features, many agents); Brian optimizes for a solo builder who wants to ship internal tools without writing code.

### The clarifying-questions convergence

Both independently discovered that forcing the AI to ask clarifying questions before planning is essential. Cole demands 10+ questions via Claude Code's AskUserQuestion tool. Brian's [[PRDCreator]] walks through a structured Q&A. The shared insight: the planning conversation surfaces assumptions the human didn't know they were making, and those assumptions are the root cause of most agent mistakes.

### What each approach reveals about the other

- **Cole's approach reveals what Brian's is missing**: structured validation (the pyramid), Jira/Linear integration for tracking, and the PRP layer (feature-level plans with curated codebase intelligence). Brian's milestone prompts are thinner than Cole's PRPs — they lack the codebase intelligence and validation strategy that make PRPs reliably one-shot.

- **Brian's approach reveals what Cole's is over-engineering**: not every project needs Jira integration, story generation, and a validation pyramid. For a solo builder making internal tools, a spec + milestones + milestone logs is sufficient. Brian's lighter tooling footprint makes his approach more accessible to non-engineers.

### The deeper agreement: the human is the product architect

Both converge on the same role for the human: [[ProductArchitect]] (Brian's term) or the planning half of the PIV loop (Cole's framing). The human doesn't write code. The human shapes the plan, defines success criteria, reviews output, and evolves the system. The agent is the implementer, not the decision-maker.

This is the paradigm shift both are documenting: from "AI helps me code" to "I direct AI to build." The planning methodology is the interface between human intent and agent execution.

## Related

- [[ColeMedin]] — PRD-First, PIV Loop, PRP Framework
- [[BrianCasel]] — Spec-Driven Development, Milestone-Based Building
- [[PRDFirstDevelopment]] — Cole's project-level planning
- [[PIVLoop]] — Cole's unit of work
- [[SpecDrivenDevelopment]] — Brian's methodology
- [[MilestoneBasedBuilding]] — Brian's chunking strategy
- [[PRPFramework]] — Rasmus's feature-level planning (used by Cole)
- [[PRDCreator]] — Brian's planning skill
- [[ContextRot]] — what both fight with context resets
- [[ProductArchitect]] — the human role both advocate
- [[VibeCoding]] — what both reject
