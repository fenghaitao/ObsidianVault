---
title: "AgentEvaluation"
type: concept
tags: [concept, evaluation, agents, testing, production]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent.md"
last_updated: 2026-06-20
---

## Definition

Agent evaluation is the practice of measuring whether an [[AIAgent]] produces *good* outputs (behavior correctness), distinct from testing whether the agent *runs without errors* (code correctness). [[ColeMedin]] reports an industry rule of thumb: **75% of agent development time is evaluation; 25% is coding/automation.**

## Key Information

### Evaluation vs. testing

| Testing | Evaluation |
|---|---|
| Code correctness | Behavior correctness |
| "Does the application crash?" | "Is the agent's answer acceptable?" |
| Pass/fail is mechanical | Pass/fail is judgment |
| Fast, deterministic | Slow, often non-deterministic |
| Tells you about bugs | Tells you about quality regressions |

Both matter. Tests tell you the plumbing works; evaluations tell you whether what flows through it is what users actually want.

### The 75% rule

> *"When you are building AI agents, only 25% of the actual work is coding or automating. The rest of the 75% is evaluating your AI agent and making adjustments to improve your agent based on the evaluation."* — Cole Medin (citing a recurring industry stat)

This is a counter-intuitive figure for software engineers transitioning to agent work. With deterministic code, the build-vs-test ratio is more like 70/30 in favor of building. With agents, behavior probabilistic, prompts evolving, models changing, downstream effects subtle — measurement dominates.

### Evaluation methods

Three primary approaches Cole highlights:

1. **LLM-as-judge** — a separate, often stronger LLM scores the agent's outputs against a rubric. Scales well, fast, deterministic enough for regression testing. Risks: shared blind spots between agent and judge models.

2. **Task completion testing** — focuses on tool-call correctness rather than text quality. Did the agent invoke the right tools, with the right arguments, in the right order, given a stated user intent? Most directly testable for tool-using agents.

3. **Human evaluation** — user surveys, A/B tests, expert review. Slowest, most expensive, ground truth. Often the eval-of-evals (used to validate that LLM-as-judge scores correlate with human judgment).

### Worked example: evaluating skill usage ([[PydanticAI]])

From `summary-build-skills-for-any-agent`, a concrete instance of **task-completion testing** for a [[ClaudeSkills]]-style agent. The reliability worry: with dozens of skills, will the agent actually invoke the right one? (e.g. you ask for "content creation" help but it fails to pull the X-post skill because it didn't connect the dots.) Manually re-testing every skill after each change is tedious, so:

- Define YAML test cases — a **"golden dataset"** of questions (e.g. *"What's the weather in New York?"*).
- Attach a **custom evaluator** that asserts the **expected skill loaded** (e.g. the weather skill).
- Run a single script as a **cheap, fast smoke test** — Cole uses **Haiku**; 25/25 cases passed.
- A failure points to a loading bug, a weak skill **description**, or a weak system prompt.
- Run **every time** you change the system prompt or the skill set.

### When evaluation pays off

- **Pre-deployment**: catch regressions before users see them.
- **Continuous**: every prompt change or model swap can be benchmarked against historical eval sets.
- **For prompt iteration**: replaces "looks good to me" with "scores 6% higher on the rubric."
- **For model migration**: critical when moving from e.g. Sonnet 4.5 to 4.6, or considering switching providers.

### Connection to [[AgentObservability]]

Observability collects production traces; evaluation runs benchmarks against them.
- **Observability**: "what happened in production today?"
- **Evaluation**: "does the new prompt do better than the old one on this curated set of cases?"

Together they form the production feedback loop: observability surfaces failure modes → those become eval cases → eval cases drive iteration → improved agent ships → observability watches it.

## Related

- [[AIAgent]] — what's being evaluated
- [[AgentObservability]] — companion practice
- [[PydanticAI]] — ships the eval framework used in the worked example
- [[ClaudeSkills]] — the capabilities being tested for correct invocation
- [[ColeMedin]] — author of the framing here
- [[summary-how-to-learn-ai-agents-roadmap]] — primary source (phase 8)
- [[summary-build-skills-for-any-agent]] — skill-usage eval worked example
