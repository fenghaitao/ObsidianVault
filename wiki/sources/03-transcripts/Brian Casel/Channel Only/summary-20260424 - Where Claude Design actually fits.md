---
title: "summary-20260424 - Where Claude Design actually fits"
type: source
tags: [source, brian-casel, claude-design, design-tool, workflow]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260424 - Where Claude Design actually fits.md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel evaluates Anthropic's Claude Design tool and concludes it's not an idea-to-ship tool and not a design layer for existing codebases. However, it's genuinely useful for two things: creating on-brand marketing assets (animations, slide decks) and visual ideation during the earliest shaping phase of a new product. He argues the handoff from Claude Design to Claude Code is disjointed — it produces mockups without specs, plans, or integration context.

## Key Points

- Claude Design runs Claude Code under the hood; design quality is similar to what you'd get with good prompting in Claude Code.
- The "tweaks" feature lets you toggle design options, but may embed tweaking logic into exported code.
- Handoff to Claude Code is a URL link to the design project — no spec, no plan, no tech stack decisions, no integration instructions.
- Brian's preferred approach: build a living design system directly in the codebase (via CLAUDE.md), not in a separate design tool.
- Use case 1 (visual ideation): mock up ideas visually, screenshot them, paste into Claude for shaping conversations. This helps non-designers visualize before locking into specs.
- Use case 2 (marketing assets): create on-brand animations and slide decks using a minimal design system (just colors + typography).
- Brian created a brand design system in Claude Design with only typography and colors — no components — for generating marketing assets.
- Slide deck feature includes speaker notes and presentation mode.
- Ironically, Brian built a custom animation tool the week before Claude Design dropped.

## Related

- [[BrianCasel]] — creator and author
- [[ClaudeDesign]] — the tool evaluated
- [[ClaudeCode]] — the alternative for production design
- [[DesignSystem]] — Brian's preferred approach
- [[DesignDrift]] — the problem design systems solve
- [[VisualIdeation]] — the valid use case
