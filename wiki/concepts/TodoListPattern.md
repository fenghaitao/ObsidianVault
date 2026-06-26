---
title: "TodoListPattern"
type: concept
tags: [coding-agents, prompt-engineering, steerability, ux]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
The todo list pattern is a structured but not structurally enforced mechanism used by Claude Code to keep the agent on track. It is purely prompt-based — injected into the system prompt — rather than enforced in code, relying entirely on the model's instruction-following capability.

## Key Information
- Purely prompt-based, not enforced deterministically in code — would not have worked a year or two ago
- Rules: one task at a time, mark them completed, keep working on in-progress if there are blocks or errors, break up tasks
- Tool descriptions for todos are at the top of the system prompt
- When the user first asks something, the reasoning exports a todo block with version, ID, title, and optional evidence
- IDs are hashes that can be referred to; titles are human-readable
- Four key benefits: (1) forces the model to plan, (2) enables resuming after crashes, (3) provides UX visibility to users, (4) enables steerability
- Jared Zoneraich describes it as "almost a weekend project someone did and it seemed to work"
- The fact that it works purely through prompting demonstrates how much better models have become at instruction following
- Represents a new "first class paradigm" that could inspire future agent design patterns

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — primary example
- [[MasterWhileLoop]] — the architecture that uses todos
- [[SimpleDesignPhilosophy]] — the philosophy of prompt-based over code-based enforcement
