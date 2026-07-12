---
title: "Slash Commands Workflow"
type: concept
tags: [AI, development, workflow, productivity, methodology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

The Slash Commands Workflow is Zevi Arnovitz's structured, repeatable development process for building products with AI, using reusable prompts (slash commands) saved within the codebase. Each slash command represents a distinct phase of development.

## Key Information

- Created by Zevi Arnovitz, a non-technical PM at Meta, to systematically build products with AI
- Slash commands are reusable prompts saved as files within the codebase, invoked with `/commandName`
- The full workflow: (1) **Create Issue** — quickly capture bugs or feature ideas as Linear tickets while mid-development, (2) **Exploration Phase** — Claude studies the codebase, understands the current state, and asks clarifying questions about the feature, (3) **Create Plan** — generates a markdown plan file with TL;DR, critical decisions, and task breakdown with status tracking, (4) **Execute Plan** — builds the feature (can use different models for different parts: Cursor Composer for speed, Gemini for UI), (5) **Review** — Claude reviews its own code for bugs, (6) **Peer Review** — multiple models (Claude, Codex, Gemini) review code independently, then Claude as "dev lead" evaluates all findings, (7) **Update Docs** — update documentation so future agents write better code
- The workflow was originally formulated within a GPT Project as a "CTO co-founder" system prompt
- Zevi created slash commands whenever he noticed a pattern repeating, automating it into the workflow
- The exploration phase is the key differentiator from "vibe coding" — it ensures proper planning before code is written
- Plans can be split between models: backend tasks to Claude, frontend tasks to Gemini, fast tasks to Cursor Composer
- All slash commands and prompts are available for download from Lenny's Podcast show notes

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — creator of the workflow
- [[AI CTO Co-Founder]] — original inspiration for the workflow
- [[Multi-Model Peer Review]] — the peer review phase
- [[Vibe Coding]] — contrasted with the structured workflow approach
- [[Claude Code]] — primary tool where slash commands run
- [[Cursor]] — IDE where slash commands are used
- [[Linear]] — issue tracker integrated via MCP
