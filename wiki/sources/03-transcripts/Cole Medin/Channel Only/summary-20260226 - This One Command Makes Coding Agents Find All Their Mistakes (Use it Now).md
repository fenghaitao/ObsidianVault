---
title: "summary-20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)"
type: source
tags: [source, original-material, validation, e2e-testing, claude-skills, self-healing]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] packages his entire AI-code validation process into a single, general `/e2e-test` [[ClaudeSkills|Claude Code skill]] he calls the **"self-healing AI coding workflow."** The premise: coding agents are terrible at validating their own work unless you give them a *specific framework* — left alone they skimp on validation. The skill works out-of-the-box on any frontend codebase, auto-installs the [[VercelAgentBrowser]] CLI, and delegates as much validation as possible to the agent so that by the time control returns to the human, most issues are fixed or precisely surfaced — lifting the burden of reviewing hundreds of lines of just-generated code.

## Key Points

- **Why it matters**: agents generate code faster than humans can review it, but AI-generated code is still *your* responsibility. This is delegation of validation, not vibe coding.
- **Six-step workflow** (invoked `/e2e-test`):
  1. **Prereq check** — requires a frontend (browser-automation-based); on Windows, use WSL (the Vercel Agent Browser CLI needs Linux/Mac/WSL).
  2. **Research phase — 3 parallel [[SubAgent]]s**: (a) codebase structure + how users use the app, (b) database schema, (c) **bug-hunt code review** (logic errors). Findings compiled into the primary agent's context.
  3. **Start dev server + build a task list** — one task per user journey.
  4. **For-loop over user journeys** — mix of agent-browser navigation and DB queries: snapshot the page → query the DB → interact with an element → verify the record → take screenshots (UI can be image-analyzed by the agent and reviewed by the human). **Only fixes big blockers** that prevent validating a journey; retests in a loop until the journey passes.
  5. **Responsive checking** — lighter pass across mobile/tablet/desktop.
  6. **Structured end-to-end report** — fixed issues / remaining issues / everything tested, in a *consistent* format (enforced at the bottom of the `skill.md`), plus a screenshots folder and an optional markdown report.
- **Deliberately under-fixes**: it's prompted to fix *only* blockers; usually *more* issues remain than are fixed. Moderate/minor issues are surfaced for the human to triage (address how/whether you want), not auto-changed.
- **Context handoff**: after testing, the context window is bloated — take the report into a **fresh session** to work through remaining issues.
- **Neon test-data isolation**: end-to-end testing creates many fake users/records; Cole uses a **[[Neon]] database branch** as a disposable test DB (snapshot → let the agent run wild → delete the branch), keeping the main DB clean. Could be built into the workflow but he leaves it DB-agnostic.
- **Two ways to use it**: standalone (run full e2e on any codebase anytime), or **built into the [[PIVLoop]]'s validate step** — reference the skill in the `/plan-feature` validation section so the agent runs it after writing a feature (as a regression check). Note: Cole **disables model-invocation** on the skill by default (a Claude Code option) so it's only run when explicitly invoked; remove that line to let the agent call it autonomously.
- **Cost**: token-heavy and slow (waits on page loads), but worth it — "the point is not to be fast, it's to be comprehensive." He's run it dozens of times in a week without hitting his Claude Code Max limit, and argues it *saves* tokens overall by catching issues early.

## Related

- [[ValidationGates]] — this is Cole's packaged, self-healing validation workflow
- [[VercelAgentBrowser]] — the browser-automation engine it runs on
- [[PIVLoop]] — can be wired into the validate step of feature development
- [[SubAgent]] — three parallel research sub-agents (structure / schema / bug-hunt)
- [[ClaudeSkills]] — delivered as a `skill.md` (with model-invocation toggle)
- [[Neon]] — database branching for test-data isolation
