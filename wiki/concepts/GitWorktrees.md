---
title: "GitWorktrees"
type: concept
tags: [git, parallelization, agent-isolation, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Git work trees are separate checkouts of a repository that allow parallel work without interference. In Cursor, they enable multiple agents to work on different tasks simultaneously, each in its own isolated checkout, with commands and file operations scoped to that work tree.

## Key Information

- Allow separate checkouts of the same repo so different agents can work in parallel without interfering with each other
- Each work tree shows the same files but with different content depending on what the agent is doing
- Agent commands, lints, and file operations are isolated and scoped to the work tree
- Agents can open PRs directly from a work tree with the changes produced inside it
- Enable "best of N" pattern: give the same task to different models in separate work trees and compare results
- Shipped in Cursor 2.0 (October 2025) with significant code complexity (~15,000 lines)
- Cursor later replaced the code-based implementation with a markdown skill (~200 lines) using /worktree and /bestofn commands
- Limitations: can be slow to create, use significant disk space, and only work in Git repos
- Cursor is exploring non-Git parallelization primitives for the future

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Cursor]] — the product
- [[BestOfN]] — pattern enabled by work trees
- [[AgentIsolation]] — the isolation work trees provide
- [[MultiRepoWorktrees]] — work trees spanning multiple repos
- [[Parallel Agents]] — the broader pattern
