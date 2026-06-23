---
title: "summary-20260514 - Make the PERFECT Videos with Claude Code (Full Workflow)"
type: source
tags: [source, original-material, video-generation, hyperframes, archon, claude-code]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260514 - Make the PERFECT Videos with Claude Code (Full Workflow).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] demonstrates an end-to-end **AI video-generation** pipeline: [[ClaudeCode]] scripts, voices, renders, and syncs short videos (animation + audio) using **[[HyperFrames]]** for HTML-based rendering, **ElevenLabs** (or free **Kokoro**) for voice, and **[[Archon]]** as the workflow engine. Open-source; "ask your coding agent to set it up" in ~10–15 minutes. Output isn't production-perfect yet (voice inflection, occasional awkward transitions) but is good enough for explainers, shorts, and team/community content — an ongoing experiment you can customize.

## Key Points

- **Tech stack**: [[ClaudeCode]] (orchestration via a skill) + **[[HyperFrames]]** (AI scene rendering; HTML-based; the more reliable successor to Remotion, which went viral as the first Claude-Code video skill) + **ElevenLabs** voice (or **Kokoro** for free) + **[[Archon]]** workflow engine + **SQLite** or **[[Neon]]** Postgres for run persistence.
- **Trigger**: clone the repo, open Claude Code, send a two-sentence prompt ("read the README, set everything up, here's my idea/URL"). Input can be a topic *or* a URL (e.g. turn a blog post into an explainer).
- **The workflow (one Claude Code skill wrapped in an Archon workflow for parallelism + durability)**:
  1. Create a **unique video ID** → isolated per-run folder; persist run state to the DB.
  2. Copy the chosen **template** into the run folder; set video metadata.
  3. **Research** the topic (with an **anti-fabrication gate** so it doesn't hallucinate).
  4. **Script** it — more than text: prompt-engineered with tags, breaks, and natural abbreviations to optimize text-to-speech.
  5. Single call to **ElevenLabs/Kokoro** → audio.
  6. **Sync animation timing** to the audio; build the **`index.html`** composition (HyperFrames is "literally just HTML").
  7. **Lint + layout-overflow inspection** frame-by-frame (no text/elements bursting containers).
  8. **Preview** in HyperFrames' built-in browser preview (scrub scenes, sound effects); iterate inline.
  9. Render the final **MP4** — with **granular adjustments** (fix one awkward inflection/transition) without re-rendering everything.
- **Templates**: 3 ship by default (control length, content, style); have Claude Code build a custom one via a guided Q&A (e.g. a 50s "concept explainer" with before/after diagrams). The agent auto-selects the right template per request.
- **Parallelism**: because Archon manages the workflow, you can generate many videos at once.
- **Use case nugget**: generate a 30–60s explainer of a new Claude Code feature (e.g. Agent View) for yourself instead of watching a long video or reading docs.

## Related

- [[HyperFrames]] — the HTML-based AI rendering engine (with ElevenLabs/Kokoro voice)
- [[Archon]] — the workflow engine orchestrating the pipeline
- [[ClaudeCode]] — runs the video-generation skill
- [[ClaudeSkills]] — the workflow is packaged as a skill
- [[Neon]] — Postgres run-state persistence (SQLite alternative)
- [[ColeMedin]] — author
