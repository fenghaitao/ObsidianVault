---
title: "PRD (Project Requirements Document)"
type: concept
tags: [AI, vibe-coding, planning, documentation, methodology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-10
---

## Definition

In the context of AI vibe coding, PRDs (Project Requirements Documents) are structured markdown files that serve as "sources of truth" for AI agents. Lazar builds at least four PRDs before executing any code: Master Plan, Implementation Plan, Design Guidelines, and User Journeys. These feed into a final tasks.md for execution.

## Key Information

- Lazar's PRD framework includes four documents:
  1. **Master Plan** — 10,000-foot overview: why, who, how it should feel; references other PRDs
  2. **Implementation Plan** — sequence/roadmap: backend first, then auth, then API, etc.
  3. **Design Guidelines** — look and feel, including CSS elements; AI is "sometimes over creative" and needs steering
  4. **User Journeys** — how users navigate, feature flows, registration → first step → second step
- All feed into **tasks.md** — the final document with specific tasks and subtasks for execution
- "I'll spend an entire day if I need to just planning this part out"
- The PRDs combat the context window problem: the AI reads them before each task, keeping context dynamic
- AI likes to read markdown format; Lazar uses .md files for all PRDs
- "We're all becoming product managers on steroids" — AI does the writing, humans provide judgment
- Custom GPTs available: Lazar built "Lovable PRD Generator" and "Lovable Base Prompt Generator" on ChatGPT store

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — originator
- [[Master Plan (AI Development)]] — sub-component
- [[Implementation Plan (AI Development)]] — sub-component
- [[Design Guidelines (AI Development)]] — sub-component
- [[User Journeys (AI Development)]] — sub-component
- [[Rules.md (AI Agent Configuration)]] — companion file for agent behavior
- [[Context Window Management]] — the problem PRDs solve
