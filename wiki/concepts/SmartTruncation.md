---
title: "SmartTruncation"
type: concept
tags: [context-management, agents, memory, truncation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md"]
last_updated: 2026-06-29
---

## Definition
Smart truncation is a context management technique that preserves the head (beginning) and tail (end) of a conversation while truncating the middle and storing it in a memory store that the agent can retrieve from on demand. It combines truncation with compression and memory to give the agent control over what context is important.

## Key Information
- Developed by Arize for their AI agent Alex after naive truncation (first N chars only) and summarization both failed.
- Keeps the first ~100 characters (head) and last ~100 characters (tail) of context, and stores the truncated middle in a memory store.
- The agent can retrieve from the memory store at any point if it determines a past tool call or message was important.
- Deduplicates messages and keeps only the latest tool call results.
- Never resets the system prompt — it stays intact across truncations.
- Gives the agent agency over what context to retrieve, rather than the system making assumptions about importance.
- Arize has not needed to modify this strategy for several months, though they are now revisiting as conversations grow longer.
- Claude Code reportedly uses a similar truncation and compression strategy.

## Related
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — source
- [[Context Management]] — parent discipline
- [[ContextEngineering]] — broader paradigm
- [[Agent Memory]] — memory store used for truncated content
- [[ContextSelection]] — heuristics for what to keep
- [[SubAgents]] — complementary technique for offloading heavy context
- [[LongSessionEvals]] — evaluation technique used alongside smart truncation
- [[ClaudeCode]] — uses similar truncation strategy
