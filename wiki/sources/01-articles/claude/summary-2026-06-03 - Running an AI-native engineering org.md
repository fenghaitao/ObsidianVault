---
title: "summary-2026-06-03 - Running an AI-native engineering org"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md"]
last_updated: 2026-07-07
---

## Core Summary

Fiona Fung, Director of Engineering for [[ClaudeCode]] and [[ClaudeCowork]] at [[Anthropic]], delivered this talk at Code w/ Claude SF 2026 about how the Claude Code engineering team rewrote their processes once agentic coding became the default way of working. The core thesis: when agentic coding eliminates coding as the bottleneck, new constraints emerge — verification, code review, and security — and engineering orgs must actively rewrite norms around planning, code ownership, review, and team structure rather than letting obsolete processes persist.

## Key Points

- **Bottleneck shift:** Engineering bandwidth used to be the scarce resource driving heavy pre-planning (waterfall, agile). Now coding, testing, and refactoring rarely slow the team down — verification, code review, and security took their place.
- **JIT planning:** The team moved from six-month roadmaps (stale by month three due to Claude Code's own speed) to just-in-time planning — doing just the right amount of planning at the right time, shifting away from design docs toward PRs and prototypes.
- **Code ownership redefined:** Since all PRs are assisted by Claude, "who made this change" is no longer sufficient. The new norm: ask what you actually need to know (regression cause, expert lookup, context on a decision) and ask Claude first, with more data and context.
- **Automate everything possible:** Every question triggers the follow-up "Is there a way to automate it?" — exemplified by replacing a manual morning ritual of summarizing customer feedback with an automated background routine.
- **Human-in-the-loop where it matters:** Claude handles style, linting, PR feedback, bug fixes, and test authoring via [[CodeReview]]. Humans remain essential for legal review, security-sensitive/trust-boundary code, and product sense/taste — but the right balance keeps changing as models improve.
- **Role blurring:** PMs code more; engineers do content and design; nontraditional coders do more engineering. The team indexes on two profiles: creative builders with product sense, and engineers with deep systems expertise — raw throughput is de-emphasized.
- **Pod autonomy within core principles:** Non-negotiable team principles exist, but each pod has agency over how they use Claude for triage, planning rituals, standups, and which workflows get "Claudified" first.
- **Metrics to track:** Onboarding ramp-up time, PR cycle time, and share of Claude-assisted commits — alongside product outcomes, not just raw throughput.
- **Practical takeaway:** Pick your noisiest (most dreaded/expensive) workflow, ask whether it still serves its purpose, and if so, automate it — illustrated by canceling an expensive weekly status-report meeting once the team realized it wasn't needed.

## Related

- [[AINativeEngineeringOrg]] — the central concept of adapting engineering org structure to AI
- [[JustInTimePlanning]] — JIT planning methodology
- [[FionaFung]] — the speaker, Director of Engineering for Claude Code and Claude Cowork
- [[ClaudeCode]] — the tool and team
- [[ClaudeCowork]] — the knowledge-worker product
- [[AgenticCoding]] — the paradigm shift driving these org changes
- [[CodeReview]] — the automated review product used heavily by the team
- [[Anthropic]] — the company
- [[summary-13 - Running an AI-native engineering org]] — the San Francisco transcript version of the same talk
- [[summary-03 - Running an AI-native engineering org]] — the London transcript version of the same talk
