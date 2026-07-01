---
title: "EvalScopes"
type: concept
tags: [evals, observability, agent, evaluation, spans, trajectories, sessions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Eval Scopes is a taxonomy introduced by Dat Ngo (Arize) that categorizes AI evaluations by their scope and depth, from granular single-component checks to holistic session-level assessments. The four scopes are: span eval, multi-span eval, trajectory eval, and session-level eval.

## Key Information

### Span Eval (Single Component)
- Scope: One single input and output of one part of an LLM call or agent component
- Simplest form of eval — most people understand this
- Example: Check if a single LLM response contains the expected information, or if a tool call returned valid JSON
- Good for unit-level quality checks on individual components

### Multi-Span Eval (Cross-Component)
- Scope: Requires data across many different components in the system
- Used when eval criteria span multiple system parts
- Example: "How well are agents passing data back and forth to each other?" — requires data from every agent and how they pass data
- Enables evaluating cross-component interactions and data flow integrity

### Trajectory Eval (Full Path)
- Scope: All spans in total — the complete path the agent took
- Answers: "Did we call things in the right trajectory/order to finish the business process?"
- Used to identify ordering issues: e.g., component B called before A, but B has a dependency on A — the LLM's call ordering was mismatched
- Root cause analysis: when evals drop on a particular branch, trajectory analysis identifies which components are out of order
- Key insight: sometimes B before A is the root cause of failures, and the fix is adding context to instruct the LLM about ordering dependencies

### Session-Level Eval (State Machine)
- Scope: The full conversation state machine — zooming out from individual turns
- Answers: "Was the user ever frustrated in this conversation? Did we answer all of their questions?"
- Evaluates the state machine of the entire interaction, not just individual agent turns
- Think of it as evaluating whether the end user was satisfied and all questions were addressed

### Usage Guidance
- Just because you can eval something doesn't mean you always should
- Goal: find the minimal set of evals that provides signal about whether the application works as intended
- There is a cost associated with each eval — be cost-aware and scope evals appropriately

## Related
- [[DatNgo]] — speaker who introduced this taxonomy
- [[Arize]] — platform that implements these eval scopes
- [[TracesAndSpans]] — the underlying observability primitives
- [[Trajectory Analysis]] — trajectory-level analysis for root cause
- [[AgentObservability]] — the broader observability context
- [[LLMAsJudge]] — evaluation technique applicable at any scope
- [[DeterministicEval]] — code-based evals at span level
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
