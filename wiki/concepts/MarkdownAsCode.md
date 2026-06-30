---
title: "MarkdownAsCode"
type: concept
tags: [skills, prompt-engineering, agent-design, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Markdown as Code is the paradigm of replacing traditional code implementations with markdown-based agent instructions (skills/commands). Instead of writing complex software logic, developers write natural language instructions that AI agents interpret and execute at runtime.

## Key Information

- David Gomes's central thesis: "markdown is basically the new code"
- Cursor replaced ~15,000 lines of code with ~200 lines of markdown for the work trees feature
- The /bestofn command is only ~40 lines of markdown, replacing ~4,000 lines of code
- Markdown instructions tell the model how to create work trees, run setup scripts, stay on the correct checkout, and compare results
- The approach leverages existing agent primitives (skills and sub-agents) rather than building custom infrastructure
- Trade-off: less code to maintain but relies on model compliance rather than mechanical enforcement
- Cross-platform instructions (Windows, Linux, macOS) are expressed as markdown conditionals

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Skills]] — the mechanism for loading markdown instructions
- [[AgentCommandsVsSkills]] — the server-controlled variant
- [[VibesBasedSafety]] — the trust-based trade-off
- [[Cursor]] — the product
