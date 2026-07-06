---
title: "PIVLoop"
type: concept
tags: [concept, agentic-coding, workflow, planning, validation, claude-code]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260430 - FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why).md"
last_updated: 2026-07-06
---

## Definition

The PIV loop — **Plan, Implement, Validate** — is [[ColeMedin]]'s unit of work for building a feature (or a PRD phase) with a coding agent. You take a focused slice of scope, create a structured plan, reset context and delegate the implementation entirely to the agent, then validate (agent self-tests + human review). It is the repeatable inner loop of his greenfield [[AILayer]]-first workflow: a PRD is split into phases, and each phase is one PIV loop.

## Key Information

### The three steps

```
Plan ───────────────→ Implement ──────────→ Validate
(human-led)            (agent-led)           (agent + human)
vibe-plan → /plan      /clear → /execute     pyramid + code review
```

1. **Plan** — start with *unstructured "vibe planning"* (explore architecture, spin up research [[SubAgent]]s for codebase/docs), then a `/plan-feature` command formalizes it into a **structured plan**: goal & success criteria, reference docs, a task list (down to specific files), and — most importantly — a **validation strategy defined upfront** (test-driven). Review/iterate the plan; it's high-leverage.
2. **Implement** — **[[ContextReset]] first**: the plan contains all the context the executor needs, so start a fresh session and `/execute <plan>`. **Delegate all coding to the agent.** This is *not* vibe coding — it's "trust but verify," safe only because the implementation is sandwiched between human-led planning and validation.
3. **Validate** — the agent self-checks via the **validation pyramid** (type-check + lint → unit → integration → **end-to-end** with [[VercelAgentBrowser]]), then the *human* does a code review and manual test before `/commit`. Cole's packaged **`/e2e-test` skill** (see `summary-self-healing-e2e-validation`) can *be* this validate step — referenced in the `/plan-feature` plan's validation section so the agent runs comprehensive regression testing after implementing.

### Relationship to top-level planning

There are two planning layers: **project-level** (the PRD + rules — see [[PRDFirstDevelopment]] / [[AILayer]]) done once, and **task-level** (the PIV loop's plan step) done per phase. Creating a structured plan mirrors creating the PRD, but scoped to a single feature.

### Inner loop vs outer loop

Per `summary-principled-agentic-engineer`, the PIV loop is the **inner loop** — when the agent nails a ticket, you just loop back to the next one. When something goes wrong, you step into the **outer loop**: [[SystemEvolution]] (fix the [[AILayer]] so the class of bug can't recur), then resume the inner loop. Most of the time you're in the inner loop; run the outer loop whenever a PIV surfaces a systemic issue.

### Why it works

- **Granularity** — never asks the agent to do too much at once; each phase is bounded.
- **Front-loaded alignment** — heavy planning makes implementation fast and reliable; later PIV loops get faster because the [[AILayer]] is already aligned.
- **Context hygiene** — the plan→implement reset keeps the executor's window clean ([[ContextRot]] defense).
- **Trust but verify** — human owns plan + final validation; agent owns the code and its own tests.

### Practical tip

Set real environment variables (via a `.env.example` the agent reads) *before* implementation — otherwise the agent does mock testing and falsely reports validation passed.

### The "R-PIV" expansion (July 2026)

Per `summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One`, Cole makes the implicit first step explicit by naming the loop **R-PIV: Research → Plan → Implement → Validate**. Research is the exploration Cole already did informally at the start of the Plan step (spinning up research [[SubAgent]]s, understanding the codebase) — the rename doesn't change the mechanics, just makes the research phase a named, first-class step. Cole ties the R-PIV loop directly to [[AICodingAutonomyLevels]] Level 3 ("developer" — a Waymo with a safety driver): full coding delegation is safe specifically because it's sandwiched by human-led research/planning and human-led validation.

## Related

- [[AILayer]] — set up before the first PIV loop; PIV loops evolve it
- [[PRDFirstDevelopment]] — the PRD whose phases each become a PIV loop
- [[ContextReset]] — the reset between Plan and Implement
- [[ValidationGates]] — the validation step's checks
- [[VercelAgentBrowser]] — end-to-end validation tool
- [[SubAgent]] — research sub-agents used in the Plan step
- [[SystemEvolution]] — applied after each loop to improve the system
- [[ColeMedin]] — articulator
- [[cole-vs-brian-planning-methodologies]] — synthesis comparing Cole's and Brian's planning approaches
- [[AICodingAutonomyLevels]] — Level 3, the autonomy level the R-PIV loop operationalizes
- [[summary-20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)]] — primary source
- [[summary-20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)]] — the /e2e-test skill as the validate step
- [[summary-20260430 - FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)]] — inner/outer loop framing; two planning layers
- [[summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)]] — the R-PIV (Research-Plan-Implement-Validate) naming
