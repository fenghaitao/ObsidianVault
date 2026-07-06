---
title: "summary-2026-04-15 - Using Claude Code session management and 1M context"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-15 - Using Claude Code session management and 1M context.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic (via Claude Code team member Thariq Shihipar) published a practical guide to session and context management in Claude Code, prompted by the new `/usage` slash command and recurring customer confusion about how to work with the 1M-token context window. The core argument: session/context choices (continue, `/rewind`, `/compact`, `/clear`, or delegate to a subagent) shape output quality more than users expect, because context accumulation causes "context rot" — degraded attention and performance as the context window fills, even though 1M tokens gives more headroom before a hard cutoff forces automatic compaction. The article gives a decision framework: start a new session per new task; use `/rewind` to correct a failed approach without losing earlier useful context; choose `/compact` (lossy auto-summary, less user effort, can be steered with instructions) vs. `/clear` (manual restart, more effort, more precise) based on how much of the accumulated context is still relevant; and delegate to subagents when a chunk of work will produce a lot of intermediate output whose tool calls/outputs won't be needed again, only the conclusion.

## Key Points

- **`/usage`**: new slash command showing a user's Claude Code usage, introduced partly to surface the wide variance in how people manage sessions.
- **Context window definition reiterated**: everything the model can see at once — system prompt, conversation, tool calls/outputs, files read; Claude Code's context window is 1 million tokens.
- **Context rot**: model performance degrades as context grows because attention spreads across more tokens and older/irrelevant content distracts from the current task; larger (1M) windows push out the hard cutoff but don't eliminate context rot.
- **Auto-compaction**: fires automatically near the context limit, summarizing the task into a smaller description so work continues in a new context window.
- **New-session rule of thumb**: start a new session when starting a new task; 1M context enables longer, more reliable single-session tasks (e.g., building a full-stack app from scratch) but context rot can still creep in.
- **When to keep context**: related follow-on tasks (e.g., writing docs for a feature just implemented) may warrant staying in the same session rather than forcing Claude to reread files it just touched (slower, more expensive).
- **`/rewind` (double-tap Esc)**: jumps back to any previous message, dropping everything after it from context. Recommended over "that didn't work, try X" — instead rewind to just after the relevant reads and re-prompt with the learning ("don't use approach A, go straight to B"). Can also be used with a "summarize from here" style handoff message, like a note from a past iteration of Claude to itself.
- **`/compact` vs `/clear`**: both shed extraneous context but differently — `/compact` asks the model to self-summarize and replace history (lossy, low effort, steerable with instructions like "focus on the auth refactor, drop the test debugging"); `/clear` requires the user to manually write down what matters and start clean (more effort, more precise/controlled result).
- **Bad compacts**: happen when the model can't predict the direction of future work — e.g., autocompact fires after a long debugging session, summarizes the investigation, and then a follow-up like "now fix that other warning in bar.ts" fails because that warning was dropped from the debugging-focused summary. Compounded by context rot: the model is at its least intelligent point right when compaction happens. With 1M context, there's more room to proactively `/compact` with an explicit description of the next intended direction, rather than waiting for autocompact.
- **Subagents**: spawned via the Agent tool, each gets its own fresh context window, does its work, and returns only a synthesized final report to the parent — good when a chunk of work will generate a lot of intermediate output that won't be needed again. Mental test given: "will I need this tool output again, or just the conclusion?" Claude Code can invoke subagents automatically, but users may want to explicitly direct it to do so.
- **Anomaly (scrape artifact, not a prompt injection)**: the raw source is a scraped web page and has visible boilerplate/structural loss — a promised "helpful table that outlines common situations, what tool to reach for, and why" is referenced in the prose but its actual table content is missing from the scrape; a list of the "five options after Claude finishes a turn" is similarly garbled (only `/rewind` and `/clear` render as text, the other three/labels are missing); and the page ends with generic newsletter-signup boilerplate ("Get the developer newsletter..."). None of this resembles an instruction-injection attempt — just lossy scraping — but it means the article's full "situations to tool" mapping table is not recoverable from this source.
- **Author**: Thariq Shihipar, member of technical staff at Anthropic working on Claude Code (same author as the April 10, 2026 "Seeing like an agent" tool-design article already in the wiki).

## Related

- [[ClaudeCode]] — the tool this session-management guidance applies to
- [[ContextWindow]] — the underlying constraint (1M tokens, context rot) this article elaborates on
- [[ClaudeCodeSubagents]] — subagent delegation pattern discussed as a context-management tool
