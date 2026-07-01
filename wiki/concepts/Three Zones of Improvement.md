---
title: "Three Zones of Improvement"
type: concept
tags: [evals, agent-quality, methodology, improvement, overfitting]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Three Zones of Improvement is a framework for understanding the types of gains achievable when improving an AI agent based on evaluation scores. It divides improvements into three zones: obvious flaws, nuanced improvements, and the danger zone of overfitting.

## Key Information

### Zone 1: Obvious Flaws
- Straightforward bugs that crash the harness
- Rate limiting issues
- Container configuration problems (CPU, memory, timeouts)
- Easy to identify and fix
- Necessary but insufficient for meaningful improvement

### Zone 2: Nuanced Improvements (Most Critical)
- Model-specific prompt engineering techniques that differ across model families
- What works for Anthropic model families may not work for Gemini or Codex model families
- The essence of working with agents and hill climbing
- Figuring out why a model that everyone says is great isn't working for you
- Specific techniques: tweaking prompt size (larger or smaller), adjusting thinking behavior (sometimes asking a model to think more causes it to loop endlessly for thousands of tokens)
- This is where real, sustainable gains are made

### Zone 3: Danger Zone (Overfitting)
- Straight-up cheating to get the highest benchmark score
- Optimizing for the eval rather than real-world performance
- [[Benchmark Maxing]] — getting a great score just to tweet about it
- Must be actively avoided
- Requires discipline to stay in Zone 2

### Practical Application
- Cline improved from ~43% through Zones 1 and 2: fixing container CPU/memory, raising timeouts, improving thinking behavior, and model-specific prompt engineering
- The process requires [[Hill Climbing (Evals)]] — iterating through all three zones while staying disciplined

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[Hill Climbing (Evals)]] — the methodology that operates across these zones
- [[Benchmark Maxing]] — Zone 3 danger
- [[Overfitting]] — the underlying phenomenon in Zone 3
- [[Model Harness Testing]] — what is being improved across these zones
- [[Two Camps of Wrong on Evals]] — the misconceptions this framework helps avoid
