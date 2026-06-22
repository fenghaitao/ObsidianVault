---
title: "summary-4-agent-skills-marketing"
type: source
tags: [source, brian-casel, agent-skills, marketing, automation]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260406 - 4 Agent Skills I Use for Marketing.md]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel demonstrates four (actually five) agent skills he built to automate marketing: a radar scan for industry monitoring, a brand visuals generator, a newsletter writer, and a newsletter builder/assembler. The core thesis: most marketing work follows repeatable patterns that can be turned into skills and delegated to agents. The real human skill is observation — noticing the patterns you repeat every week and documenting them.

## Key Points

- **Radar Scan**: agent runs daily at 4 AM, reads RSS feeds of Twitter/X searches (via rss.app), filters for relevance using training data, writes a markdown report, notifies via Telegram. Tracks Anthropic team, OpenAI team, Cursor team, and industry influencers.
- **Brand Visuals**: agent skill that generates consistent branded illustrations using Claude for concept development and Google ImageGen API for actual image generation. Includes brand colors, visual world references, and a creative interviewing process.
- **Newsletter Writer**: multi-step skill that interviews Brian section by section (main message, subject line, YouTube section, podcast section, behind-the-build section), drafts content, and iterates based on feedback.
- **Newsletter Builder**: takes the written markdown content, assembles it into HTML email using section templates, pushes to Kit (ConvertKit) via API, and schedules delivery.
- Training data lives in SparkDrop (custom app) or can be markdown files within the skill folder.
- All skills follow the same structure: main SKILL.md with workflow phases, reference files for sources/config, and output instructions.
- Brian's agent "Veil" (marketing agent) runs on OpenClaw on a dedicated Mac mini.

## Related

- [[BrianCasel]] — creator and author
- [[AgentSkills]] — the pattern behind all four
- [[NightShiftModel]] — the delegation pattern
- [[OpenClaw]] — the platform running the agents
- [[SparkDrop]] — where training data lives
- [[BrainDown]] — the markdown report viewer
- [[BrandVisuals]] — the illustration skill
- [[ContentIdeation]] — related content process
