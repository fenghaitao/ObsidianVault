---
title: "The maturity phases of running evals — Phil Hetzel, Braintrust"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"
author: "Phil Hetzel"
company: "Braintrust"
date: 2026-05-27
tags: [evals, agent-quality, maturity-model, llm-as-judge, observability, tool-calls]
---

# The maturity phases of running evals — Phil Hetzel, Braintrust

## Core Thesis

Running evals for AI agents progresses through four maturity phases that practitioners traverse as agent complexity grows. Starting with simple human vibe checks and annotation, teams progress through automated LLM-as-judge scoring, then tackle the challenges of evaluating agents that interact with external systems via tool calls, and ultimately reach advanced techniques like automated topic modeling and programmatic eval workflows. Throughout all phases, evals serve dual purposes: defense against risk (brand, compliance, cost) and offense for improvement (measuring the impact of each agent tweak).

## Key Points

### Why Evals Matter

- Evals are wholly in service to agent quality — the most important goal
- Defensive: protect against reputational risk (unkind/unhelpful agents), systems risk (cost), compliance/legal risk
- Offensive: measure how each tweak to an agent improves the application, enabling data-driven iteration
- Evals are not unit tests — they should focus on high-level failure modes, not exhaustive coverage (which is infinite)

### Eval Primitives

Every eval consists of three components:
1. **Task**: The agent or prompt under test
2. **Dataset**: Examples that initiate the task, invoking the agent/LLM workflow
3. **Scoring functions**: Methods to judge the quality of the task output

### Phase 1: Just Getting Started (Vibe Checks + Human Annotation)

- Starting with vibes is acceptable — better than nothing
- Key practice: document while vibe checking
- Have a human (builder or subject matter expert) review ~10 example outputs
- Two pieces of information required: thumbs up/down AND justification for why
- The justification extracts domain-specific knowledge from the human annotator's head
- This knowledge eventually enables scaling via LLM-as-judge
- Annotation platforms should be tailored to the specific domain, not generic
- Braintrust provides customizable human annotator views

### Phase 2: Measuring to Manage (Scaling with Automation)

- Use human justifications to derive actual failure modes (via Cursor, Cloud Code, or Codex)
- Scale human knowledge through automation:
  - **LLM-as-Judge**: Use LLMs to judge other LLMs based on identified failure modes
  - **Deterministic code-based scoring**: For objective failure modes (too many tool calls, too many tokens)
- **Critical warning**: Putting a "robe and cloak on an LLM" doesn't make it inherently more trustworthy — evaluate LLM judge outputs too
- **Dataset sourcing**: At this phase, gather production traces or UAT-level traces into the eval dataset
- Think of evals as "rerunning production" — capture production data to build confidence
- **The Flywheel**: Capture production traces → understand what's going wrong → bring examples back to offline environment → rerun production through evals → guide improvement direction

### Phase 3: Accounting for Complexity (Tool Calls + External Systems)

- Agents now interact with external systems via tool calls
- Two types of tool calls:
  - **Context-gathering tools**: Gathering data and injecting it into the LLM
  - **CRUD-based tools**: Creating, reading, updating, or deleting from external systems
- Both types increase the vectors for failure
- Now evaluating entire agent traces, not just final outputs
- Need tooling to capture large traces and target evals at individual tool/MCP calls
- Two key challenges with CRUD tools:
  1. Representing the state of external systems at the time the eval input was created
  2. Interacting with those systems without overwriting production data
- **Solutions**: Mock-level APIs to approximate production; cram system state into traces and inject into eval tasks; timestamp-based version queries to vector databases

### Phase 4: Advanced Eval Techniques

- **Topic modeling at scale**: Automatically uncover failure modes in production without manual review
- **Programmatic evals**: Using coding agents (Cloud Code, Codex) and eval provider CLIs to run evals in automated workflows
- These patterns are emerging and represent the frontier of the space

### LLM-as-Judge Best Practices

- LLM-as-judge is effective but not inherently trustworthy
- Must evaluate LLM judge outputs against human ground truth
- Deterministic code-based evals can complement LLM judges for objective failure modes
- Some things are inherently subjective — that's why agents are powerful, and why LLM-as-judge is necessary
- Create ground truth datasets for LLM judge outputs to validate alignment with human judgment

## Entities

- [[PhilHetzel]] — Solutions engineering lead at Braintrust, presenter
- [[Braintrust]] — Agent quality company (evals + observability)
- [[KPMG]] — Consulting firm where Phil worked for 4 years
- [[SlalomConsulting]] — Consulting firm where Phil led the global Databricks business unit for 8 years

## Concepts

- [[EvalPracticePhases]] — Four-phase maturity model for running evals (practitioner view)
- [[EvalPrimitives]] — Task, dataset, scoring function as the three components of an eval
- [[EvalFlywheel]] — Production traces → analysis → offline experimentation → improvement
- [[HumanAnnotation]] — Thumbs up/down with justification as the foundation for scaling eval knowledge
- [[LLM-as-Judge]] — Using LLMs to judge other LLM outputs, with trustworthiness caveats
- [[FailureModeAnalysis]] — Deriving failure modes from human annotations to build automated scoring
- [[Meta-Evaluation]] — Evaluating LLM judge outputs against ground truth
- [[EvalDataCapture]] — Capturing production and UAT traces for eval datasets
- [[ToolCallsInEvals]] — How tool calls complicate evaluation (context-gathering vs CRUD, mock APIs, trace injection)
- [[DeterministicEval]] — Code-based deterministic evaluation scoring for objective failure modes
- [[TopicModelingForEvals]] — Automatically uncovering failure modes in production
- [[AgentObservability]] — Observability and evals as the same problem from a systems perspective
- [[TraceLinkedEvaluations]] — Evaluating entire agent traces, not just outputs

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — companion talk on platform maturity stages
- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — related talk on cross-functional teams
- [[EvalMaturityStages]] — platform-building maturity stages (complementary framework)
