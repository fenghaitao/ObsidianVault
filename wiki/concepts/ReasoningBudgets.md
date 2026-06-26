---
title: "ReasoningBudgets"
type: concept
tags: [coding-agents, reasoning, model-parameters, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Reasoning budgets are adjustable thinking parameters in Claude Code that control how much compute the model spends on reasoning before acting. The tiers include "think," "think hard," and "ultra think," allowing the reasoning token budget to be used as a tunable parameter.

## Key Information
- Claude Code uses trigger phrases to adjust reasoning depth: think, think hard, think harder, and ultra think
- The reasoning token budget becomes another parameter the model can adjust (or be forced to adjust)
- Alternative approaches: making a tool call for hard planning, or letting the user specify the reasoning level
- Amp Code takes this further with fast, smart, and Oracle tiers, where Oracle may switch models without telling the user
- Zoneraich predicts adaptive budgets will be a key innovation: using a 20x faster but slightly stupider model for most tasks, with a tool call to a very good model for hard problems
- This could mean using GPT-5.1, Codex, or Opus as the "planner" while using faster models for execution
- Represents a "mix and match" approach to model selection within a single agent session

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — implements thinking tiers
- [[AmpCode]] — implements fast/smart/Oracle tiers
- [[ModelDistillation]] — enables the fast tier
