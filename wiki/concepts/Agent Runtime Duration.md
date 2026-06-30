---
title: "Agent Runtime Duration"
type: concept
tags: [ai, coding-agents, time, workflow, parallelism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban.md"]
last_updated: 2026-06-29
---

## Definition
Agent Runtime Duration is the wall-clock time a coding agent spends executing a task before yielding back to the human. As models improve and tool calling expands, runtimes are increasing from seconds to minutes, crossing a behavioral threshold where humans can no longer simply wait and must adopt new workflows.

## Key Information
- Articulated by Louis Knight-Webb at AIE CODE 2026
- Historical progression of agent runtimes:
  - GitHub Copilot: completes a single line in seconds
  - Original Cursor: completes a single file in ~30 seconds
  - Claude Code (2025): runs for 1-2 minutes
  - Claude Code (2026): runs for 5-10 minutes
- Each new capability adds time but improves accuracy: returning code (fast) → type checking (slower) → testing (slower still) → Playwright MCP (orders of magnitude slower)
- The trade-off is worthwhile: higher accuracy from waiting longer minimizes the human time spent working with the agent
- **The 5-minute threshold**: when agents run longer than ~5 minutes, humans can no longer sit and watch logs or browse Twitter — they must change their behavior
- If runtimes cross an hour threshold, the job of a software engineer fundamentally changes
- The response to increasing runtimes is [[Agent Parallelism]]: running multiple agents simultaneously so that work is always ready for review
- Next predicted breakthrough: AI QA of front-end work via Playwright MCP, which will further increase runtimes but eliminate most of the back-and-forth review cycles

## Related
- [[summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban]] — source
- [[Louis Knight-Webb]] — articulated the concept
- [[Agent Parallelism]] — the workflow response to increasing runtimes
- [[Focus Maxing]] — the design principle for tools handling long runtimes
- [[Plan and Review Shift]] — the broader paradigm shift enabled by longer runtimes
- [[TimeHorizon]] — METR's metric for AI autonomous capability, distinct but related concept
- [[Playwright]] — tool predicted to drive the next runtime increase
