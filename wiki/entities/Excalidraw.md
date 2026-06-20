---
title: "Excalidraw"
type: entity
tags: [tool, diagrams, visualization, obsidian-plugin, claude-skills]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260302 - Build BEAUTIFUL Diagrams with Claude Code (Full Workflow).md"
last_updated: 2026-06-20
---

## Definition

Excalidraw is a free, open-source diagramming tool with a hand-drawn aesthetic that stores diagrams as **JSON** (renderable at excalidraw.com or via the **Obsidian Excalidraw plugin**). [[ColeMedin]] uses it for all his diagrams and built a [[ClaudeSkills|Claude Code skill]] that generates and self-validates Excalidraw JSON — making it the canonical visual-output format in his workflow.

## Key Information

- **JSON-as-format**: because a diagram is just JSON, a coding agent can author it directly, and it can be version-controlled, edited, and re-rendered. The agent generates the JSON; you load it at **excalidraw.com** or with the **Obsidian Excalidraw plugin**.
- **The diagram skill** (`summary-beautiful-diagrams-claude-code`): a tool-agnostic skill that teaches the agent to "argue visually," assess diagram depth (build complex diagrams section-by-section to dodge the ~32k-token output limit), map shapes/text/layout, emit the JSON, then **self-validate** by rendering a PNG (Python script), viewing it, and iterating 2–4×.
- **On-brand customization**: a color-palette reference file (swap hex codes to your brand), element templates, and pattern guidance — all tunable.
- **Part of the [[SecondBrain]] template** as the "Excalidraw diagram generator" skill.

## Related

- [[ClaudeSkills]] — the skill that generates Excalidraw diagrams
- [[ClaudeCode]] — the agent that produces the JSON
- [[Obsidian]] — renders Excalidraw via its community plugin
- [[SecondBrain]] — ships the Excalidraw diagram skill
- [[ColeMedin]] — heavy user
- [[summary-beautiful-diagrams-claude-code]] — primary source
