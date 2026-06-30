---
title: "DavidGomes"
type: entity
tags: [person, cursor, engineer, skills, worktrees]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

David Gomes is an engineer at Cursor who led the effort to replace Cursor's ~15,000-line Git work trees and "best of N" feature implementation with a ~200-line markdown skill/command.

## Key Information

- Presented at aiDotEngineer conference on April 30, 2026
- Led the refactor that replaced a complex code-based feature with markdown-based agent instructions
- The PR deleting the old implementation removed approximately 15,000 lines of code
- Works on evals for the work tree feature using Braintrust and the headless Cursor CLI
- Self-described as "fairly early" in his evals writing journey
- Uses two scorers for work tree evals: one checking work was done in the work tree, another checking no work was done in the primary checkout
- Found that weaker models like Haiku frequently deviate from work tree instructions, while Composer and Grok perform better

## Related

- [[Cursor]] — the product he works on
- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Composer]] — Cursor's in-house model he's training via RL
- [[Braintrust]] — eval platform he uses
- [[GitWorktrees]] — the feature he re-implemented as a skill
- [[BestOfN]] — the feature he re-implemented as a skill
