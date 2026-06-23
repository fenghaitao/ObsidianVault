---
title: "HyperFrames"
type: entity
tags: [tool, video-generation, claude-code, rendering, html]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260514 - Make the PERFECT Videos with Claude Code (Full Workflow).md"
last_updated: 2026-06-20
---

## Definition

HyperFrames is an AI video-rendering tool that lets [[ClaudeCode]] (via a skill) generate animated video scenes defined as **plain HTML**, with a built-in browser **preview** editor. [[ColeMedin]] uses it as the rendering engine in his AI video-generation pipeline, calling it a more reliable step up from **Remotion** (which earlier went viral as the first tool to give Claude Code a video-generation skill).

## Key Information

- **HTML-as-composition**: scenes are an `index.html` the agent builds and can edit granularly — easy to mold, lint, and inspect for layout overflow frame-by-frame.
- **Built-in preview**: a localhost preview shows scenes, animations, and sound effects so you can review/adjust *before* rendering the final MP4 (and re-render only what changed).
- **Pipeline pairing** (per `summary-ai-generated-videos-claude-code`): HyperFrames (render) + **ElevenLabs** voice — or **Kokoro** for a free option — + [[Archon]] (workflow engine, parallel + durable) + [[ClaudeCode]] (orchestration). Workflow: research (anti-fabrication gate) → TTS-optimized script → single voice call → sync timing → build HTML → lint/overflow check → preview → render MP4.
- **Status**: AI-generated video is "not perfect yet" (voice inflection, occasional awkward transitions) but good for explainers/shorts; an ongoing, customizable experiment (free unless you opt into ElevenLabs).

## Related

- [[ClaudeCode]] — drives HyperFrames via a skill
- [[Archon]] — the workflow engine orchestrating the video pipeline
- [[ClaudeSkills]] — the video workflow is delivered as a skill
- [[ColeMedin]] — built the open-source video pipeline around it
- [[summary-20260514 - Make the PERFECT Videos with Claude Code (Full Workflow)]] — primary source
