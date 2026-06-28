---
title: "ClaudeMemory"
type: concept
tags: [memory, claude-app, persistence, context, team, enterprise]
sources: ["raw/01-articles/claude/2025-09-11 - Bringing memory to Claude.md"]
last_updated: 2026-06-28
---

## Definition

Claude Memory is a persistent cross-conversation memory feature in the Claude app that enables Claude to remember users' and teams' professional context, project details, preferences, and work patterns across sessions. Unlike conversation history (which lists past chats), memory is a distilled summary of learned context that Claude actively draws on to provide continuity and reduce the need to re-explain context.

## Key Information

- **Project-scoped isolation:** Each project in the Claude app has its own separate memory, preventing unrelated contexts from mixing (e.g., product launch planning stays separate from client work; confidential discussions remain separate from general operations).
- **Memory summary:** All memories are captured in a single summary visible in Settings. Users can view, update, or direct Claude to focus on or ignore specific details by chatting with Claude.
- **Work-focused design:** Memory is optimized for professional context — team processes, client needs, project specifications, and priorities — rather than personal or sensitive conversations.
- **Plan availability:**
  - Initially: [[ClaudeTeamPlan|Team]] and [[ClaudeEnterprise|Enterprise]] plans (September 11, 2025)
  - Expanded to: Pro and [[ClaudeMax|Max]] plans (October 23, 2025)
- **Safety-first rollout:** Anthropic conducted extensive safety testing before launch, covering whether memory could reinforce harmful patterns, lead to over-accommodation, or enable safeguard bypass. Targeted refinements were made before release.
- **Enterprise admin control:** Enterprise admins can disable memory organization-wide at any time.
- **Import/export:** Memory can be imported from other AI tools or exported for backup and migration.
- **Phased approach:** Anthropic deliberately started with work settings before expanding to evaluate how memory behaves across different use patterns.
- **Incognito chat:** Users can opt out of memory for individual conversations using [[IncognitoChat]], available to all Claude users.

## Relationship to Agentic Memory

Claude app Memory differs from [[AgenticMemory]] (memory for autonomous agent systems):
- Claude app Memory is user-facing and cross-conversation; agentic memory is file-system-based and used by autonomous agents during task execution.
- Claude app Memory is managed via a summary in Settings; agentic memory uses runbooks, per-agent working files, and a "dreaming" batch optimization process.
- Both address the same fundamental challenge — retaining context across sessions — but at different layers of the stack.

## Related

- [[IncognitoChat]] — private chat mode that bypasses memory
- [[ClaudeTeamPlan]] — first plan to receive memory (September 2025)
- [[ClaudeEnterprise]] — enterprise plan with memory and admin disable controls
- [[ClaudeMax]] — premium individual plan; received memory October 2025
- [[AgenticMemory]] — memory for autonomous agent systems (distinct concept)
- [[ContextWindow]] — the in-session context constraint that memory helps address across sessions
- [[Anthropic]] — creator of the feature
- [[summary-2025-09-11 - Bringing memory to Claude]] — source article
