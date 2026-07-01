---
title: "Retrospective Agent"
type: concept
tags: [agentic-engineering, self-improvement, memory, agent-harness, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

A retrospective agent is the final stage in an agent pipeline that analyzes the entire run's performance, identifies improvement opportunities, and updates the harness's memory system so future runs avoid repeating the same mistakes.

## Key Information

- Implemented as the final stage in Case (Nick Nisi's agent harness at WorkOS)
- Analyzes the complete run by reading logs and JSONL transcript files (Claude/Codex transcripts)
- Detects patterns: running the same tool request multiple times without changes, doom loops, wasted parallel tool calls
- Writes lessons learned into memory files organized by project/framework (general, Next.js, TanStack Start, etc.)
- Example: If Case broke TanStack Start's implicit `start.ts` contract, the retro agent records this in the TanStack Start memory file so future runs know about the gotcha
- Future direction: Nick plans to add Claude's auto-dream/pruning capability to keep memory files from growing unbounded
- The retro agent also accepts human feedback — users can provide corrections that get incorporated into memory
- Part of the "every failure becomes data for the next run" philosophy: don't fix the code, fix the harness so it learns
- The retrospective is enforced by the state machine — it cannot be skipped

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — implemented in Case
- [[Case]] — agent harness with retro agent
- [[State Machine Gates]] — the enforcement mechanism
- [[Agent Memory]] — what the retro agent updates
- [[Gotchas]] — what the retro agent captures
- [[DoomLoop]] — what the retro agent detects
- [[SelfImproving Agents]] — the broader category
- [[Harness Engineering]] — the discipline
