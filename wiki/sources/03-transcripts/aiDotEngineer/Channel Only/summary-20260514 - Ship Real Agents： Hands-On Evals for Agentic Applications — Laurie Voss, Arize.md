---
title: "summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize"
type: source
tags: [source, transcript, evals, agent, observability, phoenix, arize, llm-as-judge, tracing, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Core Summary
Laurie Voss (Head of Developer Experience at Arize, formerly co-founder of npm Inc.) delivers a hands-on workshop on evaluating AI agents. He walks through the full eval lifecycle: instrumenting with OpenTelemetry and Phoenix, capturing traces, reading trace data to identify failure modes, and writing three types of evals — code evals (deterministic), built-in LLM evals (correctness, faithfulness), and a custom LLM-as-judge eval for actionability. He covers meta-evaluation (judging the judge), experiments for iterative improvement, and practical frameworks like the impact hierarchy, data flywheel, Swiss cheese model, and reliability scoring. The workshop uses a financial analysis agent built with the Claude Agent SDK, powered by Claude Haiku and evaluated by Claude Sonnet via Phoenix Cloud.

## Key Points

### Evals as Tests
- Evals are tests for AI applications; traces are the log data that power them
- Spans are the building blocks of traces — each span represents one step (LLM call, tool call, agent turn) with inputs, outputs, and metadata (timing, token counts)
- The "vibes problem": teams build AI features, test with a few queries, ship, and discover failures on unexpected inputs
- Traditional unit tests don't work because the same prompt produces different (but potentially correct) outputs each run
- Human review doesn't scale — doesn't catch regressions, doesn't run in CI

### Three Types of Evals
- **Code evals**: Deterministic Python/TypeScript functions — fast, cheap, reproducible. Use for format validation, length limits, forbidden phrases, required fields. Downside: brittle for complex/non-deterministic outputs
- **LLM as judge**: A more capable LLM judges the output against a rubric (prompt defining criteria). Understands meaning, not just strings. Strengths: semantic understanding (tone, accuracy, faithfulness). Weaknesses: expensive, non-deterministic, can be wrong. Requires alignment and validation
- **Human evaluation**: Gold standard but doesn't scale. Used to build golden datasets and validate LLM judges. Human annotators get things wrong ~50% of the time due to fatigue
- These are complementary, not competing — real eval suites use all three

### Agents Make Evaluation Harder
- **Cascading failures**: An early misstep leads to radically incorrect directions. Must test: right tool picked, right parameters sent, correct understanding of tool output, correct use of previous tool output
- **Multi-agent systems**: Additional complexity — routing LLM chose right sub-agent, sub-agent understood task, passed info back correctly, stopped when supposed to
- **Don't be too prescriptive**: Agents can find faster/better paths. Evals should test the outcome, not the path taken
- Example: agent asked about Tesla — research agent assumes Nikola Tesla, writes report on 18th century inventor, forwarded to boss

### Capability Evals vs Regression Evals
- **Capability eval**: A hill to climb — something the agent is bad at, given room to improve
- **Regression eval**: Once capability eval hits 100%, it becomes a regression eval — ensures the agent can always do what it used to do
- Lifecycle: constantly turning capability evals into regression evals while adding new capability evals

### Eval Result Structure
- Score (numeric), label (human-readable), explanation (LLM judges only)
- Explanations make evals actionable — they say why something was wrong, what was missing, what the agent should have done differently
- Patterns emerge across thousands of traces: systematic failures (prompt problems) vs one-off failures (non-determinism)
- Can use a third LLM to categorize explanations at scale

### The Full Loop
Instrumentation → traces → evaluation → annotation → analysis → prompt/application improvement → repeat

### Workshop Implementation
- **Agent**: Financial analysis agent with two sub-agents (research + write report) built with Claude Agent SDK
- **Agent model**: Claude Haiku (chosen because it's "reliably dumb" — makes mistakes to test against)
- **Judge model**: Claude Sonnet (more capable model for evaluating)
- **Observability**: Phoenix Cloud with OpenTelemetry auto-instrumentation
- **Test queries**: 12 diverse queries (single ticker, comparative analysis, different focus areas)

### Reading Traces Before Writing Evals
- Must actually read traces to understand what the agent produces and what to test
- Discovered unexpected failures: agent tried to write to disk (thought it was Claude Code), wrote about AWS instead of Amazon
- Define success criteria upfront with stakeholders: what does a good report look like?
- Categorize failures: mostly looks good, possible hallucination, reasoning gaps, unverifiable data, missing recommendations
- Multiply severity × frequency to prioritize fixes

### Code Eval Example
- Test: did the output mention the expected stock ticker? Simple regex search
- Result: 11/13 passed — Tesla failed (wrote to disk), Amazon failed (only mentioned AWS, not Amazon)
- Code evals aren't just toy examples — can query databases, call APIs, anything with deterministic answers
- Test what the agent produced, not the path it took

### Built-in LLM Evals
- **Correctness eval**: Checks factual accuracy, completeness, logical consistency. Failed completely (0/13) because it used 2025 training data to judge 2026 forward-looking analysis
- **Faithfulness eval**: Checks if output is grounded in provided source material. Passed 13/13 — much more appropriate for this use case
- Lesson: choosing the right eval matters more than tuning your eval

### Custom LLM-as-Judge: Actionability
- Five parts of a good rubric: (1) Define the judge's role, (2) Explicit criteria (specific and observable, mapped to observed failures), (3) Present data clearly (XML tags, labeled fields), (4) Labeled examples (the most useful addition — LLMs learn patterns from examples), (5) Constrain output (binary yes/no, avoid 1-10 scales)
- Chain of thought before label demonstrably improves quality
- Result: 6/13 actionable — a capability eval with room to improve

### Writing Rubrics: Best Practices
- One eval per dimension — don't create a "god evaluator" that tests everything
- Guardrails (ship blockers) vs North Star metrics (nice-to-have)
- Treat evals like code: version prompts, store them, test against known answers
- Split evaluators: accuracy, completeness, tone — each with separate LLM eval
- Eval-driven development: write evals before building a feature (like TDD)

### Meta-Evaluation
- The judge is a classifier — measure performance against ground truth (human judgment)
- Build a golden dataset of known-good answers
- Split golden dataset 75/25 into training and test sets to avoid overfitting
- Use precision and recall to measure judge quality
- Human inter-rater reliability is often only 0.2-0.3 — if LLM judge achieves higher consistency, it's doing well
- Anthropic example: Opus scored 42% on CoreBench, but the eval was wrong — after fixing, score jumped to 95%
- Position bias, length bias, confidence bias, self-preference bias are known pitfalls

### Experiments
- Controlled comparison: same inputs, same evaluator, only prompt changed — any difference is attributable to the change
- Use datasets (subsets of failures) instead of running all traces every time
- Task can be a subset of agent behavior (e.g., only tool calling) for cheaper/faster experiments
- Run multiple times to account for non-determinism (Pass@K)
- Demo: improved prompt one-shotted actionability from 6/13 to 6/6 on previously failing tests

### Impact Hierarchy
- Where to invest effort: (1) Data quality fixes — highest impact, (2) Prompting improvements — few-shot examples, explicit instructions, constraints, (3) Model selection — more capable models solve problems prompting can't but cost more, (4) Hyperparameter tuning — temperature, top P, very seldom meaningful

### Data Flywheel
- More expert judgment → bigger golden dataset → better eval suite → better agents → deeper understanding of failure modes
- Creates a differentiated dataset that becomes a competitive advantage — nobody else has your evals
- Model adoption advantage: comprehensive regression evals let you know within minutes whether a new model is safe to upgrade

### Advanced Techniques
- **Production monitoring**: Continuously evaluate a percentage of production traffic; catch model drift, adversarial attacks, use case changes
- **Cost-normalized accuracy**: Accuracy divided by cost — 92% accurate at 2¢ may be better value than 95% at 15¢
- **Pairwise evaluation**: Give LLM two outputs and ask which is better — much more reliable than 1-10 ratings
- **Reliability scoring**: Pass@K (succeeds at least once in K tries) vs Pass^K (succeeds every time in K tries). Coding assistant benefits from Pass@K; customer support needs Pass^K
- **Closed-loop evaluation**: Use eval output as feedback to a coding agent that automatically improves the app
- **Multi-judge systems**: Multiple judges simultaneously for different opinions

### Swiss Cheese Model
- Borrowed from safety engineering (via Anthropic's blog)
- Each layer of defense has holes, but layered together, holes don't line up
- Code eval catches basic stuff → LLM judge catches reasoning gaps → human review catches what got through
- No single eval method captures everything — use all three simultaneously

### Sample Size Math
- 200 samples at 3% defect rate gives 95% confidence interval of 0.6%-5.4%
- 400 samples narrows to 1.3%-4.7%, consistently below 5% threshold
- 12-20 examples for directional signal; 200-400 for shipping decisions

## Related
- [[LaurieVoss]] — speaker
- [[Arize]] — company
- [[Phoenix]] — open-source observability platform
- [[ArizeAX]] — commercial product
- [[ClaudeAgentSDK]] — agent framework used
- [[Claude Haiku]] — agent model ("reliably dumb")
- [[Claude Sonnet]] — judge model
- [[Anthropic]] — model provider
- [[OpenTelemetry]] — instrumentation standard
- [[OpenInference]] — LLM-specific OTel extension
- [[npm Inc.]] — Laurie's former company
- [[CoreBench]] — benchmark with flawed eval (Anthropic example)
- [[Code Evals]] — deterministic evaluation
- [[LLMAsJudge]] — semantic evaluation technique
- [[Faithfulness Eval]] — checks grounding in source material
- [[Correctness Eval]] — checks factual accuracy
- [[Actionability Eval]] — custom eval example
- [[MetaEvaluation]] — evaluating the evaluator
- [[Capability Evals]] — hills to climb
- [[Regression Evals]] — regression testing for agents
- [[Swiss Cheese Model]] — layered defense for evals
- [[Cascading Failures]] — agent failure propagation
- [[Impact Hierarchy]] — where to invest eval effort
- [[EvalDriven Development]] — test-first for agents
- [[Pairwise Evaluation]] — comparing two outputs
- [[Reliability Scoring]] — Pass@K and Pass^K
- [[CostNormalized Accuracy]] — accuracy/cost tradeoff
- [[ClosedLoop Evaluation]] — agent auto-improvement
- [[Vibe Checking]] — informal testing problem
- [[TracesAndSpans]] — observability primitives
- [[Golden Dataset]] — ground truth for evals
- [[DataFlywheel]] — virtuous cycle of improvement
- [[AgentObservability]] — monitoring agent behavior
- [[AgentExperiments]] — controlled comparison
- [[EvalEngineering]] — practice of crafting eval prompts
- [[EvalPlatforms]] — systems for evaluation
- [[EvalMaturityStages]] — organizational progression
- [[EvalFlywheel]] — observability-evals loop
- [[FailureModeAnalysis]] — identifying failure patterns
- [[EvaluatorOptimizer Pattern]] — content refinement pattern
