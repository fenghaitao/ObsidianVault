---
title: "Slash Command Development Workflow"
type: concept
tags: [vibe-coding, workflow, ai, product-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Definition

[[Zevi Arnovitz]]'s six-stage development process, implemented as a chain of reusable custom slash commands in [[Cursor]]/[[Claude Code]], for taking a non-technical builder from a passing idea to a shipped, reviewed feature without ever hand-writing code.

## Key Information

- **1. Create issue**: run mid-development, whenever a bug or feature idea comes to mind that shouldn't derail current work. The command tells the agent the user is mid-flow and should ask only brief clarifying questions before capturing a structured ticket in [[Linear]] via MCP — deliberately low-friction, "not ready to be built, ready to start being explored."
- **2. Exploration phase**: run when picking the ticket back up (can take a Linear ticket ID as an argument). The agent reads the current codebase and the ticket, builds an understanding of existing structure and affected files, and returns a set of clarifying questions about scope, data model, UX, and validation — which Zevi answers in one prepared batch rather than iteratively.
- **3. Create plan**: produces a markdown plan file (from a template Zevi found on Twitter) with a TL;DR, the critical decisions made during exploration, and a task list with per-task status tracking — meant to be checked into the codebase so future agents working nearby can see what's already been decided and built.
- **4. Execute**: builds against the plan file, often using Cursor's fast "Composer" model for less complex work, or splitting front-end (assigned to Gemini 3, described as excellent at UI) from back-end work across models.
- **5. Review + peer review**: the agent reviews its own code (`/review`), followed by [[Multi-Model Peer Review]] — other models review the same code, and their findings are fed back to the primary agent to accept or rebut.
- **6. Update docs**: after any significant mistake, the agent is asked to introspect on what in its own prompt/tooling caused the error and to update that documentation so the mistake doesn't recur — treated as compounding, independent of underlying model improvements.
- Origin: the workflow began as an ad hoc sequence embedded directly in the system prompt of Zevi's earlier [[CTO Persona Pattern|ChatGPT "CTO" project]] ("step one we do this, step two we do this..."); individual steps were promoted into standalone slash commands only once he noticed himself repeating the same sequence across projects.
- Deliberately excludes heavy technical decisions (database schema migrations, large architectural changes) from PM-driven execution even at a larger company — Zevi's advice for PMs at bigger orgs is to ship contained, reviewable UI-level work and hand off to a developer for final integration, not to attempt full ownership of complex systems.

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — originates this workflow
- [[CTO Persona Pattern]] — the persona this workflow's agent embodies
- [[Multi-Model Peer Review]] — the workflow's review stages, in depth
- [[Linear]] — issue tracker the workflow integrates with
- [[Cursor]] / [[Claude Code]] — tools the workflow is implemented in
- [[Studymate]] — the app this workflow was demonstrated on, live
