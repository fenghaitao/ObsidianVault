---
title: "DesignSystem"
type: entity
tags: [tool, agent-skill, design, ui, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260605 - Why apps built with AI look a little... OFF.md]
last_updated: 2026-06-22
---

## Definition

Brian Casel's free open-source agent skill that installs a living design system directly into an application's codebase. It provides a documented component library (colors, typography, buttons, forms, etc.) and CLAUDE.md directives that instruct coding agents to always reference the design system before writing UI code, preventing design drift.

## Key Information

- Available at buildermethods.com/tools and via the Claude Code plugin marketplace as "BM Design System."
- Installs: a design system documentation page (accessible at `/admin/design_system`), CLAUDE.md directives, base CSS styles.
- Component catalog: colors (with design tokens like `bg-accent`, `text-ink-body`), typography, application shell/navigation, buttons (primary, secondary, ghost, danger), forms, toggles, badges, listings, modals, dropdowns, Kanban boards.
- Design tokens use generic class names so changing one color in the design system page changes it everywhere.
- CLAUDE.md rules: always check design system first, use existing design tokens, don't invent ad-hoc hex values or font sizes, use semantic HTML.
- Best installed on day one of a new app; retrofitting is possible but harder.
- Built into the [[BuildNew]] starter template.
- Components include usage guidance (when to use, when not to use) and sample code.
- Not a rigid library — agents can tweak details while working from the same base; reminders like "use our primary button style" suffice.

## Related

- [[BrianCasel]] — creator
- [[BuildNew]] — starter template with design system built in
- [[DesignDrift]] — the problem it solves
- [[ClaudeCode]] — the coding agent it targets
- [[CLAUDE.md]] — where the directives live
