---
title: "Design System"
type: concept
tags: [ui, design, components, patterns, consistency, agent-workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

A Design System is a documented library of UI components, patterns, and rules that defines the visual language of an application. It was the way to build consistent UIs before AI and remains the way to build consistent UIs with AI agents.

## Key Information

- "Making consistent UIs with agents is just another level of hard" — design systems are essential for agent-generated UI
- A design system documents: the visual language (e.g., primary button is blue, has this shape, this color, this size), rules (e.g., only one primary button visible per page at any time), and components with their states
- Components are defined with previews and snippets so both humans and agents can see them
- Build from small pieces into bigger ones, compose and reuse — same principle as code
- Rules can be enforced: for example, "no inline styles anywhere else" — if an agent tries to use inline styles, the lint rule catches it and links back to the design system
- The design system becomes another set of documents in the Decision Capture Loop, enforced by the same git hooks, linters, and CI checks
- Without a design system, UI generation by agents produces chaos — just like code without architecture

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[Decision Capture Loop]] — the enforcement mechanism that applies design system rules
- [[Architecture Enforcement]] — how design system rules are enforced (e.g., no inline styles)
- [[Architecture Decision Record (ADR)]] — design system is a form of architectural decision
- [[GenerativeUI]] — related concept for AI-generated UI
- [[Enforce Dont Instruct]] — design systems embody this principle for UI
