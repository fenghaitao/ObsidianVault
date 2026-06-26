---
title: "IncrementalDisclosure"
type: concept
tags: [context-management, agents, discovery, performance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Incremental disclosure is a context management pattern where an AI agent discovers relevant context progressively rather than having all information loaded upfront. It trades some latency for lower context usage and greater flexibility.

## Key Information
- Heard frequently at the AI Engineer conference as a recommended pattern
- Principle: don't load too much at the beginning of the conversation; let the agent self-discover the right context for the task
- Kiro uses this approach: the agent is given tools to find things rather than being loaded with all context upfront
- Based on benchmarks showing agents perform better with less initial context but with tools to discover what they need
- Contrasts with loading everything into the system prompt at session start
- Related to Kiro's codebase indexing: the index is used for secondary effects (code search, UI features) rather than being dumped into agent context

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[ProgressiveContextDisclosure]] — closely related concept from Claude Agent SDK
- [[Context Management]] — broader category
- [[AmazonKiro]] — IDE using this approach
