---
title: "summary-picking-the-right-model"
type: source
tags: [source, claude, model-selection, evals, cost-optimization, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/10 - Picking the right model.md]
last_updated: 2026-06-23
---

## Core Summary

Lucas from Anthropic's applied AI team presents a framework for picking the right model. Core thesis: a small, well-designed private eval teaches more than any public benchmark. The right model is not the cheapest per token but the cheapest per successful outcome. Key strategies: use adaptive thinking and effort parameters for fine-grained cost/quality control, prompt caching (90% hit rate target, 1/10th input cost), and context engineering (clean tool responses for 60-77% token reduction). Counterintuitive findings: more intelligent models can be faster and cheaper because they complete tasks in fewer turns.

## Key Points

- **Private evals over public benchmarks:** SWE-bench and BrowseComp are directional but don't match your specific workload. Build task-level evals with input, success criteria, and graders (LLM-as-judge + deterministic code checks).
- **Eval gotchas:** mistaking noise for signal (run multiple times), infra failures vs. model failures (separate them), silent saturation (ensure eval data matches production distribution).
- **Model selection pillars:** quality (task completion rate), latency (customer-facing), cost (per successful outcome, not per token).
- **Adaptive thinking + effort:** fine-grained control over the cost/accuracy frontier. Opus with low effort can be faster than Sonnet with high effort.
- **Prompt caching:** 1/10th input token cost; aim for 80-90% hit rate. Use append-only message strategy to avoid cache breaks.
- **Context engineering:** clean tool responses (markdown over JSON, deduplication, simplified timestamps). Example: 66% token reduction from formatting, 77% from deduplication, 9% accuracy improvement.
- **Counterintuitive:** Haiku with thinking was slower than Sonnet/Opus without thinking because smarter models complete tasks in fewer turns.

## Related

- [[AdvisorStrategy]] — the cost-efficient model strategy mentioned
- [[ContextWindow]] — the memory constraint context engineering manages
- [[PromptEngineering]] — related discipline
- [[ClaudeCode]] — the tool that uses these strategies
