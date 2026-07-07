---
title: "Artifacts"
type: concept
tags: [artifacts, interactive-apps, no-code, agentic-coding, claude-ai]
sources: ["raw/01-articles/claude/2025-06-25 - Turn ideas into interactive AI-powered apps.md", "raw/01-articles/claude/2025-11-12 - Improving frontend design through Skills.md", "raw/01-articles/claude/2026-03-12 - Claude now creates interactive charts, diagrams and visualizations.md", "raw/01-articles/claude/2026-06-18 - Claude Code now supports artifacts.md"]
last_updated: 2026-07-07
---

## Definition

Artifacts is the conceptual pattern behind Claude's ability to generate standalone, viewable, and shareable content (code, documents, interactive UIs) directly from a conversation — and, since mid-2025, to make those creations interactive AI-powered apps rather than static one-off outputs. The concrete product feature implementing this pattern is [[ClaudeArtifacts]].

## Key Information

- Turns anyone into an app creator without coding: users describe an idea in natural language and Claude produces a shareable app, tool, or game.
- Since the original (non-interactive) launch, users have created over half a billion artifacts, spanning productivity tools to educational games.
- **From static to interactive**: the June 2025 update let artifacts embed AI capabilities directly, so an artifact can call Claude itself — e.g., a flashcard app that generates new cards on any topic a user names, instead of one fixed set of flashcards.
- A dedicated **artifacts space** in the Claude app sidebar (June 2025) makes browsing, creating, and customizing artifacts a first-class experience.
- Illustrative example: musician Rick Rubin's "The Way of Code," pairing 81 meditations with interactive artifacts that anyone can reshape through conversation with Claude.
- Reflects a broader shift where "conversation itself becomes a form of creative expression," part of the same [[NoCodeDevelopment|no-code]] and [[AgenticCoding|agentic-coding]] trend of dissolving the line between describing an idea and building it.

### Distinction from In-Line Visualizations (March 2026)

Claude gained a separate, beta capability (built on the earlier "Imagine with Claude" preview) to build custom interactive charts, diagrams, and visualizations directly in-line within chat responses — distinct from Artifacts. Artifacts are permanent, polished creations meant to be shared or downloaded in a side panel; in-line visualizations are temporary aids to understanding that appear inline as part of the live discussion and change or disappear as the conversation evolves (e.g., an interactive compound-interest curve or a clickable periodic table). On by default; Claude decides when a visual helps, or a user can request one directly. Available on all plan types (Cowork added April 2026).

### Architectural Constraint and the web-artifacts-builder Skill (November 2025)

Because artifacts must render as a single HTML file, Claude's default behavior is to hand-write one file of HTML/CSS/JS — limiting the complexity of frontends it can produce, much as a human developer would be limited to basic frontends if restricted to a single file. The **web-artifacts-builder** [[ClaudeCodeSkills|Skill]] removes this constraint: it exposes scripts that set up a React project and bundle it (via Parcel) back into the required single-HTML-file format, letting Claude build artifacts with React, Tailwind CSS, and shadcn/ui components. Users enable the skill and ask Claude to "use the web-artifacts-builder skill" when building artifacts in [[Claude.ai]].

### Claude Code Artifacts (June 2026)

The artifacts concept was extended to [[ClaudeCode]] in June 2026, taking a distinct form: live, interactive web pages built from a session's full context (codebase, connectors, conversation) that visualize work progress and auto-update as the session continues. Unlike Claude.ai artifacts (user-described interactive apps), Claude Code artifacts translate agent sessions into collaborative, context-rich views -- such as PR walkthroughs, incident timelines, dashboards, and release checklists. This represents a second major branch of the artifacts pattern: from "describe an app and Claude builds it" (Claude.ai) to "Claude builds a live report from what the session already knows" (Claude Code). Artifacts are private to the author by default, org-gated, versioned at a single URL, and available in beta for Team and Enterprise plans.

See [[summary-2026-06-18 - Claude Code now supports artifacts]].

## Related

- [[ClaudeArtifacts]] — the concrete Claude product feature implementing this concept
- [[ClaudeCode]] — product where the artifacts concept was extended (June 2026)
- [[Claude.ai]] — the platform hosting the artifacts space
- [[AgenticCoding]] — broader paradigm of AI-driven, conversational software creation
- [[NoCodeDevelopment]] — paradigm for building applications without writing code
- [[summary-2025-06-25 - Turn ideas into interactive AI-powered apps]] — source announcement introducing the artifacts space and interactivity
- [[ClaudeCodeSkills]] — mechanism behind the web-artifacts-builder skill
- [[summary-2025-11-12 - Improving frontend design through Skills]] — web-artifacts-builder skill and frontend design skill
- [[Integrations]] — MCP Apps interactive connectors, part of the same broader response-format push
- [[summary-2026-03-12 - Claude now creates interactive charts, diagrams and visualizations]] — in-line visualizations announcement
- [[summary-2026-06-18 - Claude Code now supports artifacts]] — Claude Code artifacts announcement
