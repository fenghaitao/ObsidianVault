---
title: "summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI.md"]
last_updated: 2026-07-07
---

## Core Summary

Claude Tag introduces an "agent identity" access model where the AI agent has its own workspace-level credentials and permissions rather than acting on behalf of individual users. This departs from the single-player model (user credentials) and enables secure, team-wide, autonomous AI interactions in shared channels. The model replaces per-user Access Control Lists with channel-scoped agent identities, where admins define a baseline identity at the workspace level and override it per-channel, with RBAC controlling who can invoke Claude. Written by Noah Zweben of the Claude Code team.

## Key Points

- Agent identity gives Claude its own service accounts (Slack app, GitHub App, warehouse service account) rather than borrowing a user's credentials, so shared channels cannot become a side door into private documents.
- Admins define a baseline identity at the workspace level; channels inherit it by default, with channel-level overrides for scoped access (e.g., engineering channel gets GitHub, CRM channel gets the CRM connection).
- Revoking an agent identity terminates Claude's access everywhere that identity was used, simplifying security management compared to auditing individual user accounts.
- Each private channel gets a distinct identity; public channels share a workspace-level identity. Memory and access respect channel boundaries -- what Claude learns in one channel never appears in another.
- Direct messages run on users' individual claude.ai accounts with their own connectors and credentials, making DMs the right place for personal tasks (email drafts, licensed software).
- Anthropic plans future enhancements: just-in-time credential grants for single-action approvals and an identity-aware overlay for organizations with complex clearance structures.
- The teams that get the most value grant Claude generous access from the start and pare back based on admin preferences, extending access one deliberate grant at a time.

## Related

- [[ClaudeTag]] — the multiplayer AI product described in this article
- [[AgentIdentity]] — the access model where agents have their own credentials
- [[MultiplayerAI]] — the paradigm of AI in shared, team-wide channels
- [[Anthropic]] — the company behind Claude Tag
