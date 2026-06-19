---
title: "summary-second-brain-with-claude-code-obsidian-skills"
type: source
tags: [source, transcript, second-brain, obsidian, claude-code, skills, knowledge-management]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] introduces his **[[SecondBrain]]** system — using [[ClaudeCode]] + [[Obsidian]] + [[ClaudeSkills]] as a personal knowledge / ideation / research engine, *not for coding*. The thesis: a "coding agent" minus the code-intelligence tool is just a powerful general-purpose CLI agent operating against a markdown filesystem. Pair with Obsidian (which *is* a markdown filesystem with a graph view), and you have a perfect harness for the ideation/organization/research use case. This source is **directly relevant to the design of the wiki this knowledge base is built in.**

## Key Points

- **Why Claude Code for non-coding tasks**: a coding agent's capabilities reduce to five categories — file operations, file search, terminal execution, web search, code intelligence. Strip code intelligence and you have a general-purpose CLI agent. Cole's "huge mistake" was thinking Claude Code was just for coding.
- **Why pair with [[Obsidian]]**:
  - Obsidian is markdown-on-the-filesystem. Claude Code's strongest substrate is markdown-on-the-filesystem.
  - Obsidian provides graph view, backlinks, search, plugins for human-side reading and curation.
  - **Obsidian beats Notion for this** because Notion requires an MCP server abstraction — Claude Code can't directly own a Notion workspace the way it can own a folder of markdown.
  - Cole calls Obsidian his "canvas" — Claude Code generates content there, he applies the human touch.
- **The Three-Use-Case Frame** for a Second Brain:
  - **Research** — web search + terminal + file-write
  - **Ideation** — file-search through accumulated notes + LLM reasoning
  - **Organization** — file ops + search across the vault
  All three are core Claude Code capabilities. Coding is the only capability that *isn't* used for non-coding work.
- **[[ClaudeSkills]] is the third leg** — and the part that makes the system scale. Each skill is a folder with a `SKILL.md` describing a capability the agent can invoke. **Progressive disclosure**: only the short description loads upfront; the full skill instructions and supporting files load only when the skill is invoked.
- **Three layers of progressive disclosure** in a skill:
  1. The short description (always loaded — used for "should I invoke this skill?" decision).
  2. The full `SKILL.md` (loaded when the skill is invoked).
  3. Supplementary files inside the skill folder — Python scripts, reference markdown — loaded only when needed mid-skill.
- **Why Skills > MCP for personal capabilities**: MCP servers expose all their tools' descriptions upfront, blowing up the context window when you have many integrations. Skills are lazy — only relevant ones populate the context per session.
- **Skills Cole's system uses** (template repo):
  - **Brand & voice generator** — produces the project's brand spec (tone, palette, typography) for downstream skills like the PowerPoint generator to consume.
  - **PowerPoint generator** — Python-script-based slide generation, on-brand. Cole says this beats Gamma and Anthropic's PPTX skill because of the brand-aware scripts in the cookbook folder.
  - **MCP-to-Skill** — wraps an MCP server's tools as a skill, sidestepping the MCP context-bloat issue. Cole uses this for [[Zapier]] (which exposes Gmail, Asana, Calendar, Slack with ~20 tools).
  - **Excalidraw / Remotion / YouTube script / X post / LinkedIn post** — content-generation skills.
  - **Skill creator** — Anthropic-published meta-skill that creates new skills.
- **Critical principle**: the second brain is for **ideation, organization, research**. Not generating "AI slop" to post automatically. The human touch is preserved at the publication boundary.

## Related

- [[SecondBrain]] — central concept
- [[ClaudeSkills]] — the scaling primitive
- [[ClaudeCode]] — the agent substrate
- [[Obsidian]] — the markdown canvas
- [[KarpathyLLMWiki]] — the broader pattern this implements (forward-reference; full page lands in batch C)
- [[ColeMedin]] — author
- [[ProgressiveDisclosure]] — the loading strategy that makes Skills scale
- [[Zapier]] — example MCP server Cole wraps as a skill
