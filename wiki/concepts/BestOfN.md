---
title: "BestOfN"
type: concept
tags: [agents, model-comparison, parallelization, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Best of N is a pattern where the same task is given to N different models simultaneously, each working in its own isolated environment. A judge (either automated or the parent agent) compares the results and helps the user choose the best implementation. Users can also ask the parent agent to stitch together pieces from different implementations.

## Key Information

- Originally implemented in Cursor 2.0 as a code-heavy feature alongside work trees
- Re-implemented as a ~40-line markdown skill using sub-agents and work trees
- The parent agent spins up sub-agents for each model, each in its own work tree
- After all sub-agents finish, the parent agent provides commentary comparing implementations, grading them, and helping the user choose
- The parent agent can stitch together pieces from different implementations (e.g., "I like this part from Opus and this part from GPT")
- The new skill-based implementation provides superior judging compared to the old code-based version because the parent agent has more context
- The /bestofn command is server-controlled, allowing Cursor to iterate prompts without user updates

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[GitWorktrees]] — the isolation mechanism
- [[SubAgents]] — the architectural pattern used
- [[LLMAsJudge]] — the judging mechanism
- [[Parallel Agents]] — the broader pattern
- [[Cursor]] — the product
