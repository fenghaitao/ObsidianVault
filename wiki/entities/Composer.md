---
title: "Composer"
type: entity
tags: [model, cursor, llm, distilled, rl-training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Composer is Cursor's in-house trained and distilled model. It is extremely fast and is used as one of the model options within Cursor for coding tasks. Cursor trains Composer using RL (reinforcement learning) and plans to add work-tree-specific RL tasks for future versions.

## Key Information

- A distilled model that is extremely fast — Jared Zoneraich has been "almost switching completely to it"
- Demonstrates that fine-tuning/distillation can build defensibility based on proprietary data
- Cursor trains Composer using RL; for Composer 2, no RL tasks involved work tree prompts
- Future versions (Composer 3, 4, 5) will include RL tasks for operating in work tree environments
- Performs well on work tree evals compared to weaker models like Haiku
- David Gomes is working on adding work-tree-specific RL tasks to the training pipeline

## Related

- [[Cursor]] — the product
- [[DavidGomes]] — engineer working on Composer RL training
- [[ModelDistillation]] — technique behind Composer's speed
- [[ReinforcementLearningWithLLMs]] — training approach
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
