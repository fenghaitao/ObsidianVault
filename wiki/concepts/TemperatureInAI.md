---
title: "TemperatureInAI"
type: concept
tags: [ai-engineering, llm, determinism, creativity]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Temperature is a setting in large language models (0 to 1) that controls the randomness/creativity of token selection during generation. Lower values produce deterministic outputs; higher values produce more varied, creative outputs.

## Key Information
- Temperature controls entropy/randomness in next-token prediction
- Range: 0 to 1; avoid using exactly 0 or exactly 1 (weird behavior at extremes)
- At low temperature (e.g., 0.001): same task twice produces identical output character-for-character
- At high temperature (e.g., 0.9): same task produces wildly different approaches to the same problem
- Use case matters: deterministic tasks need low temperature; creative tasks benefit from higher temperature
- Understanding temperature is especially important when building AI agents
- Tools for experimentation: Docker Model Runner, Ollama, LM Studio
- Aman Khan noted that lowering temperature can reduce variance in LLM-as-judge outputs, though it doesn't eliminate it entirely

## Related
- [[summary-20251219 - Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian)]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[LLM-as-Judge]] — temperature affects judge reliability
- [[SystemPromptFeedbackLoop]] — another control lever for AI output quality
