---
title: "summary-20260112 - Replacing my n8n workflow with a Claude Code Skill"
type: source
tags: [source, brian-casel, claude-skills, n8n, brand-visuals]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260112 - Replacing my n8n workflow with a Claude Code Skill.md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel spent a week building a complex N8N automation for brand illustration generation, scrapped it when output was garbage, then rebuilt it as a Claude Code skill in 30 minutes with better results. The lesson: breaking workflows into rigid nodes strips away AI's intelligence. Claude Code skills let the model reason about brand guidelines while following process.

## Key Points

- Spent a week building an N8N workflow for brand visuals — scrapped entirely.
- Rebuilt as a Claude Code skill in 30 minutes with higher quality output.
- N8N's rigid node logic stripped away the model's ability to think and reason about brand guidelines.
- Skill structure: SKILL.md (main process), references (visual world, style, prompts, colors), Python script (Gemini API integration), projects folder (per-illustration).
- Claude Opus 4.5 used for creative reasoning; Google Gemini ImageGen API for actual generation.
- Skill presents 3 concept options, Brian selects one, then generates.
- Claude Code itself became the application — not just a coding tool, but a workflow interface.

## Related

- [[BrianCasel]] — author
- [[ClaudeSkills]] — the skill system
- [[BrandVisuals]] — the skill built
- [[N8N]] — the tool that failed
- [[ClaudeCode]] — the platform
