---
title: "summary-beautiful-diagrams-claude-code"
type: source
tags: [source, original-material, excalidraw, claude-skills, diagrams, visual-validation]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260302 - Build BEAUTIFUL Diagrams with Claude Code (Full Workflow).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] packages his diagram-creation process into an open-source **[[Excalidraw]] diagram [[ClaudeSkills|skill]]** that teaches a coding agent to "argue visually" — generating the Excalidraw JSON for clean, educational diagrams and then **self-validating** by rendering the diagram to PNG, viewing the image, and iterating on imperfections. Coding agents are weak at visual tasks without a framework; this skill supplies the prompting, design patterns, color palette, and validation loop to turn [[ClaudeCode]] (or any agent) into a competent diagrammer — producing a strong starting point that saves hours weekly.

## Key Points

- **Delivery**: clone the GitHub repo into `.claude/skills/excalidraw-diagram/` (or any agent's skills dir). Tool-agnostic. Render the output JSON at **excalidraw.com** (free) or via the **Obsidian Excalidraw plugin**. Easiest setup: ask the agent to read the repo's README and set itself up (a Python script for rendering is the only real dependency).
- **"Argue visually" philosophy**: the diagram's *structure and labels* should convey the concept even with explanatory text stripped out — not just "boxes and boxes and boxes" (the default, samey output agents produce unguided). Two self-questions baked into the skill: *does the visual structure mirror the concept's behavior?* and *could someone learn something concrete from this?*
- **Workflow**: idea → **assess depth** (simple = one shot; complex = build **section by section** to avoid Claude Code's ~32,000-token output limit) → **map the pattern** (shapes, text, layout) → build the JSON → **validation loop**: render PNG → view image → find imperfections (janky/short arrows, colors, info density, hierarchy) → edit the JSON in place → repeat (usually 2–4 iterations).
- **Never perfect first try** — sensibly so: the LLM must decide every color, shape, position, and layout (huge number of micro-decisions). The value is a strong *starting point* for human-directed iteration (Cole's meta-diagram took 2–3 passes).
- **Customization via reference files** ([[ProgressiveDisclosure]]): a **color palette** file (swap to your brand's hex codes), element/template patterns, "multi-zoom architecture" for variety, and "evidence artifact" elements for educational rigor — all tunable, all working out-of-the-box.
- **Self-validation theme**: this is the same "let the agent check its own work via images" idea behind browser-based [[ValidationGates]] — applied to visual output. Giving agents a way to *see* their work is what makes them usable for visual tasks.
- One of the skills shipped in Cole's [[SecondBrain]] template (the "Excalidraw diagram generator").

## Related

- [[Excalidraw]] — the diagramming tool/format the skill targets
- [[ClaudeSkills]] — the packaging format; visual self-validation example
- [[ClaudeCode]] — the agent that runs it
- [[Obsidian]] — render target via the Excalidraw plugin
- [[ProgressiveDisclosure]] — color palette / templates as reference files
- [[SecondBrain]] — the template that ships this skill
- [[ValidationGates]] — the same self-validation principle, for visuals
