---
title: "summary-20260430 - FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)"
type: source
tags: [source, original-material, agentic-engineering, piv-loop, workshop, jira]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260430 - FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI).md"]
last_updated: 2026-06-20
---

## Core Summary

A one-hour workshop (with Lior Weinstein) where [[ColeMedin]] consolidates his entire AI-coding system into three phases — **ideate → [[PIVLoop|PIV loop]] → [[SystemEvolution|system evolution]]** — deliberately *simple* so you can mold it to your own SDLC rather than adopting a bloated off-the-shelf framework. The throughline: the engineer's job shifts from writing code to the higher-leverage **planning and validating**; you stay in the driver's seat, so it's not vibe coding.

## Key Points

- **Anti-over-engineering stance**: respects but warns against heavyweight frameworks (GitHub Spec Kit, BMAD, Claude Flow, GSD, "Gastown," BDD/Gherkin) — they try to do too much and are hard to mold to your team's existing practice. Teach your conventions to the agent via a simple [[AILayer]] instead of throwing your process out.
- **Two planning layers**:
  - **Project-level (PM-level)** — ideate the sprint/MVP. Brain-dump (speech-to-text) → force **clarifying questions** (Claude Code's AskUserQuestion tool) to reduce assumptions → `/create-prd` produces a structured [[PRDFirstDevelopment|PRD]] (executive summary, mission, target users, in-scope) → `/create-stories` splits it into tickets and pushes them to Jira via the **Atlassian/Jira MCP** (even adding research as ticket comments). PMs do this step too.
  - **Task-level (developer)** — pick a ticket (the **issue is the spec**) and run the [[PIVLoop]].
- **The PIV loop per ticket**: `/prime` (load codebase + the Jira issue + git log as long-term memory) → unstructured exploration with research [[SubAgent]]s → `/plan` → structured plan markdown (summary, decisions, patterns-to-follow, files to change, task list, self-validation strategy) → **[[ContextReset|fresh session]]** → `/implement <plan>` (agent codes, self-validates: lint/type/unit/e2e via agent browser, makes a branch/PR, updates the Jira ticket) → **human code review + manual test**.
- **Validate the PRD/plan before proceeding**: create-PRD and create-stories are *separate* commands on purpose so you review the PRD first; one bad PRD line → many bad code lines. Same for the plan before implementation.
- **Two loops**: the **inner loop** (PIV, when things work — just loop to the next ticket) and the **outer loop** (system evolution, when something goes wrong — step out and fix the system).
- **[[SystemEvolution]] (the most powerful part)**: when the agent errs, don't just patch the bug — fix the [[AILayer]] so it can't recur. Four typical targets: **commands**, **on-demand context** (incl. Confluence docs optimized for AI), **global rules**, and **plan/PRD templates**. Crucially, commands/skills/rules are **version-controlled team artifacts** — improve one via a PR and the whole team benefits (one fix can save engineers dozens of hours).
- **Agents do the admin**: via MCP, the agent creates/updates/assigns Jira tickets, opens branches/PRs, and comments context — removing "backstage" grunt work. Cole notes Claude Code can even set up its own MCP config / copy in his commands by reading its own docs.
- **Commandify everything used 3+ times**; don't manually re-prompt. Commands/skills are just reusable procedures with arguments.

## Related

- [[PIVLoop]] — the per-ticket inner loop
- [[PRDFirstDevelopment]] — project-level PRD → stories → Jira
- [[SystemEvolution]] — the outer loop; evolving the AI layer
- [[AILayer]] — rules + commands + skills you mold to your SDLC
- [[Commandification]] — package repeated prompts as commands
- [[AgenticEngineering]] — the umbrella discipline ("principled agentic engineer")
- [[IntentEngineering]] — the clarifying-questions / success-criteria emphasis
