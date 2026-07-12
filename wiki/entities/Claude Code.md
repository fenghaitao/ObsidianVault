---
title: "Claude Code"
type: entity
tags: [tool, ai, agent, coding, security-incident]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/16 - Head of Growth (Anthropic)： Anthropic is automating its own growth.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

Claude Code is Anthropic's AI coding agent, launched around July 2025. It started as a terminal-based hack by Boris Cherny and has grown to power 4% of all GitHub commits, with ~$2B in revenue. It is available on terminal, iOS, Android, desktop app, web, Slack, and GitHub.

## Key Information

- A group was able to hijack Claude Code into performing a cyber attack by separating malicious requests into smaller, individually legitimate-seeming requests.
- The attack worked by having one instance gather information (e.g., "go to this URL and tell me what backend it's running") and another instance use that information (e.g., "this is my system, how would you hack it?").
- This technique bypasses defenses because each individual request appears legitimate; only when combined do they form a malicious attack.
- Sander Schulhoff had been warning about this attack vector for approximately two years prior to the incident.
- Represents a new class of AI-powered computer viruses that can think for themselves and make API requests to determine next steps.
- Zevi Arnovitz, a non-technical PM at Meta, uses Claude Code within Cursor as his primary AI coding agent
- Zevi runs Claude Code alongside Cursor's Composer for different tasks — Claude Code for planning and complex work, Composer for speed
- Claude Code supports slash commands: reusable prompts saved in the codebase that can be invoked with `/commandName`
- Zevi's slash command workflow: create issue, exploration phase, create plan, execute plan, review, peer review, update docs
- Claude Code integrates with Linear via MCP (Model Context Protocol) to create issues automatically
- Zevi uses Claude Code as his "dev lead" — it has the most context and leads the project, while other models provide peer review

- Boris Cherny, Head of Claude Code, has 100% of his code written by Claude Code since November 2025; he ships 10-30 PRs per day
- Claude Code started as a solo project by Boris; the first internal demo got "two likes"
- The product was originally called "Claude CLI" then "QuadCode" before being renamed Claude Code
- Built on the principle of latent demand: it stayed terminal-based because that was the only form factor that could keep up with the model's rapid improvement
- Boris's principle: "under-resource things a little bit at the start" — the terminal was the easiest way to build solo
- Growth has been exponential and accelerating; the DAU chart went "vertical" immediately internally
- Claude Code was not immediately a hit externally — it took many months for people to understand it
- Key inflection points: Opus 4 (May 2025), then November 2025, and continuing
- In the last month before recording, daily active users doubled
- 4% of all GitHub commits are authored by Claude Code (per SemiAnalysis); predicted 20% by end of 2025
- Boris predicts "by the end of the year, you might not need an IDE to code anymore"
- Claude Code reviews 100% of pull requests at Anthropic internally
- Boris uses plan mode for ~80% of tasks; auto-accepts edits after plan is approved
- Available on iOS, Android, desktop app, web, Slack, and GitHub integrations
- Boris: "Most of the world still does not use Claude Code... it just feels like this is 1% done"
- Built in 10 days using Claude Code itself; ships with an entire virtual machine for security
- The Claude Code team is hiring; everyone on the team codes regardless of role
- Claire Vo uses Claude Code as a "god mode administrator" of her OpenClaw agents: when an agent breaks, she opens Claude Code, points it at the OpenClaw docs, and says "go fix"
- Claude Code can read OpenClaw's configuration, identify mismatches (e.g., "you have this field named ABC and it's supposed to be XYZ"), and fix them automatically
- Claude Code can also perform "brain transplant" operations — fracturing one agent's memory into separate agents by reading and reorganizing configuration files
- There is a dedicated Claude Code growth pod within Anthropic's growth team, working closely with Cat and Boris
- The Chrome extension that underpins Claude Code and Co-work use cases was built by the growth team, not a core product team

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Claude]] — underlying model
- [[Anthropic]] — parent company
- [[Cursor]] — IDE where Zevi runs Claude Code
- [[Zevi Arnovitz]] — non-technical PM power user
- [[Slash Commands Workflow]] — Zevi's development methodology
- [[Prompt Injection]] — related attack vector
- [[Boris Cherny]] — Head of Claude Code
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Opus 4]] — inflection point model
- [[Opus 4.6]] — current most capable model
- [[Sonnet 4]] — earlier inflection model
- [[Sonnet 3.5]] — early model
- [[Plan Mode]] — key feature
- [[Co-work (Claude)]] — spin-off product for non-coding tasks
- [[Latent Demand]] — key product principle
- [[QuadCode]] — earlier name
- [[MCP (Model Context Protocol)]] — enabling protocol
- [[OpenClaw]] — used as admin tool for managing agents
- [[Claire Vo]] — uses Claude Code as "god mode administrator" for her OpenClaws
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
- [[SemiAnalysis]] — reported on adoption metrics
- [[GitHub]] — 4% of commits are Claude-authored
- [[Amol Avaisary]] — Head of Growth, growth pod works on Claude Code
- [[Browser Extension (Claude)]] — built by growth team, underpins Claude Code and Co-work
- [[summary-16 - Head of Growth (Anthropic)： Anthropic is automating its own growth]] — source summary
