---
title: "Agent Orchestration"
type: concept
tags: [agent-systems, planning, multi-agent, orchestration]
sources: ["raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md"]
last_updated: 2026-07-07
---

## Definition

Agent orchestration is the coordination of multiple AI agents and model tiers to break complex tasks into structured, reviewable phases — typically inserting a planning step between a request and execution to surface assumptions, align stakeholders, and improve output quality.

## Key Information

### The Planning-First Pattern

The core insight behind agent orchestration is that planning quality determines output quality. When a coding agent receives a vague prompt, it fills gaps with plausible but incorrect assumptions. In AI workflows, late validation — discovering a fundamental flaw after hours of implementation — is disproportionately expensive.

Agent orchestration addresses this by inserting a structured planning phase before code generation. The orchestration layer analyzes requirements, surfaces hidden assumptions, and produces a collaborative planning artifact (such as a Product Requirements Document, or PRD) that stakeholders review before any code is generated.

### CodeRabbit's Implementation

[[CodeRabbit]] built an agent orchestration system on [[Claude]] that sits between a coding request and a coding agent. The system:

- Coordinates multiple [[Claude]] model tiers (see [[ModelTiering]]) to analyze requirements and surface assumptions
- Produces a structured PRD that defines what should be built and what constraints it must satisfy
- Positions itself above [[ClaudeCode]]'s Plan Mode — it is a higher-level orchestration that happens before Claude Code, to "point it in a really narrow and right direction where everything that needs to be explicit is made explicit"
- Uses the PRD as a shared artifact for team alignment, onboarding new engineers, and validating later that output matched intent

### Assumption Surfacing

A central function of agent orchestration is making implicit assumptions explicit. Experienced developers internalize knowledge and assume coding agents share that context, but agents don't. When assumptions go unstated, agents fill gaps with guesses — producing code that compiles and passes tests but doesn't solve the intended problem. The orchestration layer forces these assumptions to the surface before implementation begins.

### Evaluation

Validating orchestration quality requires its own evaluation infrastructure. [[CodeRabbit]] developed a library of LLM judges that scored specific dimensions of plan quality, then measured whether the generated code worked, whether it contained extra scope, and how many tokens it took to get there — comparing outcomes with and without the planning step to isolate the value of planning itself.

### Abstraction Level

Finding the right level of plan abstraction requires iteration. Plans that are too granular go stale the moment the codebase shifts. Plans that are too high-level leave room for agents to fill in assumptions — the original problem the orchestration layer was meant to solve.

## Related

- [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]] — source summary
- [[CodeRabbit]] — company that built the system described here
- [[ModelTiering]] — the practice of matching model tiers to task complexity within an orchestration system
- [[ClaudeCode]] — the coding agent the planning layer sits above
- [[AgenticCoding]] — the broader development paradigm this pattern improves
- [[MultiAgentSystem]] — the multi-agent coordination pattern agent orchestration extends
- [[ExplorePlanCodeCommit]] — Claude Code's built-in planning workflow, a lower-level complement
