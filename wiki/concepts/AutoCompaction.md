---
title: "Auto-compaction"
type: concept
tags: [ai, context-engineering, codex, openai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Auto-compaction is the ability of coding agents to automatically manage and compress their context window during long-running tasks, paging out less relevant information while retaining critical context. GPT 5.4 and Codex brought significant improvements to this capability.

## Key Information
- GPT 5.4 and Codex are described by Ryan Lopopolo as "fantastic at auto compaction"
- Makes manual context resets (e.g., `/new` in Claude Code) largely unnecessary
- Engineers must build for the expectation that context will get paged out over time during long tasks
- Requires continually refreshing context as the agent works — via reviewer agents, lint failures, and test assertions that re-inject requirements
- Related to just-in-time context surfacing: don't front-load all instructions; surface them when relevant

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Codex]] — coding agent with strong auto-compaction
- [[GPT 5.2]] — predecessor model
- [[Context Management]] — broader topic
- [[JustInTime Context Surfacing]] — complementary pattern
- [[ProgressiveContextDisclosure]] — related concept
