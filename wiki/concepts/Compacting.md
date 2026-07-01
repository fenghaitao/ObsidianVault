---
title: "Compacting"
type: concept
tags: [ai, llm, context-window, context-management, coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Compacting is a technique where an LLM session's conversation history is summarized and compressed into a much smaller token space, allowing the session to continue without clearing context entirely. It creates a written record of what happened rather than preserving the full conversation.

## Key Information
- Compacting squeezes all information from a session into a compact summary, reducing token usage
- Many developers like compacting, but Matt Pocock dislikes it
- Pocock's objection: compacting creates a variable, unpredictable state. Each compact produces a different summary, making the LLM's behavior less reproducible
- Pocock prefers clearing context entirely and returning to the base system prompt because "this state is always the same" — predictable and optimizable
- He compares LLMs to the protagonist from the film Memento: they continually reset to a base state, and this is a feature to optimize for, not a bug
- Compacting is diagrammed as taking all session information and creating a "history" or written record from it
- Essential to know exact token count during coding sessions to understand proximity to the Dumb Zone

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — critiques compacting
- [[Smart Zone and Dumb Zone]] — the reason compacting exists
- [[Memento Pattern for LLMs]] — Pocock's preferred alternative
- [[Context Management]] — broader context strategies
- [[AutoCompaction]] — automated version
- [[ContextCompression]] — related technique
