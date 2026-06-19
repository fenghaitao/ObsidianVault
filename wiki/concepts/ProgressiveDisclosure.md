---
title: "ProgressiveDisclosure"
type: concept
tags: [concept, context-management, claude-skills, mcp, lazy-loading]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
last_updated: 2026-06-19
---

## Definition

Progressive Disclosure is the loading strategy used by [[ClaudeSkills]]: only short capability descriptions load into the context window upfront; the full instructions for any specific capability load **only when that capability is actually invoked**. It's the architectural primitive that lets a [[SecondBrain]] scale to dozens of skills without overwhelming the [[ContextRot|context window]].

## Key Information

### The three layers (in [[ClaudeSkills]])

| Layer | What loads | When |
|---|---|---|
| **Layer 1: Skill descriptions** | Short ~1-line description per skill | Always, at session start |
| **Layer 2: `SKILL.md`** | Full skill instructions | When the agent decides to invoke this skill |
| **Layer 3: Skill resources** | Python scripts, reference markdown, examples in the skill folder | When the skill needs them mid-execution |

Each layer is a strict subset of the next — the agent only ever loads what it needs for the current task.

### Concrete example: PowerPoint generator skill

From `summary-second-brain-with-claude-code-obsidian-skills`:

- **Always loaded (Layer 1)**: `"Generate or edit on-brand PowerPoint presentations. Use when the user asks to create or edit slides."` (1 line, ~30 tokens)
- **Loaded when invoked (Layer 2)**: full `SKILL.md` with workflow, conventions, output format. (~800 tokens)
- **Loaded mid-execution (Layer 3)**: `cookbook/create_presentation.py` or `cookbook/edit_presentation.py` depending on whether the user wants to create new or edit existing. (~2000 tokens, only one loads)

A 50-skill system would have:
- Always loaded: 50 lines, ~1500 tokens (manageable)
- Loaded on demand: only the active skill's full content

Without progressive disclosure (e.g. naïvely loading all 50 `SKILL.md` files upfront): ~40,000 tokens of always-loaded context. Unworkable.

### Why this matters more than raw model context size

Even with 1M-token context windows ([[Anthropic]] Claude, Gemini Pro), [[ContextRot]] sets in well before you fill the window. Progressive disclosure isn't about fitting more — it's about *attending* to less. The model reasons better with 5K relevant tokens than with 50K mostly-irrelevant tokens.

### Where else this pattern appears

- **`@docs` references in [[Cursor]]/[[Windsurf]]** — only loads framework docs when you reference them.
- **[[ModularRulesArchitecture]]** — rules-via-reference is a form of progressive disclosure.
- **[[RetrievalAugmentedGeneration]]** — query-time retrieval is the most general case of "load only what's needed for this question."
- **[[ToolUse]] tool descriptions** — load tool descriptions, not tool implementations.

The principle is universal in well-designed agent systems: **declarative summary upfront, full content on demand**.

### Why MCP fights this and Skills supports it

[[ModelContextProtocol]] servers expose all their tools' descriptions when the server is mounted — even if you only use one of them in a session. A 20-tool MCP server is a 20-tool always-loaded cost.

Skills invert this: the skill's existence is signaled by a 1-line description; the actual capability content is dormant until invoked. This is *why* Cole prefers Skills over MCP for personal capabilities at scale, and *why* he wraps MCP servers as Skills (the MCP-to-Skill skill from his template) when he must use MCP.

## Related

- [[ClaudeSkills]] — primary implementation
- [[ContextRot]] — failure mode this avoids
- [[SecondBrain]] — pattern that depends on progressive disclosure to scale
- [[ContextEngineering]] — broader discipline
- [[ModelContextProtocol]] — counterpoint (always-loaded tool descriptions)
- [[ColeMedin]] — articulator in this corpus
- [[Anthropic]] — Skills inventor
- [[summary-second-brain-with-claude-code-obsidian-skills]] — primary source
