---
title: "Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"
author: "Vincent Koc"
company: "Comet"
date: 2026-05-12
tags: [evals, agents, adaptive-systems, benchmarks, intent-engineering, openclaw]
---

# Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw

## Core Thesis

AI evaluation must undergo a fundamental mindset shift from static benchmarks to adaptive, intent-based evaluation. As AI agents become self-adapting, self-optimizing systems (exemplified by harnesses like OpenClaw that change themselves), treating evals as fixed datasets is increasingly disconnected from reality. The path forward is to treat evals not as a point-in-time measurement but as a living, self-optimizing agent — defining the desired end state and letting machines self-correct toward it. This shift mirrors the evolution from prompt engineering through context engineering to intent engineering, where machines self-optimize based on intent rather than explicit instruction.

## Key Points

### The Gap: Software Engineering vs. AI Evaluation

Traditional software engineering has evolved through unit tests, manual regression suites, CI/CD pipelines, and crucially, chaos engineering and observability — deliberately breaking systems to understand their limits. AI evaluation has not made the same progression. The field remains stuck at static benchmarks and handcrafted offline evaluations, missing the chaos engineering equivalent that would reveal where systems actually break under real-world conditions.

### Why Static Benchmarks Fail Adaptive Systems

AI applications are not static, but they are evaluated as if they were. Agent harnesses like OpenClaw now change themselves — creating skills, adapting behavior — at a velocity that static benchmarks cannot match. When software ships at lightning speed, the question becomes: how do benchmarks keep up? The current approach of building enormous datasets to approximate agent behavior only works until something goes wrong — and something always goes wrong.

### The Three Eras of AI Steering

1. **Prompt Engineering** (peaked ~2023): "Doom scrolling" wordsmith instructions — bashing random words into an AI and hoping for improvement. Analogous to discovering painkillers while searching for a liver disease cure. Still practiced despite being largely superseded.

2. **Context Engineering**: Made evals more relevant by introducing steps — RAG, tool calling, data retrieval. Allowed breaking large agentic systems into testable components (e.g., testing individual MCP tools). Made evaluation more steerable but still incomplete.

3. **Intent Engineering** (emerging 2025): Machines self-optimize based on intent. With cheap tokens enabling high-velocity code generation and models becoming remarkably capable (solving ARC-I2 puzzles through pattern recognition), agents can now understand and adapt to user intent rather than follow explicit instructions. This is where evaluation becomes most complex — how do you test when every user's experience differs?

### The Four Pillars of Malleable Evaluation

1. **Intent-Based Outcomes**: Instead of testing "1 + 1 = 2", define the desired end state and let agents work toward it. Evaluation becomes defining the goal, not the path.

2. **Self-Curating Suites from Traces**: Agents automatically generate test suites from production traces. When customer demographics shift and query patterns change, the eval suite adapts rather than remaining frozen.

3. **Online Always-On Evaluation**: Continuous evaluation as a service — agents performing evals continuously rather than at discrete points, feeding back into improvement loops.

4. **Telemetry in the Loop**: When the agent harness is aware of its own telemetry — errors, costs, conditions — it can self-correct. The agent heals itself by consuming its own observability data.

### Eval Calcification

Vincent introduces the concept of "eval calcification" — evaluations becoming progressively harder and more brittle over time unless approached with intelligence. Without adaptive approaches, the gap between what agents actually do and what benchmarks measure will only widen.

### The 80/20 Rule for Adaptive Systems

80% of agent behavior is stable and can be covered by static, intent-defined evaluations. But the 20% that constantly changes — weird user questions, novel usage patterns — is what breaks businesses. The solution is agents that monitor and adapt to that 20%, feeding changes back into the eval system.

### The Self-Optimizing Vision

Drawing on Karpathy-style auto-optimization research (set a goal, set a target, let the system tune itself), Vincent proposes that evals should become the end state rather than the dataset. Users define what success looks like, and the machine self-corrects toward that outcome. Evals evolve from static artifacts into living, growing agents.

## Entities

- [[VincentKoc]] — Speaker, eval researcher at Comet, core contributor to OpenClaw
- [[Comet]] — ML/AI evaluation platform where Vincent works
- [[OpenClaw]] — Self-adapting agent harness cited as example of malleable software
- [[AndrejKarpathy]] — Referenced for auto-optimization research methodology

## Concepts

- [[Malleable Evals]] — Evaluations that adapt alongside adaptive AI systems
- [[Intent Engineering]] — Machines self-optimizing based on intent rather than explicit instruction
- [[Eval Calcification]] — The progressive hardening of evaluations without adaptive approaches
- [[Chaos Engineering For AI]] — Applying chaos engineering principles to AI evaluation
- [[Adaptive Testing For LLMs]] — Tests that change with the application rather than remaining static
- [[Telemetry In The Loop]] — Feeding agent telemetry back into the agent for self-correction
- [[IntentBased Outcomes]] — Evaluating against desired end state rather than exact outputs
- [[SelfCurating Test Suites]] — Agent-generated eval suites that evolve from production traces
- [[Static Benchmarks]] — Traditional fixed-dataset evaluation approach being critiqued

## Related

- [[OnlineEvals]] — existing concept for scoring against live production traffic
- [[EvalFlywheel]] — the loop connecting production observability with offline experimentation
- [[EvalMaturityStages]] — progression framework for eval platform sophistication
- [[AgentObservability]] — prerequisite for adaptive evaluation
- [[ARC-I2]] — puzzle benchmark demonstrating LLM pattern recognition capability
- [[OpenClaw]] — the self-adapting harness that exemplifies the need for malleable evals
