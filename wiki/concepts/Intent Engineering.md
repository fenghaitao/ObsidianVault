---
title: "Intent Engineering"
type: concept
category: paradigm
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Intent engineering is the emerging paradigm (2025+) where AI agents self-optimize based on user intent rather than following explicit instructions. Unlike prompt engineering (manually crafting instructions) or context engineering (providing structured data and tools), intent engineering leverages models' growing capability to understand goals and adapt behavior accordingly.

## Key Information

- **Evolutionary progression**: Follows prompt engineering (~2023) and context engineering as the third era of AI steering
- **Enabling factors**: Cheap tokens enabling high-velocity code generation; models becoming remarkably capable at pattern recognition and reasoning (e.g., solving ARC-I2 puzzles)
- **Key challenge for evaluation**: When every user's experience differs because the agent adapts to individual intent, how do you build tests that meaningfully assess quality?
- **Self-optimization**: The machine tunes itself based on intent — similar to auto-optimization research where a goal and reward signal drive self-correction
- **Relationship to agent harnesses**: Exemplified by [[OpenClaw]], where the harness changes itself — creating skills, adapting to the user — rather than executing fixed workflows
- **Proposed by**: [[VincentKoc]] as the next stage beyond prompt and context engineering

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator of the framing
- [[Malleable Evals]] — evaluation methodology for intent-engineered systems
- [[Intent-Based Outcomes]] — evaluation approach derived from intent engineering
- [[OpenClaw]] — agent harness exemplifying intent-driven adaptation
- [[ContextEngineering]] — preceding paradigm
- [[PromptEngineering]] — earlier paradigm
