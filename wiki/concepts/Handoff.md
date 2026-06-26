---
title: "Handoff"
type: concept
tags: [context-management, coding-agents, amp-code, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Handoff is Amp Code's context management technique that starts a fresh agent thread with only the necessary context, rather than compacting (summarizing) an existing long conversation. The analogy is switching weapons in Call of Duty — it's faster than reloading. Jared Zoneraich considers this potentially the winning strategy for context management.

## Key Information
- Alternative to "compact" — the standard technique of summarizing chat history when context gets too high
- Compact is described as "the worst" — users have to wait ~10 seconds with no clear reason for the delay
- Handoff starts a new thread and gives it only the information it needs, avoiding the overhead of summarization
- Analogy: in Call of Duty, switching weapons is faster than reloading
- Zoneraich speculates you might need both compact and handoff, but handoff "feels like the winning strategy"
- Represents a "very fresh perspective" from Amp Code on context management
- Related to sub-agent patterns where each sub-agent starts with a blank slate

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[AmpCode]] — the agent that implements handoff
- [[Sourcegraph]] — company behind Amp Code
- [[Context Management]] — the broader problem handoff addresses
- [[ContextCompression]] — the alternative approach (compact)
- [[SubAgents]] — related pattern of fresh context windows
- [[AgentHandoffs]] — distinct concept: OpenAI Agents SDK feature for agent-to-agent transfer within a single agentic loop
