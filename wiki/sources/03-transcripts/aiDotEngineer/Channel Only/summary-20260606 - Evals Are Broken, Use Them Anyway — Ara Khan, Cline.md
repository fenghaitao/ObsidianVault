---
title: "Evals Are Broken, Use Them Anyway — Ara Khan, Cline"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"
author: "Ara Khan"
company: "Cline"
date: 2026-06-06
tags: [evals, benchmarks, agent-quality, hill-climbing, coding-agents, model-evaluation, prompt-engineering]
---

# Evals Are Broken, Use Them Anyway — Ara Khan, Cline

## Core Thesis

Evals are broken but you should use them anyway. Most people are wrong about evals — they fall into one of two camps: treating objective benchmark metrics as definitive truth, or dismissing quantitative evaluation entirely in favor of subjective "vibes." The correct approach lies in the middle: evals are neither the end-all-be-all nor completely useless. When used with the right heuristics and a disciplined hill-climbing process, evals are essential tools for improving AI agents.

## Key Points

### Two Camps of Wrong on Evals

Ara Khan identifies two fundamental ways people misunderstand evals:

1. **The Objective Metrics Camp**: People who treat benchmark dashboards as definitive truth — interpreting similar benchmark scores across different models as evidence that the models are effectively the same, when real-world experience says otherwise. This camp is prone to believing that benchmark numbers are a hoax when they don't align with reality.

2. **The Taste/Vibes Camp**: People who go too far in the opposite direction, dismissing all quantitative evaluation and relying purely on subjective feel. They anthropomorphize models ("I like talking to her") and reject systematic measurement entirely.

The truth is that evals are useful tools when applied correctly — neither gospel nor garbage.

### Three Heuristics for Interpreting Evals

1. **Don't believe model provider eval numbers**: Model companies publish benchmark scores that are approximations at best. AI researchers and engineers routinely dismiss these numbers as not to be taken that seriously. Real-world trying and preferences matter more.

2. **Stay current, but don't be the earliest adopter**: The frontier model changes every couple of months. Let new models settle for a couple of weeks — if they still stand the test of time after the initial hype, then consider switching. Only people who work on this for a living need to always be on the cutting edge.

3. **Look for very new and very precise evals**: Many standardized evals have become old and no longer measure frontier capabilities. OpenAI itself stated that SWE-bench no longer measures frontier coding capabilities — it contains problems like solving the Fibonacci sequence that don't apply to real-world software engineering.

### Cline's Journey with Evals

- Initially, Cline (like the Codex team and others) ignored evals entirely, considering them unnecessary and a waste of time
- Last year, the team decided they needed measurement and committed to building actual evals from scratch
- They gathered massive datasets of real user coding problems (opt-in, paid participants), parsed and cleaned them into evaluation tasks
- The hardest challenge: single-turn evals (binary answers) are easy, but agentic evals involve multi-step workflows (reading files, searching docs, installing environments, running scripts, executing tests) with near-infinite search spaces
- They adopted **[[TerminalBench]]** (89 real-world programming problems from [[Stanford]]) covering race conditions, database issues, infrastructure problems — tasks that take 30-40 minutes to run
- They used **[[Harbor]]** (from the Loda Institute) for standardized configuration and infrastructure to run all 89 tasks in parallel, with the slowest task as the limiting factor
- They used **[[Modal]]** for compute infrastructure to handle the parallel execution

### The Three Things Being Tested

When running agent evals, three components are being evaluated simultaneously:

1. **The model itself**: A strong model can compensate for a weak harness
2. **The coding harness**: How well the agent framework actually leverages the model's capabilities (e.g., why Anthropic models seem to work better with Claude Code than with other coding agents)
3. **The problem quality**: If you're testing on trivial problems, a 100% score means nothing

### Three Zones of Improvement

When improving an agent based on eval scores (starting from an initial baseline like 43%):

1. **Zone 1 — Obvious Flaws**: Straightforward bugs that crash the harness, rate limiting issues, container configuration problems (CPU, memory, timeouts). These are easy to fix.

2. **Zone 2 — Nuanced Improvements** (most critical): Model-specific prompt engineering techniques — what works for Anthropic model families may not work for Gemini or Codex model families. This is the essence of working with agents: figuring out why a model that everyone says is great isn't working for you, and tweaking prompts (making them larger or smaller), adjusting thinking behavior, etc.

3. **Zone 3 — Danger Zone (Overfitting)**: Straight-up cheating to get the highest benchmark score just to tweet about it. This is [[Benchmark Maxing]] — optimizing for the eval rather than real-world performance.

### Hill Climbing

The core methodology: get a score on a benchmark, evaluate all failures, triage them by root cause (e.g., test didn't pass, retry tool broken), identify the small levers that produce massive improvements, and iterate. You must pass both the vibe check (does the product actually feel good to use?) AND have a decent quantitative score. When new models come out, give them fair judgment — supporting a broader range of model families (e.g., Gemini) can unlock entire user communities.

### The Engineering + Philosophy Problem

Building evals is both an engineering problem and a philosophy problem. The philosophy challenge: you have a problem and cannot exactly approximate the search space of where things could go wrong. Even coding problems have an infinite search space. The goal is to build evals that are an approximate representation of the actual thing you're dealing with.

## Entities

- [[AraKhan]] — Speaker, works at Cline
- [[Cline]] — Open-source coding agent company
- [[TerminalBench]] — 89-problem benchmark from Stanford for real-world programming tasks
- [[Harbor]] — Eval infrastructure from Loda Institute for parallel execution
- [[HarborEval]] — De facto evaluation harness for agent builders
- [[Stanford]] — University that created TerminalBench
- [[Modal]] — Compute infrastructure used by Cline for eval execution
- [[Codex]] — Coding agent; team shared Cline's early stance of ignoring evals
- [[Anthropic]] — Model provider whose models Cline tested
- [[Gemini]] — Model family Cline worked to support through hill climbing
- [[ClaudeCode]] — Coding agent cited as example of harness leveraging model well

## Concepts

- [[Two Camps of Wrong on Evals]] — Objective metrics camp vs. taste/vibes camp
- [[Eval Heuristics]] — Three heuristics for interpreting and using evals
- [[Hill Climbing (Evals)]] — Iterative score improvement methodology
- [[Three Zones of Improvement]] — Obvious flaws, nuanced improvements, overfitting
- [[Model Harness Testing]] — Testing the model, harness, and problem quality
- [[Benchmark Maxing]] — Optimizing for benchmarks at the expense of real-world performance
- [[AgenticEvaluations]] — Multi-step agent evaluations vs. single-turn model evals
- [[BenchmarkSaturation]] — Why old standardized evals lose their signal
- [[Overfitting]] — Zone 3 danger in eval-driven development
- [[AgentHarness]] — The coding harness as a component being tested

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — companion talk on eval practice phases
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — agentic evaluations at scale
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — benchmarking agent methodology
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — eval platform maturity
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — harness engineering deep dive
