---
title: "MultiRepoWorktrees"
type: concept
tags: [git, worktrees, agents, cursor, multi-repo]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Multi-Repo Worktrees extend the Git work tree pattern to span multiple repositories simultaneously. When a user has a multi-repo setup (e.g., separate frontend and backend repos), the agent creates a work tree on each repo, and opening a PR creates one PR per repo.

## Key Information

- The old Cursor work tree implementation did not support multi-repo setups — it was simply disabled
- The new skill-based /worktree command works across multiple repos
- The agent creates a work tree on each repo in the multi-repo setup
- Opening a PR from a multi-repo work tree creates separate PRs for each repo
- This was cited as a major advantage of the new markdown-based implementation over the old code-based one

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[GitWorktrees]] — the underlying mechanism
- [[Cursor]] — the product
