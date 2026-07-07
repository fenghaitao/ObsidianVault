---
title: "summary-2026-06-18 - Claude Code now supports artifacts"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-18 - Claude Code now supports artifacts.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic announced that Claude Code now supports artifacts: live, interactive web pages built from a session's full context (codebase, connectors, conversation) that visualize work progress and auto-update as the session continues. Artifacts translate Claude Code sessions into shareable, collaborative views -- such as PR walkthroughs, incident timelines, dashboards, and release checklists -- so teams spend less time communicating status updates and more time building. Every artifact is private by default, org-gated, versioned at a single URL, and available in beta for Team and Enterprise plans.

## Key Points

- Claude Code artifacts are built from session context (codebase, connectors, conversation) without requiring separate data-source wiring or infrastructure.
- Artifacts auto-update: when Claude Code republishes, the open page refreshes in place, and teammates see updates immediately.
- Each publish creates a new version at the same link, with full version history and a gallery for browsing all artifacts.
- A flagship use case is incident investigation: Claude Code works through logs, publishes a timeline with suspect commits and error-rate charts, and republishes updates as the investigation progresses -- shared via a link before standup.
- Artifacts are private to the author by default; sharing is to authenticated org members only (cannot be made public).
- Admins control access via an org-level toggle, role-based scoping, retention policies, and the compliance API.
- Available in beta to Claude Team and Enterprise orgs, from the Claude Code CLI and desktop app, viewable in any browser.

## Related

- [[ClaudeCode]] -- the product gaining artifacts support
- [[ClaudeArtifacts]] -- the existing Claude.ai artifact feature (distinct product, shared concept)
- [[Artifacts]] -- the broader conceptual pattern
