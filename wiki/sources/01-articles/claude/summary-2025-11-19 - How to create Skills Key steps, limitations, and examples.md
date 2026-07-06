---
title: "summary-2025-11-19 - How to create Skills Key steps, limitations, and examples"
type: source
tags: [source, skills, how-to, claude-code]
sources: ["raw/01-articles/claude/2025-11-19 - How to create Skills Key steps, limitations, and examples.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's practical guide to authoring `SKILL.md` files: define a concrete problem before writing anything, then build the three components that matter — name, description (the only parts that influence triggering), and instructions — test with a matrix of normal/edge/out-of-scope cases, then refine based on real usage. Includes worked examples (docx editing, brand-guidelines, frontend-design) illustrating strong descriptions and progressive-disclosure structure.

## Key Points

- **Only name and description drive triggering** — Claude semantically matches request against description, not keyword matching; instructions only matter after a skill has already activated.
- **Strong descriptions** balance specific capabilities, clear triggers, relevant context, and explicit boundaries (what the skill is *not* for) — e.g., "Not for simple PDF viewing or basic conversions."
- **Build only for real, repeated tasks**: rule of thumb — have you done this at least 5 times, will you do it at least 10 more times?
- **Progressive disclosure via a "menu" structure**: SKILL.md describes available sub-workflows and references separate reference files by relative path; Claude reads only the file relevant to the current task, keeping unrelated content out of context (demonstrated in the docx skill's decision tree across `docx-js.md` and `ooxml.md`).
- **skill-creator** interactively builds skills via clarifying questions, description suggestions, and formatting help — recommended for a team's first few skills.
- **Testing**: a test matrix of normal usage, edge cases, and out-of-scope requests; test triggering and execution separately, since triggering failures need broader descriptions while execution failures need more specific instructions.
- **Governance**: shared document repository with skill specs recommended for all team sizes; org-wide skill management/sharing in Claude.ai was "coming soon" as of this article (delivered per the December 18, 2025 Agent Skills update).

## Related

- [[ClaudeCodeSkills]] — the mechanism this article is a how-to guide for
