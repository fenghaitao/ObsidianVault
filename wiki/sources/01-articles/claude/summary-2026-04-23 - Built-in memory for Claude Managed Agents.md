---
title: "summary-2026-04-23 - Built-in memory for Claude Managed Agents"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-23 - Built-in memory for Claude Managed Agents.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic announced that memory on [[ClaudeManagedAgents]] is now available in public beta, letting agents learn across sessions via a file-system-based, intelligence-optimized memory layer. Because memories are stored as ordinary files, developers can export them, manage them through the API, and retain full control over what agents retain, with scoped permissions (e.g. read-only org-wide stores vs. read-write per-user stores), audit logs, version rollback, and redaction. Multiple agents can work concurrently against the same store without overwriting each other's writes, and updates surface in the Claude Console as session events. The article showcases four customers — Netflix, Rakuten, Wisedocs, and Ando — using memory to close feedback loops, speed up verification, and replace custom retrieval infrastructure. Memory is available today via the Claude Console or a new CLI.

## Key Points

- Memory mounts directly onto a filesystem so Claude can use the same bash/code-execution tools it already relies on for agentic tasks; latest models (referencing Opus 4.7) are described as better at saving comprehensive, well-organized file-system-based memories and being more discerning about what to retain.
- Built for enterprise deployment: scoped permissions, audit logs, full programmatic control; stores can be shared across multiple agents with different access scopes (e.g. org-wide read-only, per-user read-write).
- Memories are exportable files, independently manageable via API; every change is tracked in a detailed audit log identifying which agent/session produced it; rollback to earlier versions and redaction of history are both supported.
- Console surfaces memory updates as session events so developers can trace what an agent learned and where it came from.
- Customer usage: Netflix carries context across sessions (including multi-turn insights and mid-conversation human corrections) instead of manually updating prompts/skills; Rakuten's task-based long-running agents cut first-pass errors by 97% using cross-session memory within workspace-scoped, observable boundaries; Wisedocs built a document-verification pipeline using cross-session memory to spot and remember recurring document issues, speeding up verification by 30%; Ando is building a workplace messaging platform on Managed Agents, using memory to capture how each organization interacts instead of building memory infrastructure themselves.
- Generally available today in public beta on the Claude Platform, accessible via the Claude Console (workspaces/default/memory-stores) or a new CLI; documentation published at platform.claude.com/docs/en/managed-agents/memory.
- Anomaly: the raw file's customer bullet list has minor scrape artifacts (missing spaces/stray characters, e.g. "**Netflix**agents" and a stray "- ****" after the Wisedocs bullet) — boilerplate formatting noise from the page scrape, not prompt injection; no injected instructions were present in this source and none were followed.

## Related

- [[ClaudeManagedAgents]] — the platform this memory feature ships on
- [[AgenticMemory]] — the underlying concept of file-system-based agent memory and dreaming
- [[Rakuten]] — customer cited with a 97% first-pass error reduction
- [[Netflix]] — customer cited for cross-session context continuity
