---
title: "Memento Pattern for LLMs"
type: concept
tags: [ai, llm, context-window, context-management, coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Matt Pocock's analogy that LLMs behave like Leonard Shelby, the protagonist from the film Memento, who cannot form new memories and continually resets to a base state. Rather than fighting this property through compacting, Pocock argues developers should embrace and optimize for it.

## Key Information
- Every LLM session goes through the same stages: system prompt, exploratory phase, implementation, testing/feedback loops
- When context is cleared, the LLM returns exactly to the system prompt — a predictable, reproducible state
- Pocock prefers this over compacting because the reset state is always identical, making behavior more predictable
- The system prompt should be kept as small as possible. Large system prompts (e.g., 250K tokens) push the LLM straight into the Dumb Zone before any work begins
- Optimizing for the reset means designing workflows where each fresh session can be productive from the base state
- This is one of two fundamental LLM constraints Pocock builds his workflow around (the other being the Smart Zone and Dumb Zone)

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — creator of the analogy
- [[Compacting]] — the alternative approach Pocock rejects
- [[Smart Zone and Dumb Zone]] — the other fundamental constraint
- [[Context Management]] — broader context strategies
- [[SystemPromptFeedbackLoop]] — related concept
