---
title: "Hill Climbing (Evals)"
type: concept
tags: [evals, methodology, agent-quality, iterative-improvement]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Hill climbing in the context of evals is the iterative methodology of running an agent against a benchmark, getting a score, evaluating all failures, identifying root causes through trace analysis, pulling small levers that produce massive improvements, and repeating. It requires passing both the quantitative score check and the qualitative "vibe check."

## Key Information
- Core loop: get a score → evaluate failures → triage root causes → pull improvement levers → re-run → repeat
- Failure triage uses another agent to analyze traces (every single LLM call) and categorize failures (e.g., test didn't pass, retry tool was broken, rate limited)
- The limiting factor in parallelized eval runs is the slowest task
- Must pass both the vibe check (does the product feel good to use?) AND have a decent quantitative score
- Applies differently to different model families — the same prompt engineering techniques don't transfer between Anthropic, Gemini, and Codex model families
- Cline improved from ~43% to higher scores through hill climbing: adjusting CPU/memory in containers, raising timeouts, tweaking thinking behavior, and model-specific prompt engineering
- Hill climbing revealed that supporting additional model families (e.g., Gemini) could unlock entire user communities
- Requires discipline to stay in Zone 2 (nuanced improvements) and avoid Zone 3 (overfitting/benchmark maxing)

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[Three Zones of Improvement]] — the zones encountered during hill climbing
- [[Two Camps of Wrong on Evals]] — the misconceptions hill climbing avoids
- [[Model Harness Testing]] — what is being tested during hill climbing
- [[Benchmark Maxing]] — the danger zone hill climbing must avoid
- [[AgenticEvaluations]] — the type of evals used in agent hill climbing
- [[Eval Heuristics]] — heuristics that guide effective hill climbing
