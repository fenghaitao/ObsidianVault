---
title: "summary-20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)"
type: source
tags: [source, original-material, agentic-coding, piv-loop, ai-layer, greenfield]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] walks through his "dead simple," own-it-and-evolve **greenfield** agentic coding framework via a live build of a self-hosted Linktree-style app. The shape: set up the [[AILayer]] (PRD + global rules + commands + sub-agents + reference folder), split the PRD into phases, and knock out each phase with a **[[PIVLoop]]** (Plan → Implement → Validate). Throughout, he threads **four golden rules**: protect context, commandify everything, treat the git history as long-term memory, and adopt the [[SystemEvolution]] mindset. He deliberately favors a simple, customizable framework over heavyweight ones (BMAD, GitHub Spec Kit) so you can make it your own.

## Key Points

- **PRD first (project-level planning)**: start with an *unstructured* casual conversation (Cole uses speech-to-text — AquaVoice — to brain-dump), spin up **research sub-agents** (web + codebase), then have the agent **ask a flood of clarifying questions** (Claude Code's AskUserQuestion multiple-choice tool) to *reduce assumptions* — "one bad line in a PRD can be a thousand bad lines of code." Then a `/create-prd` command writes a structured PRD: MVP scope, out-of-scope, directory structure, and **phases of work**.
- **Global rules (`AGENTS.md`)**: concise constraints/conventions always loaded (tech stack, run/test/log commands, project structure, code patterns) — a `/create-rules` command builds it from a template. Keep it short (~230 lines).
- **Reference folder = on-demand context = [[ProgressiveDisclosure]]**: bigger guides (e.g. `components.md`, `api.md`, `styles.md`) that the agent loads *only* when working on that area — pointed to from the global rules so the always-loaded context stays lean.
- **The AI layer is reusable + evolvable**: Cole keeps a generic set of commands/skills as a starter for every new project, then evolves them to be project-specific as the codebase grows.
- **Sub-agents for research only**: great for context isolation (they load 10s–100s of thousands of tokens but return only a summary). Claude Code ships research/exploration sub-agents but *not* implementation ones — Cole agrees: don't use sub-agents for implementation (you need all the editing context; isolation causes hallucinations).
- **[[PIVLoop]] (Plan-Implement-Validate)** per phase:
  - **Plan** = "vibe planning" (unstructured exploration, research sub-agents) → `/plan-feature` command → structured plan: goal/success criteria, reference docs, task list (down to specific files), and — most important — a **validation strategy defined upfront** (test-driven).
  - **Context reset** between plan and implement — the plan is *all* the context the executor needs; start a fresh session and run `/execute <plan>`. Delegate all coding to the agent.
  - **Validate** = the "validation pyramid": type-check + lint → unit → integration → **end-to-end via [[VercelAgentBrowser]]** (agent spins up back/front end, runs migrations, drives the app like a user) — then *human* code review + manual test before `/commit`.
- **`.env.example` trick**: set real environment variables *before* implementation; otherwise the agent does mock testing and falsely claims validation passed.
- **Four golden rules**: (1) **context is your most precious resource**; (2) **commandify everything** used more than twice (note: Claude Code merged commands with skills, but Cole keeps the distinction — commands = *you* invoke, skills = the *agent* decides to load); (3) **git commit history is long-term memory** (a `/commit` command standardizes messages so `/prime` can read the log to understand how the codebase evolved); (4) **[[SystemEvolution]]** — when something's wrong, fix the AI layer (rules / on-demand context / commands / tests) so it can't recur.
- **Compounding in parallel**: you simultaneously grow the **code base**, the **test base** (regression harness — Cole mentions QA Tech, an AI testing platform whose agents evolve test cases with your codebase), and the **AI layer**. Cole calls evolving the AI layer "the most high-leverage part of the entire process," and prefers to make AI-layer changes himself (via agent **meta-reasoning** with "don't change anything yet").

## Related

- [[PIVLoop]] — the per-phase Plan-Implement-Validate loop
- [[AILayer]] — the reusable context-asset wrapper set up first
- [[PRDFirstDevelopment]] — the PRD-as-north-star starting point
- [[Commandification]] — "commandify everything" golden rule
- [[SystemEvolution]] — fix the system, evolve the AI layer
- [[ContextReset]] — reset between plan and implement
- [[ValidationGates]] / [[VercelAgentBrowser]] — the validation pyramid
- [[SubAgent]] — research-only, for context isolation
