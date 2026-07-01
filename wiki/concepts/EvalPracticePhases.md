---
title: "Eval Practice Phases"
type: concept
category: framework
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Eval Practice Phases is a four-phase maturity model describing how practitioners progress in running evaluations for AI agents, from basic human vibe checks to advanced automated techniques. It represents a continuum (not discrete stages) that teams traverse as agent complexity grows and more failure vectors emerge. This is the practitioner view, distinct from the [[EvalMaturityStages]] framework which describes platform-building maturity.

## Key Information

### Phase 1: Just Getting Started
- **Approach**: Vibe checks with human annotation
- Starting with vibes is acceptable — better than nothing
- Run agent on ~10 example inputs, loop through outputs
- Human (builder or subject matter expert) provides thumbs up/down plus justification
- Justification extracts domain-specific knowledge from the annotator's head
- Annotation platforms should be domain-specific, not generic
- Output: documented human judgments that can later seed automated scoring

### Phase 2: Measuring to Manage
- **Approach**: Derive failure modes from human annotations, scale with automation
- Use coding agents (Cursor, Cloud Code, Codex) to derive failure modes from justifications
- Build automated scoring via LLM-as-judge for subjective dimensions and deterministic code for objective ones
- Capture production/UAT traces into eval datasets
- Think of evals as "rerunning production" — the [[EvalFlywheel]] begins here
- Critical: evaluate LLM judge outputs too — putting "a robe and cloak on an LLM" doesn't make it trustworthy

### Phase 3: Accounting for Complexity
- **Approach**: Evaluate agents that interact with external systems via tool calls
- Two tool call types: context-gathering (data injection) and CRUD-based (modifying external systems)
- Now evaluating entire agent traces, not just final outputs
- Key challenges: representing external system state at eval time, avoiding production data overwrites
- Solutions: mock APIs, cram system state into traces, timestamp-based version queries
- Requires tooling to capture large traces and target evals at individual tool/MCP calls

### Phase 4: Advanced Eval Techniques
- **Approach**: Automated discovery and programmatic workflows
- Topic modeling at scale to automatically uncover failure modes in production
- Programmatic evals using coding agents and eval provider CLIs for automated workflows
- These are emerging patterns at the frontier of the space

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[EvalMaturityStages]] — complementary framework for platform-building maturity
- [[EvalPrimitives]] — the three components of every eval
- [[EvalFlywheel]] — the continuous loop enabled at Phase 2
- [[HumanAnnotation]] — the foundation practice of Phase 1
- [[LLMAsJudge]] — scaling technique at Phase 2
- [[ToolCallsInEvals]] — the complexity challenge of Phase 3
- [[DeterministicEval]] — code-based scoring used alongside LLM-as-judge
- [[TopicModelingForEvals]] — advanced technique at Phase 4
