---
title: "Jeba"
type: concept
tags: [prompt-engineering, optimization, llm, technique]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition

Jeba is a sample-efficient technique for improving complex LLM systems through iterative prompt optimization, without requiring reinforcement learning or fine-tuning. It seeds a system with prompts, executes them across tasks, scores results, selects the best via PA selection, and uses an LLM to reflect and generate improved prompts.

## Key Information

- Based on a paper from early 2025
- Key motivation: sample-efficient improvement of complex LLM systems without RL or fine-tuning
- Process: seed prompts → execute on tasks → score → PA selection (select best) → LLM reflection on what worked/didn't → generate new prompts → repeat
- Key innovations: reflective prompt mutation technique, PA selection for broader exploration of prompt space, tuning text rather than weights
- Used by The Browser Company for hill-climbing and refining AI product prompts
- Particularly valuable for small companies that can't afford expensive RL/fine-tuning pipelines

## Related

- [[summary-20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (GEPA as related technique)
- [[TheBrowserCompany]] — company using this technique
- [[ModelBehavior]] — broader discipline this technique supports
- [[DiaBrowser]] — product optimized with this technique
- [[GEPA]] — related genetic evolutionary algorithm
- [[PromptOptimization]] — broader category
