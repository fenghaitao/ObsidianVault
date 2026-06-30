---
title: "summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban"
type: source
tags: [source, transcript, ai, software-engineering, plan-and-review, agent-parallelism, vibe-kanban, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban.md"]
last_updated: 2026-06-29
---

## Core Summary
Louis Knight-Webb, founder of Vibe Canvas (Vibe Kanban), argues that as AI coding agents improve, the software engineer's job is shifting from writing code to planning work and reviewing AI-generated output. The time saved from coding does not return as free time — it displaces into planning and reviewing. He presents two approaches (plan-based vs. review-based), a matrix for when each applies, and explores how agent runtime duration is crossing the 5-minute threshold where humans must change their behavior — leading to parallel agent execution and new interface paradigms. He then shuts down his company live on stage.

## Key Points
- The ratios of software engineering work are inverting: coding time shrinks as AI improves (GitHub Copilot → ChatGPT → Cursor → Claude Code), while planning and reviewing time grows
- Time saved from coding is not free time — it displaces into planning and reviewing. "You get 20 minutes back for every half an hour you were spending coding."
- Two fundamental approaches to working with AI agents:
  - **Plan-based approach**: spend time upfront on comprehensive specs, markdown plans, spec frameworks, interrogating the model. Benefit: less review time, fewer rounds of back-and-forth. Cost: more planning time.
  - **Review-based approach**: YOLO a brief prompt, let the agent run, then iterate through review cycles. Benefit: quick to start. Cost: more review time, more back-and-forth.
- "Spending 5 minutes of planning saves you 30 minutes of reviewing AI-generated code."
- **Plan vs. Review Matrix** for when each approach works best:
  - Frontend + Feature Development: review-based (too many stateful edge cases, interactions, animations, styles to spec everything)
  - Backend + Feature Development: plan-based (can do test-driven development)
  - Frontend + Migrations/Refactoring: plan-based
  - Backend + Migrations/Refactoring: plan-based (shouldn't be in the loop at all)
- **Agent runtime duration** is increasing: GitHub Copilot (seconds) → Cursor (30 seconds) → Claude Code 2025 (1-2 minutes) → Claude Code 2026 (5-10 minutes). Each new capability (type checking, testing, Playwright MCP) adds time but improves accuracy.
- The **5-minute threshold**: when agents run longer than ~5 minutes, humans can no longer just sit and wait — they must change their behavior.
- **Agent parallelism** is the solution: run multiple agents simultaneously so that when you finish reviewing one, another has completed. This transforms the engineer into a manager of multiple concurrent work streams.
- **Focus Maxing** (coined term): interfaces should be designed to let agents run as long as possible before yielding back to the human, rather than encouraging constant context-switching. Pulling humans in and out every 30 seconds "fries their brain."
- Wishlist for the ultimate coding agent tool: (1) embraces managing multiple work streams, (2) helps write tasks and plan, (3) helps QA work, (4) helps do code review, (5) shepherds changes until deployed (monitoring PRs, reacting to comments automatically).
- Next major breakthrough prediction: AI being able to QA front-end work via Playwright MCP — letting models find their own bugs by running the project and clicking around.
- Louis Knight-Webb achieved placement on the SWE-bench verified leaderboard ahead of OpenAI.
- He founded the London chapter of AI Tinkers.

### Vibe Kanban / Vibe Canvas
- Started about a year before the talk as a tool to parallelize coding agents
- Supports 8 popular coding agents (Codex, Claude Code, etc.)
- Features: multiple workspaces, diff-based code review, live preview, commenting, PR automation
- Had 30,000 monthly active users and 25,000 GitHub stars
- Shut down during the talk: business model was unsustainable — $30/user subscription vs. users spending $3,000 on Codex tokens through the platform
- Did not sell to enterprise or resell tokens — the two things that make money in the current AI tools market
- Project continues non-commercially; team found jobs at Agent Labs and similar companies
- Key lesson: "hire somebody who's really good at selling to Enterprise"

### Startup Lessons
- Work with great people — the team improved significantly over several rounds
- Hard work: it takes time to learn what real hard work looks like (midnight on a Saturday with the whole team motivated)
- No regrets: "It was the most interesting thing I've worked on and is right at the cutting edge of agents"
- "It increased my value as a human by doing this"

## Related
- [[Louis Knight-Webb]] — speaker, founder of Vibe Canvas/Vibe Kanban
- [[Vibe Kanban]] — the startup/product
- [[Plan and Review Shift]] — the core concept
- [[Plan-Based Approach]] — upfront planning strategy
- [[Review-Based Approach]] — YOLO-then-iterate strategy
- [[Agent Runtime Duration]] — agents running for longer periods
- [[Agent Parallelism]] — running multiple agents simultaneously
- [[Focus Maxing]] — interface design for deep human focus
- [[Plan vs Review Matrix]] — when to use each approach
- [[aiDotEngineer]] — event host
- [[SWE-bench]] — benchmark where Knight-Webb placed ahead of OpenAI
- [[ClaudeCode]] — coding agent used as example
- [[Codex]] — coding agent supported by Vibe Kanban
- [[Cursor]] — coding agent referenced in timeline
- [[GitHubCopilot]] — coding agent referenced in timeline
- [[Playwright]] — tool for browser automation, predicted as next breakthrough
