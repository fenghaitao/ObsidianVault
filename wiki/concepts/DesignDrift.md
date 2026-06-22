---
title: "DesignDrift"
type: concept
tags: [design, ui, ai-coding, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260605 - Why apps built with AI look a little... OFF.md]
last_updated: 2026-06-22
---

## Definition

Design drift is the gradual inconsistency that accumulates in AI-built applications when each coding session reinvents the UI from scratch. Without a shared design source of truth, buttons don't match, spacing varies, heading sizes differ — and the app visibly looks "AI-built."

## Key Information

- Root cause: AI agents lack a shared sense of what the app should look like. Each session makes independent design decisions.
- Symptoms: mismatched buttons, inconsistent spacing, varying heading sizes, different form styles across pages.
- Not a prompting problem — it's a missing infrastructure problem.
- Solution: a living [[DesignSystem]] baked into the codebase, enforced through CLAUDE.md directives.
- The design system provides design tokens (color classes, typography, spacing) and documented components that agents reference instead of inventing ad-hoc styles.
- Key rule: "Don't invent ad-hoc hex values or font sizes. Use the existing design tokens."
- Best installed on day one of a new app to prevent drift from the start.

## Related

- [[DesignSystem]] — the solution (Brian's free skill)
- [[BrianCasel]] — diagnostician
- [[CLAUDE.md]] — where enforcement rules live
- [[ClaudeCode]] — the agent that needs the rules
- [[BuildNew]] — starter template with design system pre-installed
