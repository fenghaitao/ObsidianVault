---
title: "summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic"
type: source
tags: [source, transcript, agent-optimization, gepa, evals, feedback-loops, pydantic-ai, logfire, managed-variables, prompt-optimization, genetic-algorithm, structured-outputs, pydantic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Core Summary
Samuel Colvin, creator of Pydantic, presents a live workshop on agent optimization using GEPA (Genetic Evolutionary Pareto Algorithm), Pydantic AI evals, and Pydantic Logfire managed variables. He demonstrates a complete optimization pipeline: running structured-output agents against a golden dataset of UK MPs' political relations, comparing prompt performance via Logfire evals, using GEPA to iteratively improve the system prompt from 85% to 96.7% accuracy, and then deploying the optimized prompt via managed variables without redeployment. The talk also covers AI observability, the Pydantic AI Gateway, and the vision of self-driving managed variables.

## Key Points
- **GEPA (Genetic Evolutionary Pareto Algorithm)**: An optimization library by Lakshya (Berkeley PhD student) that uses genetic algorithms to optimize strings (prompts or JSON). It selects candidates from the Pareto frontier of best performers, mixes them, and proposes new candidates via a proposer agent. Named from "genetic" + "Pareto."
- **Managed Variables**: Logfire's evolution beyond prompt management — any Pydantic model can be managed inside Logfire, enabling A/B testing via OpenFeature standard, and updating agent behavior (prompts, models, temperature) without redeployment.
- **Eval pipeline**: Pydantic AI's eval system supports custom evaluators (preferred over LLM-as-judge for deterministic cases), golden datasets, and comparison views in Logfire showing per-metric performance differences.
- **Optimization results**: Starting from a simple one-liner prompt (85% accuracy) → expert human-written prompt (92%) → GEPA-optimized prompt (96.7%), all using the same GPT-4.1 model.
- **Structured outputs**: The agent uses Pydantic models to extract structured political relations from Wikipedia HTML, demonstrating structured output as a general pattern beyond text extraction.
- **AI observability as a feature, not a category**: Colvin argues AI observability will be absorbed by either observability or AI platforms. Logfire provides OpenTelemetry-based logs, metrics, traces plus evals and managed variables.
- **Pydantic AI Gateway**: A model gateway providing one API key for multiple model providers (Anthropic, OpenAI, Grok, Gemini), with caching, fallback, and observability.
- **Shopify case study**: Using GEPA, Shopify switched from GPT-5 analyzing entire websites to a Qwen-based agent with optimized prompts, reducing costs from $5M/year to $73K/year while improving performance.
- **Deterministic evals > LLM-as-judge**: Custom evaluators comparing against golden data are far better than LLM-as-judge, which Colvin describes as "lunatics running the asylum."
- **Self-driving managed variables**: The vision is to wire GEPA optimization directly into Logfire managed variables so the platform autonomously hill-climbs toward better agent performance.
- **Eval challenges**: Golden datasets are hard to create; models overfit to small training sets (e.g., excluding uncles/aunts because they weren't in training cases); optimization matters more for private data where models lack pre-training knowledge.
- **User feedback as implicit evals**: The best eval signal is what users do next — if they say "no, I mean X," that's strong negative feedback; if they say "thanks" or leave, it's positive.
- **Prompt optimization vs fine-tuning**: For most use cases, improving the harness and waiting for the next model beats fine-tuning. Fine-tuning applies where massive private data and high volume justify the cost.
- **Model transferability**: Optimization is model-specific — changing models requires re-running optimization. This is why most companies don't do it; they eyeball prompts and ship.
- **Variance in evals**: Running evals many times (some hedge funds spend $20K/night) reduces variance. The number of runs per case can be configured.

## Related
- [[Samuel Colvin]] — speaker, creator of Pydantic
- [[Pydantic]] — the validation library and company
- [[Pydantic AI]] — the agent framework
- [[Pydantic Logfire]] — observability platform
- [[GEPA]] — Genetic Evolutionary Pareto Algorithm
- [[Agent Optimization]] — the core concept demonstrated
- [[Managed Variables]] — Logfire feature for runtime agent configuration
- [[Golden Dataset]] — reference data for eval comparison
- [[Pareto Frontier]] — optimization selection strategy
- [[AI Observability]] — observability for AI systems
- [[Agentic Optimization]] — autonomous agent improvement
- [[PromptOptimization]] — iterative prompt improvement
- [[LLM-as-Judge]] — evaluation technique critiqued in the talk
- [[Structured Outputs]] — pattern used for MP relation extraction
- [[OnlineEvals]] — production evaluation
- [[OfflineEvals]] — pre-production evaluation
- [[EvalEngineering]] — crafting effective evaluations
- [[EvalPlatforms]] — platforms for running evals
- [[Evaluator-Optimizer Pattern]] — pattern for agent improvement
- [[EvalFlywheel]] — continuous improvement loop
- [[OverfittingAsExpertise]] — domain specialization as a feature
- [[ModelTransferability]] — optimization is model-specific
- [[Self-Improving Agents]] — agents that improve over time
- [[Feedback Loops as AI Speed Limit]] — feedback as bottleneck
- [[Model Rot]] — models degrading over time
- [[Jeba]] — related prompt optimization technique
- [[GEA]] — DSPy's evolutionary optimizer (related to GEPA)
- [[Shopify]] — case study for cost reduction via optimization
- [[DSPy]] — agent framework with optimization
- [[OpenAI]] — model provider used
- [[Anthropic]] — model provider mentioned
- [[aiDotEngineer]] — event host
