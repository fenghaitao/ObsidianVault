---
title: "summary-apps-built-with-ai-look-off"
type: source
tags: [source, brian-casel, design-system, design-drift, ui]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260605 - Why apps built with AI look a little... OFF.md]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel diagnoses "design drift" — the phenomenon where AI-built apps look inconsistent because agents lack a shared design source of truth and reinvent the UI each session. His solution: a living design system baked into the codebase (not static Figma mockups), enforced through CLAUDE.md directives. He released a free Design System agent skill that installs a documented component library with design tokens (colors, typography, spacing, components) and CLAUDE.md rules that instruct the agent to always check the design system before writing UI code.

## Key Points

- Design drift: every AI session reinvents UI from scratch because there's no shared design source of truth.
- A design system is a set of decisions made once: colors, type, spacing, buttons, forms — defined in one place, referenced everywhere.
- The key shift: build the design system into the codebase itself (real components, real styles), not as mockups in Figma.
- The Design System skill installs: a documented component library page (colors, typography, shell, navigation, buttons, forms, badges, listings, modals), CLAUDE.md directives, and base styles.
- CLAUDE.md rules: always check the design system first, use existing design tokens, don't invent ad-hoc hex values or font sizes, use semantic HTML.
- Design tokens use generic class names (e.g., `bg-accent`, `text-ink-body`) so changing one color changes the entire app.
- Install the design system on day one of a new app; retrofitting is possible but harder.
- Brian's Build New starter template comes with the design system pre-installed.
- The design system is not a rigid component library — agents can tweak details while working from the same base.

## Related

- [[BrianCasel]] — creator and author
- [[DesignDrift]] — the problem being solved
- [[DesignSystem]] — the free skill and methodology
- [[BuildNew]] — the starter template with design system built in
- [[ClaudeCode]] — the coding agent
- [[CLAUDE.md]] — where design system directives live
- [[SpecDrivenDevelopment]] — the broader methodology
